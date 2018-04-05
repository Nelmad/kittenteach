import abc
import re
from uuid import uuid4

import requests
from django.conf import settings

from kittenteach.core.utils.utils import singleton
from slugify import Slugify

c_slugify = Slugify(separator='_', to_lower=True)


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    return x_forwarded_for.split(',')[0] if x_forwarded_for else request.META.get('REMOTE_ADDR')


class ABClient(abc.ABC):
    cookie_fmt = 'client_id_{}'

    @abc.abstractmethod
    def participate(self, *args):
        pass

    @abc.abstractmethod
    def convert(self, *args):
        pass

    @abc.abstractmethod
    def check_cookie(self, *args):
        pass

    @abc.abstractmethod
    def set_cookie(self, *args):
        pass

    def get_cookie_name(self, experiment_name):
        return self.cookie_fmt.format(c_slugify(experiment_name))


@singleton
class SixpackClient(ABClient):
    def __init__(self, host=None, *, timeout=None):
        self.host = str(host if host is not None else settings.SIXPACK_SETTINGS.get('host'))
        if not self.host.startswith(("http://", "https://")):
            self.host = f"http://{self.host}"

        self.timeout = float(timeout if timeout is not None else settings.SIXPACK_SETTINGS.get('timeout'))

        self.__valid_name_re = re.compile(r"^[a-z0-9][a-z0-9\-_ ]*$", re.I)

    def participate(self, request, experiment_name, *, alternatives, force=None, traffic_fraction=1, prefetch=False):
        if not self.name_is_valid(experiment_name):
            raise ValueError('Bad experiment name (should contain only letters and digits)')

        if len(alternatives) < 2:
            raise ValueError('Must specify at least 2 alternatives')

        if any(not self.name_is_valid(alt) for alt in alternatives):
            raise ValueError('Bad alternative name (should contain only letters and digits)')

        if not (0 <= float(traffic_fraction) <= 1):
            raise ValueError('Bad traffic_fraction specified (should be a number between 0 and 1')

        client_id = request.COOKIES.get(self.get_cookie_name(experiment_name))
        if client_id is None:
            client_id = uuid4()
            new_user = True
        else:
            new_user = False

        user_agent = request.META.get('HTTP_USER_AGENT')
        ip_address = get_client_ip(request)

        params = {
            'client_id': client_id,
            'experiment': experiment_name,
            'alternatives': list(alternatives),
            'prefetch': prefetch,
            'traffic_fraction': traffic_fraction,
            # to detect bot
            'user_agent': user_agent,
            'ip_address': ip_address,
        }

        if force is not None and force in alternatives:
            params['force'] = force
            params['record_force'] = True

        response = self.get_response('/participate', params)

        if response['status'] == 'failed':
            default_alt_name = list(alternatives)[0]
            try:
                default_alt_value = alternatives[default_alt_name]
            except TypeError:
                default_alt_value = None

            response['alternative'] = {'name': default_alt_name, 'value': default_alt_value}
        else:
            try:
                alt_value = alternatives[response['alternative']['name']]
            except TypeError:
                alt_value = None

            response['new_user'] = new_user
            response['alternative']['value'] = alt_value

        return response

    def convert(self, request, experiment_name, *, kpi=None):
        if not self.name_is_valid(experiment_name):
            raise ValueError('Bad experiment name')

        client_id = request.COOKIES.get(self.get_cookie_name(experiment_name))
        user_agent = request.META.get('HTTP_USER_AGENT')
        ip_address = get_client_ip(request)

        params = {
            'experiment': experiment_name,
            'client_id': client_id,
            'user_agent': user_agent,
            'ip_address': ip_address,
        }

        if kpi:
            if not self.name_is_valid(kpi):
                raise ValueError('Bad KPI name: {0}'.format(kpi))
            params['kpi'] = kpi

        return self.get_response('/convert', params)

    def get_response(self, endpoint=None, params=None):
        url = f"{self.host}{endpoint}"

        try:
            response = requests.get(url, params=params, timeout=self.timeout)
        except Exception:
            return {
                "status": "failed",
                "response": "http error: sixpack is unreachable"
            }

        if response.status_code != 200:
            return {
                "status": "failed",
                "response": response.content
            }

        try:
            return response.json()
        except ValueError:
            return {
                "status": "failed",
                "response": response.content
            }

    def name_is_valid(self, name):
        return self.__valid_name_re.match(name)

    def check_cookie(self, response, sixpack_response):
        if sixpack_response['status'] != 'failed' and sixpack_response['new_user']:
            self.set_cookie(response, sixpack_response)

    def set_cookie(self, response, sixpack_response):
        experiment = sixpack_response.get('experiment')

        if experiment is not None:
            experiment_name = experiment['name']
            client_id = sixpack_response['client_id']

            response.set_cookie(self.get_cookie_name(experiment_name), client_id)

# TODO add optimizely if free

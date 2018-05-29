from django.conf import settings


def base(request):
    return {
        'client_js': settings.FRONTEND_SETTINGS.get('client_js'),
        'client_css': settings.FRONTEND_SETTINGS.get('client_css'),
        'client_less': settings.FRONTEND_SETTINGS.get('client_less'),
        'static': settings.STATIC_URL
    }


def csrf(request):
    return {
        'csrf_header_name': settings.CSRF_HEADER_NAME,
        'csrf_cookie_name': settings.CSRF_COOKIE_NAME,
        'csrf_token_name': 'csrfmiddlewaretoken',
    }

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.template import loader


def index(request):
    # general access
    template = loader.get_template('core/home.html')

    context = {
        'show_header': True,
        'show_footer': True,
        'title': "home page",
        'init_js_script': 'Home'
    }

    return HttpResponse(template.render(context, request))


@login_required(login_url="login")
def dashboard(request):
    pass


def login(request):
    template = loader.get_template('core/login.html')

    context = {
        'show_header': True,
        'show_footer': False,
        'title': "registration",
    }

    return HttpResponse(template.render(context, request))

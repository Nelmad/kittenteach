from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.template import loader


def index(request):
    # general access
    template = loader.get_template('core/home.html')

    context = {
        'title': 'home page',
        'show_header': True,
        'show_footer': True,
        'init_js_script': 'Home'
    }

    return HttpResponse(template.render(context, request))


@login_required
def dashboard(request):
    pass


def login(request):
    # TODO redirect if authenticated
    template = loader.get_template('core/login.html')
    context = {
        'show_header': True,
        'show_footer': False,
        'title': '',
        'init_js_script': 'Auth',
    }

    return HttpResponse(template.render(context, request))


def handler404(request):
    template = loader.get_template('core/errors/404.html')
    context = {
        'show_header': True,
        'show_footer': False,
        'title': 'Page not found',
    }

    return HttpResponse(template.render(context, request))


def test404(request):
    template = loader.get_template('core/errors/404.html')
    context = {
        'show_header': True,
        'show_footer': False,
        'title': 'Page not found',
    }

    return HttpResponse(template.render(context, request))

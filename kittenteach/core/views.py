from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.template import loader


def index(request):
    # general access
    template = loader.get_template('core/home.html')

    context = {
        'title': 'KittenTeach - Smart Education',
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
        'title': 'Start using KittenTeach',
        'show_header': True,
        'show_footer': False,
    }

    return HttpResponse(template.render(context, request))


def teachers(request):
    template = loader.get_template('core/teachers.html')
    context = {
        'title': 'Choose your teacher',
        'show_header': True,
        'show_footer': True,
    }

    return HttpResponse(template.render(context, request))


def subjects(request):
    template = loader.get_template('core/subjects.html')
    context = {
        'title': 'Subjects available for you',
        'show_header': True,
        'show_footer': True,
    }

    return HttpResponse(template.render(context, request))


def schools(request):
    template = loader.get_template('core/schools.html')
    context = {
        'title': 'Schools for best education',
        'show_header': True,
        'show_footer': True,
    }

    return HttpResponse(template.render(context, request))


@login_required
def account(request):
    template = loader.get_template('core/account.html')
    context = {
        'show_header': True,
        'show_footer': True,
        'title': 'KittenTeach: '
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

from django.conf import settings


def base(request):
    return {
        'minify_front': settings.MINIFY_FRONT,
        'client_js': settings.FRONTEND_SETTINGS['client_js'],
        'client_css': settings.FRONTEND_SETTINGS['client_css'],
    }


def csrf(request):
    return {
        'csrf_header_name': settings.CSRF_HEADER_NAME,
        'csrf_cookie_name': settings.CSRF_COOKIE_NAME,
    }

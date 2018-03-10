from django.conf import settings


def base(request):
    return {
        'minify_front': settings.MINIFY_FRONT,
        'client_js': settings.FRONTEND_SETTINGS['client_js'],
        'client_css': settings.FRONTEND_SETTINGS['client_css'],
    }

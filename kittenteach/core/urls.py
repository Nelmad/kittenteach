from django.contrib.auth.views import logout_then_login
from django.urls import path
from django.views.i18n import JavaScriptCatalog

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('teachers/', views.teachers, name='teachers'),
    path('subjects/', views.subjects, name='subjects'),
    path('schools/', views.schools, name='schools'),

    path('login/', views.login, name='login'),
    path('logout/', logout_then_login, {'login_url': 'login'}, name='logout'),
    path('account/', views.account, name='account'),
    # path('logout/', views.logout, name='logout'),

    path('test404/', views.test404, name='test404'),

    # jsi18n
    path('jsi18n/', JavaScriptCatalog.as_view(), name='javascript-catalog'),
]

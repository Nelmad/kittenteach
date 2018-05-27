from django.urls import path
from django.views.i18n import JavaScriptCatalog

from . import views

urlpatterns = [
    path('', views.index, name='index'),

    path('login/', views.login, name='login'),
    # path('logout/', views.logout, name='logout'),

    path('dashboard/', views.dashboard, name='dashboard'),
    path('test404/', views.test404, name='dashboard'),

    # jsi18n
    path('jsi18n/', JavaScriptCatalog.as_view(), name='javascript-catalog'),
]

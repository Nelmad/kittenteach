from django.conf.urls import url
from django.urls import include
from rest_framework import routers

from kittenteach.api.views import registration
from . import views

#
# router = routers.DefaultRouter()
# router.register(r'users', views.UserViewSet)
# router.register(r'students', views.StudentViewSet)
# router.register(r'teachers', views.TeacherViewSet)
# router.register(r'subjects', views.SubjectViewSet)

urlpatterns = [
    # url(r'^', include(router.urls)),
    url(r'^reg$', registration),

    url(r'^student$', views.StudentCreateView.as_view()),

    # url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^auth/', include('djoser.urls')),
    url(r'^auth/', include('djoser.urls.authtoken')),
]

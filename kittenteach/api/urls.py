from django.conf.urls import url
from rest_framework.authtoken import views as authtoken_views

from . import views

urlpatterns = [
    # auth
    url(r'^auth$', authtoken_views.ObtainAuthToken.as_view(), name='token-auth'),

    # students
    url(r'^students/create$', views.StudentCreateView.as_view(), name='student-create'),
    url(r'^students/(?P<pk>[0-9]+)$', views.StudentRetrieveView.as_view(), name='student-details'),
    url(r'^students$', views.StudentListView.as_view(), name='students-list'),

    # teachers
    url(r'^teachers/create$', views.TeacherCreateView.as_view(), name='teacher-create'),
    url(r'^teachers/(?P<pk>[0-9]+)$', views.TeacherRetrieveView.as_view(), name='teacher-details'),
    url(r'^teachers$', views.TeacherListView.as_view(), name='teachers-list'),

    # url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]

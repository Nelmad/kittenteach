from django.urls import re_path

from . import views

urlpatterns = [
    # auth
    re_path(r'^auth/?$', views.ObtainAuthToken.as_view(), name='token-auth'),

    # students
    re_path(r'^students/create/?$', views.StudentCreateView.as_view(), name='student-create'),
    re_path(r'^students/(?P<pk>\d+)/?$', views.StudentRetrieveView.as_view(), name='student-details'),
    re_path(r'^students/?$', views.StudentListView.as_view(), name='students-list'),

    # teachers
    re_path(r'^teachers/create/?$', views.TeacherCreateView.as_view(), name='teacher-create'),
    re_path(r'^teachers/(?P<pk>\d+)/?$', views.TeacherRetrieveView.as_view(), name='teacher-details'),
    re_path(r'^teachers/?$', views.TeacherListView.as_view(), name='teachers-list'),

    # subjects
    re_path(r'^subjects/create/?$', views.SubjectCreateView.as_view(), name='subject-create'),
    re_path(r'^subjects/(?P<pk>\d+)/?$', views.SubjectRetrieveView.as_view(), name='subject-details'),
    re_path(r'^subjects/?$', views.SubjectListView.as_view(), name='subjects-list'),

    # url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]

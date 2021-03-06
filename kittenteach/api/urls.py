from django.urls import re_path

from . import views

urlpatterns = [
    # auth
    re_path(r'^auth/?$', views.ObtainAuthToken.as_view(), name='token-auth'),
    re_path(r'^reset-password/?$', views.reset_password, name='reset-password'),
    re_path(r'^current-user-details/?$', views.current_user_details, name='current-user-details'),

    # students
    re_path(r'^students/?$', views.StudentListView.as_view(), name='students-list'),
    re_path(r'^students/(?P<pk>\d+)/?$', views.StudentRetrieveView.as_view(), name='student-details'),
    re_path(r'^students/create/?$', views.StudentCreateView.as_view(), name='student-create'),

    # teachers
    re_path(r'^teachers/?$', views.TeacherListView.as_view(), name='teachers-list'),  # TODO get list of teachers for concrete subject -> ?subject = <subject_name>
    re_path(r'^teachers/(?P<pk>\d+)/?$', views.TeacherRetrieveView.as_view(), name='teacher-details'),
    re_path(r'^teachers/create/?$', views.TeacherCreateView.as_view(), name='teacher-create'),
    re_path(r'^teachers/update/?$', views.TeacherSafeUpdateView.as_view(), name='teacher-update'),
    re_path(r'^teachers/remove/?$', views.TeacherSafeRemoveView.as_view(), name='teacher-remove'),  # TODO <<<<

    # authorized teacher groups
    re_path(r'^teachers/groups/?$', views.TeacherGroupsListView.as_view(), name='teacher-groups-list'),
    re_path(r'^teachers/groups/(?P<pk>\d+)/?$', views.TeacherGroupDetailsView.as_view(), name='teacher-group-details'),
    re_path(r'^teachers/groups/create/?$', views.TeacherGroupCreateView.as_view(), name='teacher-group-create'),
    re_path(r'^teachers/groups/(?P<pk>\d+)/update/?$', views.TeacherGroupSafeUpdateView.as_view(), name='teacher-group-update'),
    re_path(r'^teachers/groups/(?P<pk>\d+)/remove/?$', views.TeacherGroupSafeRemoveView.as_view(), name='teacher-group-remove'),

    # schedule
    re_path(r'^teachers/lessons-templates/?$', views.LessonTemplateListView.as_view(), name='templates-list'),
    # re_path(r'^teachers/lessons-templates/(?P<pk>\d+)/?$', lambda: '', name='template-details'),
    re_path(r'^teachers/lessons-templates/create/?$', views.LessonTemplateCreateView.as_view(), name='template-create'),

    # subjects
    re_path(r'^subjects/?$', views.SubjectListView.as_view(), name='subjects-list'),
    re_path(r'^subjects/(?P<pk>\d+)/?$', views.SubjectRetrieveView.as_view(), name='subject-details'),  # TODO subject slug field instead of pk
    re_path(r'^subjects/create/?$', views.SubjectCreateView.as_view(), name='subject-create'),

    # schools
    re_path(r'^schools/?$', views.SchoolsListView.as_view(), name='schools-list'),
    re_path(r'^schools/(?P<pk>\d+)/?$', views.SchoolDetailsView.as_view(), name='school-details'),  # TODO school slug field instead of pk
    re_path(r'^schools/create/?$', views.SchoolCreateView.as_view(), name='school-create'),
    re_path(r'^schools/(?P<pk>\d+)/update/?$', views.SchoolSafeUpdateView.as_view(), name='school-update'),
    re_path(r'^schools/(?P<pk>\d+)/remove/?$', views.SchoolSafeRemoveView.as_view(), name='school-remove'),  # TODO <<<<
]

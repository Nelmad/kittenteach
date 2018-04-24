from django.urls import re_path

from . import views

urlpatterns = [
    # auth
    re_path(r'^auth/?$', views.ObtainAuthToken.as_view(), name='token-auth'),

    # students
    re_path(r'^students/?$', views.StudentListView.as_view(), name='students-list'),
    re_path(r'^students/(?P<pk>\d+)/?$', views.StudentRetrieveView.as_view(), name='student-details'),
    re_path(r'^students/create/?$', views.StudentCreateView.as_view(), name='student-create'),

    # teachers
    re_path(r'^teachers/?$', views.TeacherListView.as_view(), name='teachers-list'),  # TODO get list of teachers for concrete subject -> ?subject = <subject_name>
    re_path(r'^teachers/(?P<pk>\d+)/?$', views.TeacherRetrieveView.as_view(), name='teacher-details'),
    re_path(r'^teachers/create/?$', views.TeacherCreateView.as_view(), name='teacher-create'),
    re_path(r'^teachers/update/?$', views.TeacherSafeUpdateView.as_view(), name='teacher-update'),
    re_path(r'^teachers/remove/?$', views.TeacherSafeRemoveView.as_view(), name='teacher-remove'),

    # authorized teacher groups
    re_path(r'^teachers/groups/?$', views.TeacherGroupsListView.as_view(), name='teacher-groups-list'),
    re_path(r'^teachers/groups/(?P<pk>\d+)/?$', views.TeacherGroupDetailsView.as_view(), name='teacher-group-details'),
    re_path(r'^teachers/groups/create?$', views.TeacherGroupCreateView.as_view(), name='teacher-groups-create'),

    # subjects
    re_path(r'^subjects/?$', views.SubjectListView.as_view(), name='subjects-list'),
    re_path(r'^subjects/(?P<pk>\d+)/?$', views.SubjectRetrieveView.as_view(), name='subject-details'),  # TODO subject slug field instead of pk
    re_path(r'^subjects/create/?$', views.SubjectCreateView.as_view(), name='subject-create'),
]

from django.conf.urls import url

from . import views

urlpatterns = [
    # students
    # url(r'^students', views.StudentsList.as_view()),
    url(r'^students/create', views.StudentCreateView.as_view(), name='student-create'),

    # teachers
    url(r'^teachers/create', views.TeacherCreateView.as_view(), name='teacher-create'),

    # url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]

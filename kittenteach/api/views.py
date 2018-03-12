from django.contrib.auth.models import User
from rest_framework import viewsets

from kittenteach.api.serializers import UserSerializer, StudentSerializer, TeacherSerializer
from kittenteach.core.models import Student, Teacher
from kittenteach.api.viewsets import ProfileViewSet


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows users to be viewed.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class StudentViewSet(ProfileViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class TeacherViewSet(ProfileViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer


def auth(request):
    pass

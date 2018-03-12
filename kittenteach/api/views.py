from django.contrib.auth.models import User
from rest_framework import viewsets

from kittenteach.api.serializers import UserSerializer, StudentSerializer, TeacherSerializer, SubjectSerializer
from kittenteach.api.viewsets import ProfileViewSet
from kittenteach.core.models import Student, Teacher, Subject


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


class SubjectViewSet(viewsets.ModelViewSet):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer


def auth(request):
    pass

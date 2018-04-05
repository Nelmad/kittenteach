from django.contrib.auth.models import User
from django.http import HttpResponse
from rest_framework import viewsets, permissions
from rest_framework.generics import CreateAPIView

from kittenteach.api.serializers import UserSerializer, StudentSerializer, TeacherSerializer, SubjectSerializer, \
    StudentCreateSerializer
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


class StudentCreateView(CreateAPIView):
    serializer_class = StudentCreateSerializer
    permission_classes = [permissions.AllowAny]


class TeacherViewSet(ProfileViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer


class SubjectViewSet(viewsets.ModelViewSet):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer


def registration(request):
    from djoser.conf import settings
    # print(Student.user.REQUIRED_FIELDS)
    return HttpResponse('')


class StudentCreateView(CreateAPIView):
    serializer_class = StudentCreateSerializer

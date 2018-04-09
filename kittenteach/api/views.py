from rest_framework import generics, permissions

from kittenteach.api import serializers
from kittenteach.core import models


class StudentCreateView(generics.CreateAPIView):
    """
    Student create endpoint
    """
    serializer_class = serializers.StudentCreateSerializer
    queryset = models.Student.objects.all()
    permission_classes = [permissions.AllowAny]


class TeacherCreateView(generics.CreateAPIView):
    """
    Teacher create endpoint
    """
    serializer_class = serializers.TeacherCreateSerializer
    queryset = models.Teacher.objects.all()
    permission_classes = [permissions.AllowAny]


class StudentDetailsView(generics.RetrieveAPIView):
    """
    Student details endpoint
    """
    serializer_class = serializers.StudentDetailsSerializer
    queryset = models.Student.objects.all()
    permission_classes = [permissions.AllowAny]


class TeacherDetailsView(generics.RetrieveAPIView):
    """
    Teacher details endpoint
    """
    serializer_class = serializers.TeacherDetailsSerializer
    queryset = models.Teacher.objects.all()
    permission_classes = [permissions.AllowAny]


class StudentListView(generics.ListAPIView):
    """
    Students list endpoint
    """
    serializer_class = serializers.StudentListSerializer
    queryset = models.Student.objects.all()
    # TODO get students list available only for teachers
    # permission_classes = [permissions.IsAuthenticated]
    permission_classes = [permissions.AllowAny]


class TeacherListView(generics.ListAPIView):
    """
    Teachers list endpoint
    """
    serializer_class = serializers.TeacherListSerializer
    queryset = models.Teacher.objects.all()
    permission_classes = [permissions.AllowAny]

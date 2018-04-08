from rest_framework import generics, permissions

from kittenteach.api import serializers
from kittenteach.core import models


# Student Views
class StudentCreateView(generics.CreateAPIView):
    """
    Student create endpoint
    """
    serializer_class = serializers.StudentCreateSerializer
    queryset = models.Student.objects.all()
    permission_classes = [permissions.AllowAny]


# Teacher Views
class TeacherCreateView(generics.CreateAPIView):
    """
    Teacher create endpoint
    """
    serializer_class = serializers.TeacherCreateSerializer
    queryset = models.Teacher.objects.all()
    permission_classes = [permissions.AllowAny]




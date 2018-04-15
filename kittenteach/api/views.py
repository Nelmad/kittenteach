from django.contrib.auth import user_logged_in
from rest_framework import generics, permissions, filters
from rest_framework.authtoken import models as authtoken_models
from rest_framework.authtoken import views as authtoken_views
from rest_framework.response import Response

from kittenteach.api import serializers
from kittenteach.core import models


class ObtainAuthToken(authtoken_views.ObtainAuthToken):
    """
    Obtain auth-token for user
    """
    serializer_class = serializers.AuthTokenSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)

        user = serializer.validated_data['user']
        token, created = authtoken_models.Token.objects.get_or_create(user=user)

        user_logged_in.send(sender=user.__class__, request=request, user=user)
        return Response({'token': token.key})


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


class StudentRetrieveView(generics.RetrieveAPIView):
    """
    Student retrieve endpoint
    """
    serializer_class = serializers.StudentDetailsSerializer
    queryset = models.Student.objects.all()
    permission_classes = [permissions.AllowAny]


class TeacherRetrieveView(generics.RetrieveAPIView):
    """
    Teacher retrieve endpoint
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
    filter_backends = (filters.SearchFilter,)
    search_fields = ('user__first_name', 'user__last_name')
    # TODO get students list available only for teachers
    # permission_classes = [permissions.IsAuthenticated]
    permission_classes = [permissions.AllowAny]


class TeacherListView(generics.ListAPIView):
    """
    Teachers list endpoint
    """
    serializer_class = serializers.TeacherListSerializer
    queryset = models.Teacher.objects.all()
    filter_backends = (filters.SearchFilter,)
    search_fields = ('user__first_name', 'user__last_name')
    permission_classes = [permissions.AllowAny]

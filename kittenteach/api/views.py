from django.contrib import auth
from django.contrib.auth import user_logged_in
from django.http import Http404
from rest_framework import generics, permissions as rest_permissions
from rest_framework import filters as rest_filters
from rest_framework.authtoken import models as authtoken_models
from rest_framework.authtoken import views as authtoken_views
from rest_framework.response import Response
from django_filters import rest_framework as d_filters

from kittenteach.api import serializers, permissions, filters
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

        # TODO check if inactive
        auth.login(request, user)  # TODO
        user_logged_in.send(sender=user.__class__, request=request, user=user)
        return Response({'token': token.key})


class StudentCreateView(generics.CreateAPIView):
    """
    Student create endpoint
    """
    serializer_class = serializers.StudentCreateSerializer
    queryset = models.Student.objects.all()
    permission_classes = [rest_permissions.AllowAny]


class TeacherCreateView(generics.CreateAPIView):
    """
    Teacher create endpoint
    """
    serializer_class = serializers.TeacherCreateSerializer
    queryset = models.Teacher.objects.all()
    permission_classes = [rest_permissions.AllowAny]


class TeacherGroupCreateView(generics.CreateAPIView):
    """
    Create group for authorized teacher
    """
    serializer_class = serializers.TeacherGroupCreateSerializer
    queryset = models.Group.objects.all()
    rest_permissions = [permissions.IsTeacher]

    def create(self, request, *args, **kwargs):
        try:
            request.data['teacher'] = request.user.teacher.pk
        except models.Teacher.DoesNotExist:
            raise Http404
        else:
            return super().create(request, *args, **kwargs)


class SubjectCreateView(generics.CreateAPIView):
    """
    Student create endpoint
    """
    serializer_class = serializers.SubjectCreateSerializer
    queryset = models.Subject.objects.all()
    permission_classes = [permissions.IsTeacher]


class StudentRetrieveView(generics.RetrieveAPIView):
    """
    Student retrieve endpoint
    """
    serializer_class = serializers.StudentDetailsSerializer
    queryset = models.Student.objects.all()
    permission_classes = [rest_permissions.AllowAny]


class TeacherRetrieveView(generics.RetrieveAPIView):
    """
    Teacher retrieve endpoint
    """
    serializer_class = serializers.TeacherDetailsSerializer
    queryset = models.Teacher.objects.all()
    permission_classes = [rest_permissions.AllowAny]


class SubjectRetrieveView(generics.RetrieveAPIView):
    """
    Subject retrieve endpoint
    """
    serializer_class = serializers.SubjectDetailsSerializer
    queryset = models.Subject.objects.all()
    permission_classes = [rest_permissions.AllowAny]


class StudentListView(generics.ListAPIView):
    """
    Students list endpoint
    """
    serializer_class = serializers.StudentListSerializer
    queryset = models.Student.objects.all()
    filter_backends = (rest_filters.SearchFilter,)
    search_fields = ('user__first_name', 'user__last_name')
    # TODO get students list available only for teachers
    # permission_classes = [permissions.IsTeacher]
    permission_classes = [rest_permissions.AllowAny]


class TeacherListView(generics.ListAPIView):
    """
    Teachers list endpoint
    """
    serializer_class = serializers.TeacherListSerializer
    queryset = models.Teacher.objects.all()
    filter_backends = (rest_filters.SearchFilter, d_filters.DjangoFilterBackend)
    # filter_class = filters.TeacherFilterSet  # TODO custom filter set
    search_fields = ('user__first_name', 'user__last_name')
    filter_fields = ('subjects__name',)
    permission_classes = [rest_permissions.AllowAny]


class SubjectListView(generics.ListAPIView):
    """
    Subject list endpoint
    """
    serializer_class = serializers.SubjectListSerializer
    queryset = models.Subject.objects.all()
    filter_backends = (rest_filters.SearchFilter,)
    search_fields = ('name',)
    permission_classes = [rest_permissions.AllowAny]


class TeacherSafeUpdateView(generics.UpdateAPIView):
    """
    Teacher safe update endpoint
    Updates existing many2many fields values with given
    For other fields sets value (default behavior)
    """
    serializer_class = serializers.TeacherSafeUpdateSerializer
    permission_classes = [permissions.IsTeacher]

    def get_object(self):
        try:
            return self.request.user.teacher
        except models.Teacher.DoesNotExist:
            raise Http404


class TeacherSafeRemoveView(generics.UpdateAPIView):
    """
    Teacher safe remove endpoint
    Removes given values from many2many fields
    """
    serializer_class = serializers.TeacherSafeRemoveSerializer
    permission_classes = [permissions.IsTeacher]

    def get_object(self):
        try:
            return self.request.user.teacher
        except models.Teacher.DoesNotExist:
            raise Http404


class TeacherGroupDetailsView(generics.RetrieveAPIView):
    """

    """
    serializer_class = serializers.TeacherGroupDetailsSerializer
    permission_classes = [permissions.IsTeacher]

    def get_queryset(self):
        try:
            teacher = self.request.user.teacher
            return teacher.groups
        except models.Teacher.DoesNotExist:
            raise Http404


class TeacherGroupsListView(generics.ListAPIView):
    """

    """
    serializer_class = serializers.TeacherGroupListSerializer
    permission_classes = [permissions.IsTeacher]

    def get_queryset(self):
        try:
            teacher = self.request.user.teacher
            return teacher.groups.all()
        except models.Teacher.DoesNotExist:
            raise Http404


class SchoolDetailsView(generics.RetrieveAPIView):
    """

    """
    serializer_class = serializers.SchoolDetailsSerializer
    queryset = models.School.objects.all()
    permission_classes = [rest_permissions.AllowAny]


class SchoolsListView(generics.ListAPIView):
    """

    """
    serializer_class = serializers.SchoolListSerializer
    queryset = models.School.objects.all()
    filter_backends = (rest_filters.SearchFilter,)
    search_fields = ('name',)
    permission_classes = [rest_permissions.AllowAny]


class SchoolCreateView(generics.CreateAPIView):
    """
    School create for authorized teacher
    """
    serializer_class = serializers.SchoolCreateSerializer
    queryset = models.School.objects.all()
    permission_classes = [permissions.IsTeacher]

    def create(self, request, *args, **kwargs):
        try:
            request.data['creator'] = request.user.teacher.pk
        except models.Teacher.DoesNotExist:
            raise Http404
        else:
            super().create(request, *args, **kwargs)


class SchoolSafeUpdateView(generics.UpdateAPIView):  # TODO update rules
    """
    School safe update endpoint
    Updates existing many2many fields values with given
    For other fields sets value (default behavior)
    """
    serializer_class = serializers.TeacherSafeUpdateSerializer
    queryset = models.School.objects.all()
    permission_classes = [permissions.IsTeacher, permissions.IsSchoolCreator]

    # def get_object(self):
    #     try:
    #         return self.request.user.teacher
    #     except models.Teacher.DoesNotExist:
    #         raise Http404


class SchoolSafeRemoveView(generics.UpdateAPIView):  # TODO remove rules
    """
    School safe remove endpoint
    Removes given values from many2many fields
    """
    serializer_class = serializers.SchoolSafeRemoveSerializer
    queryset = models.School.objects.all()
    permission_classes = [permissions.IsTeacher, permissions.IsSchoolCreator]

    # def get_object(self):
    #     try:
    #         return self.request.user.teacher
    #     except models.Teacher.DoesNotExist:
    #         raise Http404


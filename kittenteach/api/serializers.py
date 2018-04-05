from django.contrib.auth.models import User
from djoser.serializers import UserCreateSerializer
from rest_framework import serializers

from kittenteach.api.validators import UserValidator
from kittenteach.core.models import Student, Teacher, Balance, Subject


class UserSerializer(serializers.ModelSerializer, UserValidator):
    class Meta:
        model = User
        fields = ('id', 'email', 'password', 'first_name', 'last_name')
        extra_kwargs = {
            'id': {'read_only': True},
            'password': {'write_only': True},
        }

    def create(self, validated_data):
        email = validated_data.pop('email')
        password = validated_data.pop('password')

        # set email and username the same
        user = User(
            email=email,
            username=email
        )
        user.set_password(password)
        user.save()
        return user


class StudentSerializer(serializers.HyperlinkedModelSerializer):
    user = UserSerializer(required=True)

    class Meta:
        model = Student
        fields = ('url', 'user')

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        new_user = UserSerializer.create(UserSerializer(), validated_data=user_data)
        student, created = Student.objects.update_or_create(user=new_user)
        return student


class TeacherSerializer(serializers.HyperlinkedModelSerializer):
    user = UserSerializer(required=True)

    class Meta:
        model = Teacher
        fields = ('url', 'user', 'students', 'subjects')

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        new_user = UserSerializer.create(UserSerializer(), validated_data=user_data)
        teacher, created = Teacher.objects.update_or_create(user=new_user)
        return teacher


class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = ('id', 'name')
        extra_kwargs = {
            'id': {'read_only': True}
        }


class BalanceSerializer(serializers.ModelSerializer):
    # student = StudentSerializer(required=True)
    # teacher = TeacherSerializer(required=True)

    class Meta:
        model = Balance
        fields = ('id', 'balance', 'student', 'teacher')
        extra_kwargs = {
            'id': {'read_only': True}
        }


class GroupSerializer(serializers.ModelSerializer):
    pass


class StudentCreateSerializer(serializers.ModelSerializer):
    user = UserCreateSerializer(required=True)

    class Meta:
        model = Student
        fields = ('user',)

    def validate(self, attrs):
        print('validate')
        print(attrs)
        # todo check unique email and etc

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        new_user = UserSerializer.create(UserSerializer(), validated_data=user_data)
        student, created = Student.objects.update_or_create(user=new_user)
        return student

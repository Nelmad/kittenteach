from django.contrib.auth.models import User
from rest_framework import serializers

from kittenteach.api.validators import UserValidator
from kittenteach.core.models import Student, Teacher


class UserSerializer(serializers.ModelSerializer, UserValidator):
    class Meta:
        model = User
        fields = ('id', 'email', 'password', 'first_name', 'last_name', 'username')
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


class TeacherSerializer(serializers.HyperlinkedModelSerializer):
    user = UserSerializer(required=True)

    class Meta:
        model = Teacher
        fields = ('url', 'user', 'subjects')

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        new_user = UserSerializer.create(UserSerializer(), validated_data=user_data)
        teacher, created = Teacher.objects.update_or_create(user=new_user)
        return teacher

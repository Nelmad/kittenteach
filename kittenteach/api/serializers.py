from django.contrib.auth import get_user_model
from rest_framework import serializers

from kittenteach.api import validators
from kittenteach.core import models

User = get_user_model()


class UserCreateSerializer(serializers.ModelSerializer, validators.UserCreateValidator):
    class Meta:
        model = User
        fields = ('email', 'password', 'first_name', 'last_name')
        extra_kwargs = {
            'password': {
                'required': True,
                'write_only': True,
                'error_messages': {
                    'required': 'Password field is required.',
                    'blank': 'Password field should not be blank.',
                }
            },
            'email': {
                'required': True,
                'error_messages': {
                    'required': 'Email field is required.',
                    'blank': 'Email field should not be blank.',
                }
            },
            'first_name': {
                'required': True,
                'error_messages': {
                    'required': 'First name field is required.',
                    'blank': 'First name field should not be blank.',
                }
            },
            'last_name': {
                'required': True,
                'error_messages': {
                    'required': 'Last name field is required.',
                    'blank': 'Last name field should not be blank.',
                }
            }
        }

    def create(self, validated_data):
        email = validated_data.pop('email', '')
        password = validated_data.pop('password')

        # set email and username the same
        user = User(email=email, username=email, **validated_data)
        user.set_password(password)
        user.save()
        return user


class StudentCreateSerializer(serializers.ModelSerializer):
    user = UserCreateSerializer(required=True, error_messages={'required': 'User field is required.'})

    class Meta:
        model = models.Student
        fields = ('user',)

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        new_user = UserCreateSerializer.create(UserCreateSerializer(), validated_data=user_data)
        student = models.Student.objects.create(user=new_user)
        return student


class TeacherCreateSerializer(serializers.ModelSerializer):
    user = UserCreateSerializer(required=True, error_messages={'required': 'User field is required.'})

    class Meta:
        model = models.Teacher
        fields = ('user',)

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        new_user = UserCreateSerializer.create(UserCreateSerializer(), validated_data=user_data)
        student = models.Teacher.objects.create(user=new_user)
        return student


class UserDetailsSerializer(serializers.ModelSerializer):
    # TODO read only
    class Meta:
        model = User
        fields = ('first_name', 'last_name')


class StudentDetailsSerializer(serializers.HyperlinkedModelSerializer):
    user = UserDetailsSerializer(read_only=True)

    class Meta:
        model = models.Student
        fields = ('url', 'user')


class TeacherDetailsSerializer(serializers.HyperlinkedModelSerializer):
    user = UserDetailsSerializer(read_only=True)

    class Meta:
        model = models.Teacher
        fields = ('url', 'user')


class StudentListSerializer(serializers.ModelSerializer):
    user = UserDetailsSerializer(read_only=True)

    class Meta:
        model = models.Student
        fields = ('user',)


class TeacherListSerializer(serializers.ModelSerializer):
    user = UserDetailsSerializer(read_only=True)

    class Meta:
        model = models.Teacher
        fields = ('user',)


# TODO specify url
# TODO pagination for lists
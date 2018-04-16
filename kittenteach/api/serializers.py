from django.contrib.auth import get_user_model
from django.utils.translation import ugettext_lazy as _
from rest_framework import serializers
from rest_framework.compat import authenticate

from kittenteach.api import validators
from kittenteach.core import models

User = get_user_model()


class AuthTokenSerializer(serializers.Serializer):
    email = serializers.EmailField(
        label=_("Email"),
        error_messages={
            'required': _('Email field is required.'),
            'blank': _('Email field should not be blank.'),
        }
    )
    password = serializers.CharField(
        label=_("Password"),
        style={'input_type': 'password'},
        trim_whitespace=False,
        error_messages={
            'required': _('Password field is required.'),
            'blank': _('Password field should not be blank.'),
        }
    )

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')

        if email and password:
            user = authenticate(request=self.context.get('request'), username=email, password=password)

            # The authenticate call simply returns None for is_active=False
            # users. (Assuming the default ModelBackend authentication backend.)
            if not user:
                msg = _('Unable to log in with provided credentials.')
                raise serializers.ValidationError(msg, code='authorization')
        else:
            msg = _('Must include "email" and "password".')
            raise serializers.ValidationError(msg, code='authorization')

        attrs['user'] = user
        return attrs

    def create(self, validated_data):
        pass

    def update(self, instance, validated_data):
        pass


class UserCreateSerializer(serializers.ModelSerializer, validators.UserCreateValidator):
    class Meta:
        model = User
        fields = ('email', 'password', 'first_name', 'last_name')
        extra_kwargs = {
            'email': {
                'required': True,
                'allow_blank': False,
                'error_messages': {
                    'required': _('Email field is required.'),
                    'blank': _('Email field should not be blank.'),
                }
            },
            'password': {
                'required': True,
                'allow_blank': False,
                'write_only': True,
                'trim_whitespace': False,
                'error_messages': {
                    'required': _('Password field is required.'),
                    'blank': _('Password field should not be blank.'),
                }
            },
            'first_name': {
                'required': True,
                'allow_blank': False,
                'error_messages': {
                    'required': _('First name field is required.'),
                    'blank': _('First name field should not be blank.'),
                }
            },
            'last_name': {
                'required': True,
                'allow_blank': False,
                'error_messages': {
                    'required': _('Last name field is required.'),
                    'blank': _('Last name field should not be blank.'),
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


class TeacherUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Teacher
        fields = ('subjects', 'students')

    # def update(self, instance, validated_data):
    #     print('SERIALIZER UPDATE')


class SubjectCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Subject
        fields = ('name',)
        extra_kwargs = {
            'name': {
                'required': True,
                'allow_blank': False,
                'error_messages': {
                    'required': _('Name field is required.'),
                    'blank': _('Name field should not be blank.'),
                }
            }
        }


class StudentItemSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(read_only=True, view_name='student-details')

    class Meta:
        model = models.Student
        fields = ('url',)


class SubjectItemSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(read_only=True, view_name='subject-details')

    class Meta:
        model = models.Subject
        fields = ('url', 'name')
        extra_kwargs = {
            'name': {'read_only': True},
        }


class TeacherItemSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(read_only=True, view_name='teacher-details')

    class Meta:
        model = models.Teacher
        fields = ('url',)


class UserDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('first_name', 'last_name')
        extra_kwargs = {
            'first_name': {'read_only': True},
            'last_name': {'read_only': True},
        }


class StudentDetailsSerializer(serializers.ModelSerializer):
    user = UserDetailsSerializer(read_only=True)
    teachers = TeacherItemSerializer(read_only=True, many=True)

    class Meta:
        model = models.Student
        fields = ('user', 'teachers')


class SubjectDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Subject
        fields = ('name', 'teachers')


class TeacherDetailsSerializer(serializers.ModelSerializer):
    user = UserDetailsSerializer(read_only=True)
    subjects = SubjectItemSerializer(read_only=True, many=True)
    students = StudentItemSerializer(read_only=True, many=True)

    class Meta:
        model = models.Teacher
        fields = ('user', 'students', 'subjects')


class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('first_name', 'last_name')
        extra_kwargs = {
            'first_name': {'read_only': True},
            'last_name': {'read_only': True},
        }


class StudentListSerializer(serializers.HyperlinkedModelSerializer):
    user = UserListSerializer(read_only=True)
    url = serializers.HyperlinkedIdentityField(read_only=True, view_name='student-details')

    class Meta:
        model = models.Student
        fields = ('url', 'user')


class TeacherListSerializer(serializers.HyperlinkedModelSerializer):
    user = UserListSerializer(read_only=True)
    url = serializers.HyperlinkedIdentityField(read_only=True, view_name='teacher-details')

    class Meta:
        model = models.Teacher
        fields = ('url', 'user')


class SubjectListSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(read_only=True, view_name='subject-details')

    class Meta:
        model = models.Subject
        fields = ('url', 'name')

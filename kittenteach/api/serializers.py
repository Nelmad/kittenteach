from django.contrib.auth import get_user_model
from django.utils.translation import ugettext_lazy as _
from rest_framework import serializers
from rest_framework.compat import authenticate
from rest_framework.serializers import raise_errors_on_nested_writes
from rest_framework.utils import model_meta

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


class SubjectCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Subject
        fields = ('name', 'creator')
        extra_kwargs = {
            'name': {
                'required': True,
                'allow_blank': False,
                'error_messages': {
                    'required': _('Name field is required.'),
                    'blank': _('Name field should not be blank.'),
                }
            },
            'creator': {
                'required': True,
                'allow_blank': False,
                'error_messages': {
                    'required': _('Creator field is required.'),
                    'blank': _('Creator field should not be blank.'),
                }
            }
        }


class TeacherGroupCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Group
        fields = ('name', 'teacher', 'subject', 'students')
        extra_kwargs = {
            'name': {
                'required': True,
                # 'allow_blank': False,
                'error_messages': {
                    'required': _('Name field is required.'),
                    'blank': _('Name field should not be blank.'),
                }
            },
            'teacher': {
                'required': True,
                # 'allow_blank': False,
                'error_messages': {
                    'required': _('Teacher field is required.'),
                    'blank': _('Teacher field should not be blank.'),
                }
            },
            'subject': {
                'required': True,
                # 'allow_blank': False,
                'error_messages': {
                    'required': _('Subject field is required.'),
                    'blank': _('Subject field should not be blank.'),
                }
            },
            'students': {
                'required': False,
                # 'allow_blank': False,
                'error_messages': {
                    'blank': _('Subject field should not be blank.'),
                }
            }
        }


class SchoolCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.School
        fields = ('name', 'address', 'creator')
        extra_kwargs = {
            'name': {
                'required': True,
                # 'allow_blank': False,
                'error_messages': {
                    'required': _('Name field is required.'),
                    'blank': _('Name field should not be blank.'),
                }
            },
            'creator': {
                'required': True,
                # 'allow_blank': False,
                'error_messages': {
                    'required': _('Creator field is required.'),
                    'blank': _('Creator field should not be blank.'),
                }
            },
            'address': {
                # 'allow_blank': False,
                'error_messages': {
                    'blank': _('Address field should not be blank.'),
                }
            }
        }


class TeacherSafeUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Teacher
        fields = ('subjects', 'students')

    def update(self, instance, validated_data):
        raise_errors_on_nested_writes('update', self, validated_data)
        info = model_meta.get_field_info(instance)

        for attr, value in validated_data.items():
            if attr in info.relations and info.relations[attr].to_many:
                field = getattr(instance, attr)
                field.add(*value)  # add values to list instead of set
            else:
                setattr(instance, attr, value)
        instance.save()

        return instance


class SchoolSafeUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.School
        fields = ('teachers',)

    def update(self, instance, validated_data):
        raise_errors_on_nested_writes('update', self, validated_data)
        info = model_meta.get_field_info(instance)

        for attr, value in validated_data.items():
            if attr in info.relations and info.relations[attr].to_many:
                field = getattr(instance, attr)
                field.add(*value)  # add values to list instead of set
            else:
                setattr(instance, attr, value)
        instance.save()

        return instance


class TeacherSafeRemoveSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Teacher
        fields = ('subjects', 'students')

    def update(self, instance, validated_data):
        raise_errors_on_nested_writes('update', self, validated_data)
        info = model_meta.get_field_info(instance)

        for attr, value in validated_data.items():
            if attr in info.relations and info.relations[attr].to_many:
                field = getattr(instance, attr)
                field.remove(*value)  # remove values to list instead of set
            # else:
            # setattr(instance, attr, value)
        instance.save()

        return instance


class SchoolSafeRemoveSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Teacher
        fields = ('teachers',)

    def update(self, instance, validated_data):
        raise_errors_on_nested_writes('update', self, validated_data)
        info = model_meta.get_field_info(instance)

        for attr, value in validated_data.items():
            if attr in info.relations and info.relations[attr].to_many:
                field = getattr(instance, attr)
                field.remove(*value)  # remove values to list instead of set
            # else:
            # setattr(instance, attr, value)
        instance.save()

        return instance


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


class TeacherGroupListSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(read_only=True, view_name='teacher-group-details')
    subject = SubjectItemSerializer(read_only=True)
    students = StudentListSerializer(read_only=True, many=True)

    class Meta:
        model = models.Group
        fields = ('url', 'name', 'subject', 'students')


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


class SchoolListSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(read_only=True, view_name='school-details')

    class Meta:
        model = models.School
        fields = ('url', 'name', 'address')


class TeacherGroupItemSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(read_only=True, view_name='teacher-group-details')

    class Meta:
        model = models.Group
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
    teachers = serializers.HyperlinkedIdentityField(read_only=True, view_name='teacher-details', many=True)

    class Meta:
        model = models.Subject
        fields = ('name', 'teachers')
        extra_kwargs = {
            'name': {'read_only': True},
        }


class TeacherDetailsSerializer(serializers.ModelSerializer):
    user = UserDetailsSerializer(read_only=True)
    subjects = SubjectItemSerializer(read_only=True, many=True)
    students = StudentItemSerializer(read_only=True, many=True)
    groups = serializers.HyperlinkedIdentityField(read_only=True, view_name='teacher-group-details', many=True)

    class Meta:
        model = models.Teacher
        fields = ('user', 'students', 'subjects', 'groups')


class TeacherGroupDetailsSerializer(serializers.ModelSerializer):
    teacher = TeacherListSerializer(read_only=True)
    subject = SubjectListSerializer(read_only=True)
    students = StudentListSerializer(read_only=True, many=True)

    class Meta:
        model = models.Group
        fields = ('name', 'teacher', 'subject', 'students')
        extra_kwargs = {
            'name': {'read_only': True}
        }


class SchoolDetailsSerializer(serializers.ModelSerializer):
    creator = TeacherListSerializer(read_only=True)

    class Meta:
        model = models.School
        fields = ('name', 'address', 'creator')
        extra_kwargs = {
            'name': {'read_only': True},
            'address': {'read_only': True},
        }


class LessonTemplateListSerializer(serializers.ModelSerializer):
    group = TeacherGroupDetailsSerializer(read_only=True)

    class Meta:
        model = models.LessonTemplate
        fields = ('group', 'weekday', 'time')
        extra_kwargs = {
            'weekday': {'read_only': True},
            'time': {'read_only': True},
        }


class LessonTemplateCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.LessonTemplate
        fields = ('group', 'weekday', 'time', 'teacher')
        extra_kwargs = {
            'group': {
                'required': True,
                # 'allow_blank': False,
                'error_messages': {
                    'required': _('Group field is required.'),
                    'blank': _('Group field should not be blank.'),
                }
            },
            'weekday': {
                'required': True,
                # 'allow_blank': False,
                'error_messages': {
                    'required': _('Weekday field is required.'),
                    'blank': _('Weekday field should not be blank.'),
                }
            },
            'time': {
                'required': True,
                # 'allow_blank': False,
                'error_messages': {
                    'required': _('Time field is required.'),
                    'blank': _('Time field should not be blank.'),
                }
            },
            'teacher': {
                'required': True,
                'error_messages': {
                    'required': _('Teacher field is required.'),
                    'blank': _('Teacher field should not be blank.'),
                }
            }
        }

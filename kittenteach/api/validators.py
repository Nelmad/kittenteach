from django.utils.translation import ugettext_lazy as _
from djoser.serializers import User
from rest_framework import serializers


class UserCreateValidator:
    def validate_email(self, value):
        normalized_email = value.lower()
        if User.objects.filter(email=normalized_email).exists():
            raise serializers.ValidationError(_("Email field must be unique."), code='unique')
        return normalized_email

    def validate_first_name(self, value):
        if not value:
            raise serializers.ValidationError(_("First name field must not be empty"))
        return value

    def validate_last_name(self, value):
        if not value:
            raise serializers.ValidationError(_("Last name field must not be empty"))
        return value

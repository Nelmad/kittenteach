from django.utils.translation import ugettext_lazy as _
from djoser.serializers import User
from rest_framework import serializers


class UserValidator:
    def validate_email(self, value):
        normalized_email = value.lower()
        if User.objects.filter(email=normalized_email).exists():
            raise serializers.ValidationError(_("Email field must be unique."), code='unique')
        return normalized_email

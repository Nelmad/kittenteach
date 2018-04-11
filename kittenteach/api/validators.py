from django.contrib.auth import get_user_model
from django.utils.translation import ugettext_lazy as _
from rest_framework import serializers

User = get_user_model()


class UserCreateValidator:
    def validate_email(self, value):
        if not value:
            raise serializers.ValidationError(_("Email field should not be blank."), code='blank')
        normalized_email = value.lower()
        if User.objects.filter(email=normalized_email).exists():
            raise serializers.ValidationError(_("Email field must be unique."), code='not_unique')
        return normalized_email

    def validate_first_name(self, value):
        if not value:
            raise serializers.ValidationError(_("First name field should not be blank."), code='blank')
        return str(value)

    def validate_last_name(self, value):
        if not value:
            raise serializers.ValidationError(_("Last name field should not be blank."), code='blank')
        return str(value)

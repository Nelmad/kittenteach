from rest_framework import permissions

from kittenteach.core import models


class IsTeacher(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    """

    def has_permission(self, request, view):
        try:
            teacher = request.user.teacher
        except (AttributeError, models.Teacher.DoesNotExist):
            return False
        else:
            return True


class IsStudent(permissions.BasePermission):
    def has_permission(self, request, view):
        try:
            student = request.user.student
        except (AttributeError, models.Student.DoesNotExist):
            return False
        else:
            return True


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Object-level permission to only allow owners of an object to edit it.
    Assumes the model instance has an `owner` attribute.
    """

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        # Instance must have an attribute named `owner`.
        return obj.owner == request.user
from django_filters.rest_framework import FilterSet, CharFilter

from kittenteach.core import models


# TODO filter for nested
class TeacherFilterSet(FilterSet):
    subject = CharFilter(name='subjects__name')

    class Meta:
        model = models.Teacher
        fields = ('subject',)

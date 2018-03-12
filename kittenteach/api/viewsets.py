from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet


class ProfileViewSet(mixins.CreateModelMixin,
                     mixins.RetrieveModelMixin,
                     mixins.UpdateModelMixin,
                     mixins.ListModelMixin,
                     GenericViewSet):
    """
    A viewset that provides default `create()`, `retrieve()`, `update()`,
    `partial_update()` and `list()` actions.
    """
    pass


class HistoryViewSet(mixins.CreateModelMixin,
                     mixins.RetrieveModelMixin,
                     mixins.ListModelMixin,
                     GenericViewSet):
    """
    A viewset that provides default `create()`, `retrieve()` and `list()` actions.
    """
    pass

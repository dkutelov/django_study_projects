from rest_framework import generics
from rest_framework.exceptions import MethodNotAllowed

from .models import Appointment
from .permissions import AppointmentPermission, IsOwnerOrReadOnly
from .serializers import AppointmentSerializer, AppointmentCreateSerializer
from rest_framework.permissions import IsAuthenticated


class MethodSerializerView(object):
    """
    Utility class for get different serializer class by method.
    For example:
    method_serializer_classes = {
        ('GET', ): MyModelListViewSerializer,
        ('PUT', 'PATCH'): MyModelCreateUpdateSerializer
    }
    """
    method_serializer_classes = None

    def get_serializer_class(self):
        assert self.method_serializer_classes is not None, (
            'Expected view %s should contain method_serializer_classes '
            'to get right serializer class.' %
            (self.__class__.__name__, )
        )
        for methods, serializer_cls in self.method_serializer_classes.items():
            if self.request.method in methods:
                return serializer_cls

        raise MethodNotAllowed(self.request.method)


class AppointmentList(MethodSerializerView, generics.ListCreateAPIView):
    queryset = Appointment.objects.all()

    method_serializer_classes = {
        ('GET',): AppointmentSerializer,
        ('POST',): AppointmentCreateSerializer
    }

    permission_classes = [IsAuthenticated, AppointmentPermission]  # all should be True to pass


class AppointmentDetail(MethodSerializerView, generics.RetrieveUpdateDestroyAPIView):
    queryset = Appointment.objects.all()

    method_serializer_classes = {
        ('GET',): AppointmentSerializer,
        ('PUT', 'PATCH'): AppointmentCreateSerializer,

    }

    permission_classes = [IsAuthenticated, AppointmentPermission, IsOwnerOrReadOnly]

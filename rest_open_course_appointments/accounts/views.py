from rest_framework import generics, response, status
from rest_framework.permissions import IsAuthenticated

from accounts.models import Doctor, Contact
from accounts.permissions import DoctorPermission
from accounts.serializers import DoctorSerializer, ContactSerializer
from accounts.tasks import email_to_customer, email_to_admin
from rest_open_course_appointments import settings


class DoctorList(generics.ListAPIView):
    # queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    permission_classes = [IsAuthenticated, DoctorPermission]

    # def list(self, request, *args, **kwargs):
    #     specialty = self.request.query_params.get('specialty', None)
    #     if specialty:
    #         queryset = Doctor.objects.all().filter(specialty=specialty)
    #     else:
    #         queryset = Doctor.objects.all()
    #
    #     page = self.paginate_queryset(queryset)
    #     if page is not None:
    #         serializer = self.get_serializer(page, many=True)
    #         return self.get_paginated_response(serializer.data)
    #
    #     serializer = self.get_serializer(queryset, many=True)
    #     return Response(serializer.data)

    # or
    def get_queryset(self):
        specialty = self.request.query_params.get('specialty', None)

        if specialty is not None:
            queryset = Doctor.objects.filter(specialty=specialty)
            return queryset

        queryset = Doctor.objects.all()
        return queryset


class ContactForm(generics.CreateAPIView):
    queryset = Contact
    serializer_class = ContactSerializer

    def post(self, request, *args, **kwargs):
        print(settings.EMAIL_HOST_USER)
        print(settings.EMAIL_HOST_PASSWORD)
        serializer = ContactSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        email_to_customer.delay(self.request.user.username, request.data['email'])
        email_to_admin.delay(request.data['email'], request.data['content'])
        return response.Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    permission_classes = [IsAuthenticated,]



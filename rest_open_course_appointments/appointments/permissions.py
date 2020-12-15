from rest_framework.permissions import BasePermission, SAFE_METHODS

from accounts.models import Patient


class AppointmentPermission(BasePermission):
    """
        Allows only patients to create appointments
    """
    def has_permission(self, request, view):
        # check if user is patient (not doctor
        if request.method == 'GET':
            return True
        # import pdb; pdb.set_trace()
        patient = Patient.objects.filter(user__pk=request.user.id).exists()

        if patient or (request.user.is_superuser and not request.method == 'POST'):
            return True
        return False


class IsOwnerOrReadOnly(BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS or request.user.is_superuser:
            return True
        return obj.patient.user == request.user and obj.status == 'P'

from django.contrib import admin

from .models import Appointment, Cardboard, Visitation

admin.site.register(Appointment)
admin.site.register(Cardboard)
admin.site.register(Visitation)

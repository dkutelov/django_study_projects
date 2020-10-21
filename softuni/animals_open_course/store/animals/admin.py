from django.contrib import admin

from animals.models import Animal, Owner

admin.site.register(Animal)
admin.site.register(Owner)

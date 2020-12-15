from django.db import models
from django.contrib.auth.models import User
from django.core import validators
from . enums import SpecialtyEnum, GenderEnum


class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.PositiveIntegerField(validators=[validators.MinValueValidator(25)])
    specialty = models.CharField(max_length=10, choices=[(s.name, s.value) for s in SpecialtyEnum])

    def __str__(self):
        return f'Doctor {self.user} with age {self.age} and sepcialty {self.specialty}'


class Patient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.PositiveIntegerField(validators=[validators.MinValueValidator(23)])
    gender = models.CharField(max_length=8, choices=[(g.name, g.value) for g in GenderEnum])

    def __str__(self):
        return f'{self.user}'


class Contact(models.Model):
    email = models.EmailField()
    content = models.TextField()


from django.db import models
from .validators import pages_validator


class Book(models.Model):
    title = models.CharField(max_length=20)
    pages = models.IntegerField(default=0, validators=[pages_validator])
    description = models.TextField(max_length=100, default='')
    author = models.CharField(max_length=20)


from django.db import models


class Profile(models.Model):
    first_name = models.CharField(max_length=15, blank=False)
    last_name = models.CharField(max_length=15, blank=False)
    budget = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f'{self.first_name} {self.last_name} - budget at {self.budget}'


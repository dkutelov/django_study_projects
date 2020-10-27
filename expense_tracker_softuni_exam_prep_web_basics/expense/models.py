from django.db import models
from user_profile.models import Profile


class Expense(models.Model):
    title = models.CharField(max_length=50, blank=False)
    image_url = models.URLField(max_length=200)
    description = models.TextField()
    price = models.FloatField(blank=False)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.title} - {self.price} - {self.description}'


from django.db import models

from accounts.models import UserProfile


class Pet(models.Model):
    DOG = 'dog'
    CAT = 'cat'
    PARROT = 'parrot'
    UNKNOWN = 'unknown'
    PET_TYPES = (
        (DOG, 'dog'),
        (CAT, 'cat'),
        (PARROT, 'parrot'),
        (UNKNOWN, 'unknown'),
    )

    type = models.CharField(max_length=7, choices=PET_TYPES, default=UNKNOWN)
    name = models.CharField(max_length=6, blank=False)  # should not be empty
    age = models.PositiveIntegerField(blank=False)
    description = models.TextField()
    image_url = models.URLField(blank=False)
    image = models.ImageField(upload_to="pet")
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name} {self.age} {self.type}'


class Like(models.Model):
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
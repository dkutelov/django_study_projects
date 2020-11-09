from django.db import models

from recipe.validators import validate_list_separated_by_comma_and_space


class Recipe(models.Model):
    title = models.CharField(max_length=30)
    image_url = models.URLField()
    description = models.TextField()
    ingredients = models.CharField(
        max_length=250,
        validators=(validate_list_separated_by_comma_and_space,)
    )
    time = models.IntegerField()

    def __str__(self):
        return f'{self.title}'

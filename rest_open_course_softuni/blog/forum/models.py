from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.IntegerField()


class Question(models.Model):
    author = models.CharField(max_length=200, default="Anonumous")
    question = models.TextField()
    user = models.ForeignKey(Profile, on_delete=models.CASCADE,null=True, blank=True, related_name='questions')

    def __str__(self):
        return f'{self.author} {self.question}'


class Answer(models.Model):
    author = models.CharField(max_length=200, default="Anonumous")
    content = models.TextField()
    likes = models.PositiveIntegerField(default=0)
    dislikes = models.PositiveIntegerField(default=0)
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answers')

    def __str__(self):
        return f'{self.content[:10]}... {self.author}'



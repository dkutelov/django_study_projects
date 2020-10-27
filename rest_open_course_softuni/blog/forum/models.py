from django.db import models


class Question(models.Model):
    author = models.CharField(max_length=200, default="Anonumous")
    question = models.TextField()

    def __str__(self):
        return f'{self.author} {self.question}'


class Answer(models.Model):
    author = models.CharField(max_length=200, default="Anonumous")
    content = models.TextField()
    likes = models.PositiveIntegerField(default=0)
    dislikes = models.PositiveIntegerField(default=0)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.content[:10]}... {self.author}'
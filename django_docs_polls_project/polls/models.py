from django.db import models
import datetime
from django.utils import timezone


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

    def __str__(self):
        return self.question_text


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text


class ScaleChoice(models.Model):
    SCORE_TYPES = (
        (1, 'max_agree'),
        (2, 'med_agree'),
        (3, 'min_agree'),
        (4, 'neutral'),
        (5, 'min_disagree'),
        (6, 'med_disagree'),
        (7, 'max_disagree'),
    )
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_score = models.IntegerField(choices=SCORE_TYPES, blank=None)

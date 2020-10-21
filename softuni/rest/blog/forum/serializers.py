from rest_framework import serializers
from .models import Question


# Serializers define the API representation
class QuestionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Question
        fields = ['author', 'question']
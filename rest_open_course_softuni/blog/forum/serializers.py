from rest_framework import serializers
from .models import Question


# Serializers define the API representation
class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ('id', 'author', 'question')

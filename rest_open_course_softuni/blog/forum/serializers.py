from rest_framework import serializers
from .models import Question, Answer, Profile


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ('id', 'author', 'content', 'likes', 'dislikes')


# Serializers define the API representation
class QuestionSerializer(serializers.ModelSerializer):
    answers = AnswerSerializer(many=True, read_only=True)

    class Meta:
        model = Question
        fields = ('id', 'author', 'question', 'answers')  # answer is the related name form the model


class ProfileSerializer(serializers.ModelSerializer):
    questions = QuestionSerializer(many=True, read_only=True)

    class Meta:
        model = Profile
        fields = ('id', 'user', 'phone_number', 'questions')


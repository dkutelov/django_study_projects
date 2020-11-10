from rest_framework import routers, serializers, viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404

from .models import Question, Answer, Profile
from .serializers import QuestionSerializer, AnswerSerializer, ProfileSerializer


# ViewSets define the view behavior
# class QuestionViewSet(viewsets.ModelViewSet):
#     queryset = Question.objects.all()
#     serializer_class = QuestionSerializer


class QuestionList(APIView):
    @staticmethod
    def get(request):
        questions = Question.objects.all()
        serializer = QuestionSerializer(questions, many=True)
        return Response(serializer.data)  # serializer.errors

    @staticmethod
    def post(request):
        serializer = QuestionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class QuestionDetails(APIView):
    @staticmethod
    def get_object(pk):
        try:
            question = Question.objects.get(pk=pk)
            return question
        except Question.DoesNotExist:
            raise Http404

    def get(self, request, question_id):
        question = self.get_object(question_id)
        serializer = QuestionSerializer(question)
        return Response(serializer.data)

    def put(self, request, question_id):
        question = self.get_object(question_id)
        serializer = QuestionSerializer(question, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, question_id):
        question = self.get_object(question_id)
        question.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class AnswerDetails(APIView):
    @staticmethod
    def get_object(pk):
        try:
            question = Answer.objects.get(pk=pk)
            return question
        except Answer.DoesNotExist:
            raise Http404

    def get(self, request, question_id, answer_id):
        answer = self.get_object(answer_id)
        serializer = AnswerSerializer(answer)
        return Response(serializer.data)


class UserList(APIView):

    def get(self, request):
        profiles = Profile.objects.all()
        serializer = ProfileSerializer(profiles, many=True)
        return Response(serializer.data)
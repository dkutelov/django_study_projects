from rest_framework import routers, serializers, viewsets
from .models import Question
from .serializers import QuestionSerializer


# ViewSets define the view behavior
class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


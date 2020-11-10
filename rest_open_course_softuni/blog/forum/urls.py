from django.urls import path, include
from rest_framework import routers
from . import views

# urlpatterns = [
#     re_path('^questions/$', views.QuestionViewSet, name="questions"),
# ]

# router = routers.DefaultRouter()
# router.register(r'questions', views.QuestionList.as_view())

urlpatterns = [
    # path('', include(router.urls)),
    path('questions/', views.QuestionList.as_view(), name="quesitons"),
    path('questions/<int:question_id>/', views.QuestionDetails.as_view(), name="question-details"),
    path('questions/<int:question_id>/answers/<int:answer_id>/', views.AnswerDetails.as_view(), name="qanswer-details"),
    path('users/questions/', views.UserList.as_view(), name='question-details')

    # path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
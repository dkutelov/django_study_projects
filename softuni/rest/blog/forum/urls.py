from django.urls import path, include
from rest_framework import routers
from . import views

# urlpatterns = [
#     re_path('^questions/$', views.QuestionViewSet, name="questions"),
# ]

router = routers.DefaultRouter()
router.register(r'questions', views.QuestionViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
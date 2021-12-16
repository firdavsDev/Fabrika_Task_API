from django.db import router
from django.urls import path,include
from rest_framework.routers import DefaultRouter, SimpleRouter
from . import views
app_name = 'polls'

router = DefaultRouter()
router.register('polls',views.PollsViewSet, basename='poll')
router.register('questions',views.QuestionsViewSet, basename='question')
router.register('choices',views.ChoiceViewSet, basename='choice')
router.register('replies',views.ReplyViewSet, basename='reply')

urlpatterns = router.urls
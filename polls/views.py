# file imports
from .models import Question, Choice, Poll, Reply
from .serializers import ChoiceSerializer, ReplySerializer, QuestionSerializer, PollSerializer,MyToken
#rest
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
#jwt
from rest_framework_simplejwt.views import TokenObtainPairView

#Loggin class
class MYTokenAPI(TokenObtainPairView):
    permission_classes = (AllowAny,)
    serializer_class = MyToken

# Poll viewset
class PollsViewSet(viewsets.ModelViewSet):
    serializer_class = PollSerializer
    queryset = Poll.objects.all()
    permission_classes = [IsAuthenticated,IsAdminUser]
    
#Question viewset
class QuestionsViewSet(viewsets.ModelViewSet):
    serializer_class = QuestionSerializer
    queryset = Question.objects.all()
    permission_classes = [IsAuthenticated,IsAdminUser]
    
# Choice viewset
class ChoiceViewSet(viewsets.ModelViewSet):
    serializer_class = ChoiceSerializer
    queryset = Choice.objects.all()
    permission_classes = [IsAuthenticated,IsAdminUser]
    

# Reply viewset
class ReplyViewSet(viewsets.ModelViewSet):
    serializer_class = ReplySerializer
    queryset = Reply.objects.all()
    permission_classes = [IsAuthenticated]


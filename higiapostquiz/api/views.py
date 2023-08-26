from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny
from eventos.api.serializers import ContentCategorySerializer, PostSerializer, QuestionSerializer

from eventos.models import ContentCategory, Post, Question

class ContentCategoryViewSet(ModelViewSet):
    permission_classes = [AllowAny]
    queryset = ContentCategory.objects.all()
    serializer_class = ContentCategorySerializer

class PostViewSet(ModelViewSet):
    permission_classes = [AllowAny]
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class QuestionViewSet(ModelViewSet):
    permission_classes = [AllowAny]
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
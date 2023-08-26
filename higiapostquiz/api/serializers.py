from rest_framework.serializers import ModelSerializer

from eventos.models import ContentCategory, Post, Question

class ContentCategorySerializer(ModelSerializer):
    class Meta:
        model = ContentCategory
        fields = ['id','name', 'type', 'enabled']

class PostSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'title', 'subtitle', 'description', 'urlWeb', 'category']

class QuestionSerializer(ModelSerializer):

    class Meta:
        model = Question
        fields = ['id', 'question', 'alternatives', 'explanation', 'correctIndex', 'category']

from django.db import models


# Create your models here.
class ContentCategory(models.Model):
    name = models.CharField(max_length=150)
    type = models.CharField(max_length=150) 
    enabled = models.BooleanField()

class Post(models.Model):
    title = models.CharField(max_length=150)
    subtitle = models.CharField(max_length=150)
    description = models.CharField(max_length=150)
    urlweb = models.CharField(max_length=500)
    category = models.ForeignKey(ContentCategory, on_delete=models.CASCADE)

class Question(models.Model):
    question = models.CharField(max_length=150)
    alternatives = models.JSONField()
    explanation = models.CharField(max_length=150)
    correctIndex = models.IntegerField()
    category = models.ForeignKey(ContentCategory, on_delete=models.CASCADE)
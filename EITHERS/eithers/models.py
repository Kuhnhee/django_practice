from django.db import models

# Create your models here.
class Question(models.Model):
    title = models.CharField(max_length=30)
    issue_a = models.CharField(max_length=30)
    issue_b = models.CharField(max_length=30)
    image_a = models.ImageField(blank=True)
    image_b = models.ImageField(blank=True)

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    pick = models.IntegerField()
    comment = models.TextField()

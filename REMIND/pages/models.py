from django.db import models

# Create your models here.
class Page(models.Model):
    title = models.CharField(max_length=100)
    contents = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
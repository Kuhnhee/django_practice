from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.TextField()
    content = models.TextField()

    def __str__(self):
        return f'제목:{self.title} | 내용:{self.content}'
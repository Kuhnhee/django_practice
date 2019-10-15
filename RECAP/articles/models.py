from django.db import models
from django.urls import reverse

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta: # subclass for ordering
        ordering = ['-pk'] # reversed ordering based on pk
        # ordering = ('-pk',) # tuple로 쓰는 방법

    # method도 추가 예정
    def get_absolute_url(self):
        # 첫번째 인자 : 어느 view method로 갈 건지 # 두번째 인자 : pk
        return reverse('articles:detail', kwargs={'article_pk' : self.pk}) 
        # reverse는 django.urls에 있다.



## Comment class added 
class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    content = models.TextField()
from django.db import models

# Create your models here.
class Article(models.Model):
    #각각의 컬럼들이 어떤 값을 가지는지를 상세하게 알려준다.
    title = models.TextField() #제목
    content = models.TextField() #내용
    created_at = models.DateTimeField(auto_now_add=True) #작성시간
    image_url = models.TextField()

    def __str__(self):
        return f'{self.id} | {self.title}'

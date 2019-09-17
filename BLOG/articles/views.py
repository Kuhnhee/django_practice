from django.shortcuts import render, redirect
from datetime import datetime
from .models import Article

# blogs = []

# class Article:
#     def __init__(self, title, content, created_at):
#         self.title = title
#         self.content = content
#         self.created_at = created_at

#     def __str__(self):
#         return f'제목:{self.title} 내용:{self.content} 작성시간:{self.created_at}'

# Create your views here.
def new(requests):
    return render(requests,'new.html')

def create(requests):
    title = requests.GET.get('title')
    content = requests.GET.get('content')
    image_url = requests.GET.get('image_url')

    #DB에 저장하기
    article = Article()
    article.title = title
    article.content = content
    article.image_url = image_url
    article.save()

    # context = {
    #     'title': title,
    #     'content': content,
    #     'img_url': img_url,
    #     'created_at': article.created_at
    # }

    return redirect('index')

def index(requests):
    
    articles = Article.objects.all()

    context = {
        'articles': reversed(articles),
    }
    return render(requests, 'index.html', context)
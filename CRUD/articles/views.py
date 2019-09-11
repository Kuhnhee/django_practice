from django.shortcuts import render, redirect
from .models import Article

# Create your views here.
def new(request):

    return render(request, 'new.html')

def create(request):
    title = request.GET.get('title')
    content = request.GET.get('content')
    article = Article()
    article.title = title
    article.content = content
    article.save()

    return redirect('index')

def index(request):

    #show all
    articles = Article.objects.all()

    context = {
        'articles': reversed(articles),
    }

    return render(request, 'index.html', context)


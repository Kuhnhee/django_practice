from django.shortcuts import render, redirect
from .models import Page

# Create your views here.

def index(request):
    pages = Page.objects.all()
    context = {
        'pages' : pages,
    }

    return render(request, 'pages/index.html', context)

def new(request):
    return render(request, 'pages/new.html')

def create(request):
    page = Page(
        title = request.GET.get('title'),
        contents = request.GET.get('contents'),
    )
    page.save()

    return  redirect('pages:detail', page.pk)

def detail(request, pk):
    page = Page.objects.get(id=pk)

    context = {
        'page' : page
    }
    return render(request, 'pages/detail.html', context)
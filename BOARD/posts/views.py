from django.shortcuts import render, redirect
from .models import Post

# Create your views here.
def index(request):
    #table 형태로 게시판을 보여줌
    posts = Post.objects.all()

    context = {
        'posts': posts
    }

    return render(request, 'posts/index.html', context)


def new(request):
    return render(request, 'posts/new.html')


def create(request):
    #new에서 날아온 데이터로 DB에 저장한다.
    post = Post(
        title = request.GET.get('title'),
        content = request.GET.get('content'),
        image_url = request.GET.get('image_url'),
    )
    post.save()
    '''
    Post.objects.create(
        title = request.GET.get('title')
        content = request.GET.get('content')
        image_url = request.GET.get('image_url')
    )
    '''
    '''
    Post.objects.create(**request.GET)
    '''
    return redirect('home')

def detail(request, pk):
    #pk라는 id를 가진 글을 찾아와 보여줌
    post = Post.objects.get(id=pk) #(pk=pk) 또한 가능
    context = {
        'post' : post
    }
    return render(request, 'posts/detail.html', context)


def delete(request, pk):
    # pk라는 id를 가진 글을 삭제한다.
    post = Post.objects.get(pk=pk)
    post.delete()

    return redirect('home')
    

def edit(request, pk):
    # pk라는 id를 가진 글을 편집하게 함
    # 1. pk라는 id를 가진 글을 찾음
    post = Post.objects.get(pk=pk)

    context = {
        'post': post,
    }

    return render(request, 'posts/edit.html', context)


def update(request, pk):
    # 1. pk라는 id를 가진 글을 찾아서,
    # 2. /edit/으로부터 날아온 데이터를 적용하여 변경함

    post = Post.objects.get(pk=pk)
    
    post.title = request.GET.get('title')
    post.content = request.GET.get('content')
    post.image_url = request.GET.get('image_url')
    #updated_at은 자동으로 update됨
    post.save()

    # return redirect(f'/posts/{pk}/')
    return redirect('posts:detail', pk)
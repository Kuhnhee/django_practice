from django.shortcuts import render, redirect, get_object_or_404
from .models import Article, Comment
from .forms import ArticleForm, CommentForm

from IPython import embed #디버깅 용도. interative shell 튀어나온다
from django.http import Http404, HttpResponse

from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    # embed()
    visits_num = request.session.get('visits', 0) #key, value를 세션에 직접 기록
    request.session['visits'] = visits_num + 1
    request.session.modified = True
    # embed()
    articles = Article.objects.all() # Article 모델 내의 모든 data를 가져옴
    context = {
        'articles': articles,
        'visits': visits_num
    }
    return render(request, 'articles/index.html', context) # 어떤 templates를 불러올 것인지


def detail(request, article_pk):
    # article = Article.objects.get(pk=article_pk)
    article = get_object_or_404(Article, pk=article_pk)
    comments = article.comment_set.all()

    #만약에 Article.objects.get(pk=article_pk)에서 에러가 튀어 나오면, 핸들링 해주는 것
    # article = get_object_or_404()는 아래와 같이 동작한다.
    '''
    try:
        article = Article.objects.get(pk=article_pk)
    except Article.DoesNotExist:
        raise Http404('해당하는 id의 글이 존재하지 않습니다.') #404 에러 객체
    '''
    form = CommentForm()
    context = {
        'article': article,
        'form': form,
        'comments': comments,
    }
    return render(request, 'articles/detail.html', context)

# Form class version
# def create(request):
#     if request.method == "POST":
#         form = ArticleForm(request.POST) # 이렇게 맡겨버리면 된다.
#         # embed()
#         # 전송된 데이터가 유효한 값인지 검사 
#         # 유효성 검사 하지 않는다면 form.save() 하면 끝이지만
#         # 최대한 form의 기능을 쓰기 위해선 다음 같이 해야 한다.
#         if form.is_valid():
#             title = form.cleaned_data.get('title')
#             content = form.cleaned_data.get('content')
#             article = Article.objects.create(title=title, content=content)
#             return redirect(article) # get_absolute_url을 지정하면 해당 객체만 넣어도 redirect가 된다.
#         else: # 유효하지 않다면
#             return redirect('articles:create')

#     else:
#         form = ArticleForm()
#         context = {
#             'form': form,
#         }
#         return render(request, 'articles/create.html', context)

# ModelForm version
@login_required
def create(request):
    # if not request.user.is_authenticated:
    #     return redirect("accounts:login")

    if request.method == "POST":
        form = ArticleForm(request.POST) # 이렇게 맡겨버리면 된다.

        if form.is_valid():
            '''
            title = form.cleaned_data.get('title')
            content = form.cleaned_data.get('content')
            article = Article.objects.create(title=title, content=content)
            '''
            article = form.save(commit=False)
            article.user = request.user
            article.save()
            return redirect(article) # get_absolute_url을 지정하면 해당 객체만 넣어도 redirect가 된다.
        else: # 유효하지 않다면
            return redirect('articles:create')

    else:
        #입력하기 전 기본 창을 출력
        form = ArticleForm()
        context = {
            'form': form,
        }
        return render(request, 'articles/create.html', context)


########################## 10/15 added ############################

# UPDATE -> articles/:id/update | (PUT) articles/:id

# # Form Class version
# def update(request, article_pk):
#     article = get_object_or_404(Article, pk=article_pk)
#     if request.method == 'POST':
#         form = ArticleForm(request.POST)

#         if form.is_valid():
#             article.title = form.cleaned_data.get('title')
#             article.content = form.cleaned_data.get('content')
#             article.save()
#             return redirect(article)

#     #bootstrap form을 사용해 render함. 이 때, 초기값(initial)을 설정해 줄 수 있다.
#     #기존에 있던 데이터들을 그대로 보여줘야 함. form 객체에 article 객체의 값들을 넘김
#     # form.is_valid()가 false인 경우도 여기로 오게 된다.
#     form = ArticleForm(initial={
#         'title': article.title,
#         'content': article.content,
#         })
#     context = {
#         'form': form,
#         'article': article,
#     }
#     return render(request, 'articles/update.html', context)


# ModelForm version
@login_required
def update(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)

    if article.user != request.user:
        return redirect('articles:index')

    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=article)

        if form.is_valid():
            form.save()
            return redirect(article)

    #bootstrap form을 사용해 render함. 이 때, 초기값(initial)을 설정해 줄 수 있다.
    #기존에 있던 데이터들을 그대로 보여줘야 함. form 객체에 article 객체의 값들을 넘김
    # form.is_valid()가 false인 경우도 여기로 오게 된다.

    #편집 화면
    form = ArticleForm(instance=article)
    context = {
        'form': form,
        'article': article,
    }
    return render(request, 'articles/update.html', context)


# DELETE -> articles/:id/delete
@login_required
@require_POST
def delete(request, article_pk):
    if request.user.is_authenticated:

        # 요청이 POST로 들어올 때만 삭제한다. GET일 경우에도 삭제하면, url을 아는 누군가에 의해 함부로 삭제될 수 있어
        article = get_object_or_404(Article, pk=article_pk)

        if article.user != request.user:
            return redirect('articles:index')

        if request.method == 'POST':
            article.delete()
            return redirect('articles:index')
        else:
            return redirect(article)

    return HttpResponse('승인되지 않았습니다.', status=401)


@require_POST
@login_required
def commentCreate(request, article_pk):

    article = get_object_or_404(Article, pk=article_pk)

    form = CommentForm(request.POST)

    if form.is_valid():
        comment = form.save(commit=False)
        comment.user = request.user
        comment.article = article
        comment = form.save()
    return redirect(article)

@login_required
@require_POST
def commentDelete(request, article_pk, comment_id):
    
    article = get_object_or_404(Article, pk=article_pk)
    comment = get_object_or_404(Comment, pk=comment_id)
    comment.delete()

    return redirect(article)


def send_cookie(request):
    # 우리가 해본 리턴 종류들
    # return render() -> html 페이지를 만들어 주는 것
    # return redirect()
    # return reverse()
    # return HttpResponse()

    res = HttpResponse('과자 받아라')
    res.set_cookie('mycookie', 'oreo') #key, value 구조로 되어있다.
    return res


def like(request, article_pk):
    # article_pk로 넘어온 글의 like_users에 현재 접속중인 유저를 추가한다.
    # request.user.like_articles.add(Article.objects.get(pk=article_pk))
    article = Article.objects.get(pk=article_pk)
    article.like_users.add(request.user) # request.user.like_articles.add(article) 과 동일한 작업 수행
    return redirect(article)


def like_cancel(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    article.like_users.remove(request.user)
    return redirect(article)
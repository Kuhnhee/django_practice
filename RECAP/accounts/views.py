from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from IPython import embed

from django.views.decorators.http import require_POST
from .forms import CustomUserChangeForm, CustomUserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash

from django.contrib.auth import get_user_model

# Create your views here.
def signup(request):
    #만약 로그인 되어있으면, articles/로 리다이렉트
    if request.user.is_authenticated:
        return redirect('articles:index')

    if request.method == 'POST':
        #실제 DB에 유저 정보 저장

        #검증하자
        form = CustomUserCreationForm(request.POST)
        # embed()
        if form.is_valid():
            form.save()
            return redirect('articles:index') #index 페이지로 리다이렉트
    else:
        form = CustomUserCreationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/auth_form.html', context)


def login(request):
    #만약 로그인 되어있으면, articles/로 리다이렉트
    if request.user.is_authenticated:
        return redirect('articles:index')

    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST) # 쿠키, 세션ID, 브라우저 정보 등이 필요해서 request 전체를 전달함
        if form.is_valid():
            #form이 valid하면, 로그인 시킨다.
            auth_login(request, form.get_user()) #get_user(): 해당 유저정보를 가져와라
            return redirect(request.GET.get('next') or 'articles:index') # 'next' 핸들링

    else:
        form = AuthenticationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/auth_form.html', context)


def logout(request):
    # 세션을 지우기
    auth_logout(request)
    return redirect('articles:index')


@require_POST
def delete(request):
    # DB에서 user를 삭제한다.
    request.user.delete()
    return redirect('articles:index')


@login_required
def update(request):
    # 회원정보 수정 로직
    if request.method == 'POST':
        # 실제 DB에 적용
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('articles:index')
    else:
        # 편집 화면 보여줌
        form = CustomUserChangeForm(instance=request.user) # user의 정보를 가져와라!

    context = {
        'form': form,
    }
    return render(request, 'accounts/auth_form.html', context)


@login_required
def change_password(request):
    if request.method == 'POST':
        #실제 비번 변경
        # UserChangeForm과 파라미터 순서 다름 주의
        form = PasswordChangeForm(request.user, request.POST) 
        if form.is_valid():
            form.save()
            # session auth hash가 변경됨. 반영해주자!
            update_session_auth_hash(request, form.user)
            return redirect('articles:index')
    else:
        # 편집 화면 보여줌(form)
        form = PasswordChangeForm(request.user) # user의 정보를 가져와라!

    context = {
        'form': form,
    }
    return render(request, 'accounts/auth_form.html', context)


def profile(request, username):
    # DB에서 유저를 뒤져본다.
    person = get_object_or_404(get_user_model(), username=username)
    context = {
        'person': person,
    }
    return render(request, 'accounts/profile.html', context)


def follow(request, person_pk):
    person = get_object_or_404(get_user_model(), pk=person_pk)
    user = request.user

    if person.followers.filter(pk=user.pk).exists():
        person.followers.remove(user)
    else:
        person.followers.add(user) # person의 follower로 user를 추가한다.
    return redirect('profile', person.username)


from django.shortcuts import render, redirect
from .models import Question, Answer
import random as ran

# Create your views here.
def index(request):
    questions = Question.objects.all()
    context = {
        'questions': questions,
    }
    return render(request, 'eithers/index.html', context)

def new(request):
    if request.method == 'POST':
        Question.objects.create(
            title = request.POST.get('title'),
            issue_a = request.POST.get('issue_a'),
            issue_b = request.POST.get('issue_b'),
            image_a = request.FILES.get('image_a'),
            image_b = request.FILES.get('image_b')
        )
        return redirect('eithers:index')
    else:
        return render(request, 'eithers/new.html')


def detail(request, pk):
    # pk라는 id를 가진 글을 찾아와 보여줌
    question = Question.objects.get(pk=pk)

    # 해당 글에 달려있는 모든 댓글을 보여줌
    answers = question.answer_set.all()

    # 선택지
    choices = {
        0: question.issue_a, 
        1: question.issue_b,
    }

    context = {
        'question': question,
        'answers': answers,
        'choices': choices,
    }
    return render(request, 'eithers/detail.html', context)

def answers_create(request, pk):
    if request.method == 'POST':
        Answer.objects.create(
            question = Question.objects.get(pk=pk),
            comment = request.POST.get('comment'),
            pick = request.POST.get('gridRadios')
        )
        return redirect('eithers:detail', pk)
    else:
        return render(request, 'eithers/index.html')


def answers_delete(request, pk):
    question = Question.objects.get(pk=pk)
    answers = question.answer_set.all()
    answers.delete()

    return redirect('eithers:detail', pk)

def random(request):
    questions = Question.objects.all()
    pk = ran.choice(questions).id

    return redirect('eithers:detail', pk)

def clean(request):
    #모든 질문 삭제
    Question.objects.all().delete()
    return redirect('eithers:index')
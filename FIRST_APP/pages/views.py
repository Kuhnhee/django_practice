from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.

def index(request):
    #flask : return render_template('index.html')
    return render(request, 'index.html')

def home(request):
    name = '강동주'
    data = ['강동주', '김지수', '정의진']
    empty_data = ["엄복동","클레멘타인",'성냥팔이소녀의재림']
    array=range(6)
    matrix=['1','2','3','4','5','6']
    context = {
        'name': name,
        'data': data,
        'empty_data': empty_data,
        'array': array,
        'matrix': matrix,
        'number': 10,
    }
    return render(request, 'home.html', context)

def lotto(request):

    lotto = random.sample(range(1,46), 6)
    context = {
        'lotto': lotto,
        'number': 10,
    }
    return render(request, 'lotto.html', context)

def cube(request, num):
    context = {
        'num': num**3,
    }
    return render(request, 'cube.html', context)

def match(request):
    import random
    goonghap = random.randint(50, 100)

    me = request.POST.get('me')
    you = request.POST.get('you')
    # https://docs.djangoproject.com/en/2.2/ref/request-response/
    context = {
        'me': me,
        'you': you,
        'goonghap': goonghap,
    }
    return render(request, 'match.html', context)

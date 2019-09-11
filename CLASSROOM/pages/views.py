from django.shortcuts import render

# Create your views here.

def info(request):
    context = {
        'teacher': '강동주',
        'student': ['이건희','박상우','이한얼','김현호'],
    }

    return render(request, 'info.html', context)


def name(request, name):
    
    db = {
        '이건희': 27,
        '박상우': 28,
        '이한얼': 27,
        '김현호': 28,
    }

    context = {
        'name': name,
        'age': db.get(name),
    }
    return render(request, 'name.html', context)

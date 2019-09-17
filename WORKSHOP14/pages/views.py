from django.shortcuts import render

# Create your views here.
def push(request):

    return render(request, 'push.html')

def pull(request):
    num = request.GET.get('num')
    context = {
        'num': num,
    }
    return render(request, 'pull.html', context)
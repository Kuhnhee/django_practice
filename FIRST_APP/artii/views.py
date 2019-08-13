from django.shortcuts import render
import requests
import bs4
# Create your views here.

def artii(request):
    url = "http://artii.herokuapp.com/fonts_list"
    response = requests.get(url).text

    font_list = response.split(' ')

    context = {
        'list': font_list,
    }


    return render(request, 'artii.html', context)

def artiiresult(request):
    text = request.GET.get('text')
    url = "http://artii.herokuapp.com/make?text="
    url += text

    response = requests.get(url).text

    context = {
        'show':response,
    }
    
    # me = request.GET.get('me')
    return render(request, 'artiiresult.html', context)

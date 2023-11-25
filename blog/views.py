from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
# Create your views here.

def home(request):
    return HttpResponse('Bienvenue dans mon Blog!')

def detail(request, article_id):
    text = 'Detail du Blog #{0}!'.format(article_id)
    return HttpResponse(text)

def heure_actuelle(request):
    return render(request, 'blog/date.html', {'date': datetime.now()})

def addition(request, num1, num2):
    total = int(num1) + int(num2)
    return render(request, 'blog/addition.html', {'num1': num1, 'num2': num2,  'total' : total})

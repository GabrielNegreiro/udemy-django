from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'recipes/home.html', context={
        'nome': 'Gabriel'
    })

def contato(response):
    return HttpResponse("Contato 1")
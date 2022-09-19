from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.

def home(request):
    return render(request, 'generator/home.html')

def password(request):

    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    characters = list(alphabet)

    if request.GET.get('upperCase'):
        characters.extend(list(alphabet.upper()))
    if request.GET.get('special'):
        characters.extend(list('!@#$%^&*()-.,:;'))
    if request.GET.get('numbers'):
        characters.extend(list('1234567890'))

    length = int(request.GET.get('length', 8))
    if length == 0:
        return render(request, 'generator/home.html')
    else:
        thepassword = ''
        for x in range(length):
            thepassword += random.choice(characters)
        return render(request, 'generator/password.html', {'password': thepassword})

def about(request):
    return render(request, 'generator/about.html')

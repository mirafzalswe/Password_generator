from django.shortcuts import render
import random
# Create your views here.


def index(request):
    return render(request, 'generator/index.html')

def password(request):

    charactesr = list('abcdefghijklmnopqrstuvwxyz')
    if request.GET.get('uppercase'):
        charactesr.extend(list('ABCDEFGHIJKLMOPQRSRUVWXYZ'))

    if request.GET.get('special'):
        charactesr.extend(list('!@#$%^&*()_+'))

    if request.GET.get('number'):
        charactesr.extend(list('1234567890'))

    uzunlik = request.GET.get('length',12) # deflaut qiyamat 12 da dekani
    password = ''
    for x in range(int(uzunlik)):
        password += random.choice(charactesr)
    return render(request, 'generator/password.html', {'password' : password})
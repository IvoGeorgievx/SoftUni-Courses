import random
from datetime import datetime

from django.http import HttpResponse
from django.shortcuts import render, redirect


def home_page(request, *args, **kwargs):
    context = {
        'title': 'First solo try',
        'value': random.random(),
        'info': {
            'address': 'Cambridge'
        },
        'time_now': datetime.now(),
        'items': ['Creatine', 'Beta Alanine', 'Protein', 'BCAA']
    }
    return render(request, 'home_page.html', context)


def returning_something(request, id):
    return render(request, 'home_page.html')


def redirecting_showhow(request):
    return redirect('home page')


def supplements(request):
    context = {
        'items': ['Creatine', 'Beta Alanine', 'Protein', 'BCAA'],
    }
    return render(request, 'supplements.html', context)

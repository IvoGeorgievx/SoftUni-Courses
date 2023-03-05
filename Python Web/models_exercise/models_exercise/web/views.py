from django.contrib.auth.models import User
from django.shortcuts import render

from models_exercise.web.models import Employees, Department


def index(request):

    employees = Employees.objects.all()

    context = {
        'employees': Employees.objects.all(),
    }

    return render(request, 'index.html', context)
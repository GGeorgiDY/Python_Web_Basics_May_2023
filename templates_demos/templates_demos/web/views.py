import random
from datetime import datetime

from django.http import HttpResponse
from django.shortcuts import render, redirect


class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def all(self):
        return f'{self.name} is {self.age} years old'


def index(request):
    context = {
        'title': 'SoftUni Homepage',
        'value': random.random(),
        'info': {
            'address': 'Sofia'
        },
        'student': Student('Doncho', 19),
        'student_info': Student('Doncho', 19).all(),
        'now': datetime.now(),
        'students': ['Pesho', 'Pesho', 'Gosho', 'Maria', 'Stamat'],
        'values': list(range(1, 20)),
    }

    # return HttpResponse()
    return render(request, 'index.html', context)


def redirect_to_home(request):
    return redirect('index')


def about(request):
    return render(request, 'about.html')

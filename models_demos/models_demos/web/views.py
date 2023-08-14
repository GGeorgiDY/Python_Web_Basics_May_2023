from django.shortcuts import render

from models_demos.web.models import Employee


def index(request):
    x = list(Employee.objects.all())
    pass

from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse

from .models import *
from datetime import datetime

# Create your views here.
def index(request):
    cars = Car.objects.all()
    context = {
        'car_list': cars,
        'app_name': 'CarApp'
    }
    return render(request, 'index.html', context)


def car_details(request, car_id):
    car = get_object_or_404(Car, pk=car_id)
    context = {
        'car_data': car,
        'app_name': 'CarApp'
    }
    return render(request, 'details.html', context)
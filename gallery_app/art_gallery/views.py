from django.shortcuts import render
from .models import *
from datetime import datetime


# Create your views here.
def index(request):
    # Show flights in the past
    arts = Artwork.objects.filter(date__lte=datetime.now().date())
    context = {'flight_list': arts, 'app_name': 'FlightApp'}
    return render(request, 'index.html', context)




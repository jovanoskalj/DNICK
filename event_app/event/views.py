from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse

from .forms import EventForm
from .models import *

# Create your views here.

# Create your views here.
def index(request):
    # Show flights in the past
    events = Event.objects.filter(user=request.user)
    context = {'events_list': events, 'app_name': 'event'}
    return render(request, 'index.html', context)


def add_event(request):
    if request.method == 'POST':
        form = EventForm(request.POST, request.FILES)
        if form.is_valid():
            event = form.save(commit=False)
            event.user = request.user
            event.save()
            return redirect('index')

    form = EventForm()
    return render(request, "add_event.html", context={'form': form})


def edit_event(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    # Flight.objects.filter(pk=flight_id).exists()

    if request.method == 'POST':
        form = EventForm(request.POST, request.FILES, instance=event)
        if form.is_valid():
            event = form.save(commit=False)
            event.user = request.user
            event.save()
            return redirect('index')

    form = EventForm(instance=event)
    return render(request, "edit_event.html", context={'form': form, 'event_id': event_id})
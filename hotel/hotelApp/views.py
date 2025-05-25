from django.shortcuts import render, get_object_or_404, redirect

from .forms import *
from .models import *


# Create your views here.
def index(request):
    reservations = Reservation.objects.filter(room__isCleaned=True, room__room_number__lte=5).all()
    context = {'reservation_list': reservations, 'app_name': 'ReservationApp'}
    return render(request, 'index.html', context)


def edit_reservation(request, reservation_id):
    reservation = get_object_or_404(Reservation, pk=reservation_id)
    if request.method == 'POST':
        form = ReservationForm(request.POST, request.FILES, instance=reservation)
        if form.is_valid():
            form.save()
        return redirect('index')

    form = ReservationForm(instance=reservation)
    return render(request, 'edit_reservation.html', context={'form': form, 'reservation_id': reservation_id})


def details(request, reservation_id):
    reservation = Reservation.objects.filter(id=reservation_id).first()
    context = {'reservation_data': reservation, 'app_name': 'ReservationApp'}
    return render(request, 'details.html', context)

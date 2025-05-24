from django.shortcuts import render, get_object_or_404, redirect
from joblib.externals.cloudpickle import instance

from .models import *
from .forms import *


# Create your views here.

def index(request):
    estates = RealEstate.objects.filter(isSold=False, area__gte=100).all()
    context = []

    for estate in estates:
        price = 0
        estate_characteristics = RealEstateCharacteristics.objects.filter(real_estate=estate)
        for est_ch in estate_characteristics:
            price += est_ch.characteristic.price  # Претпоставувам дека `price` е поле во `RealEstateCharacteristics`

        context.append({'real_estate': estate, 'price': price})  # собирај ги во context

    return render(request, 'index.html', {'real_estates': context})



def edit(request, estate_id):
    real_estate = get_object_or_404(RealEstate, pk=estate_id)

    # Земи карактеристики како string
    existing_characteristics = RealEstateCharacteristics.objects.filter(real_estate=real_estate)
    characteristics_string = ', '.join([rc.characteristic.name for rc in existing_characteristics])

    if request.method == 'POST':
        form = RealEstateForm(request.POST, request.FILES, instance=real_estate, characteristics_str=characteristics_string)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = RealEstateForm(instance=real_estate, characteristics_str=characteristics_string)

    return render(request, "edit_estate.html", context={'form': form, 'estate_id': estate_id, 'estate':real_estate})


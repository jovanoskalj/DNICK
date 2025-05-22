from lib2to3.fixes.fix_input import context

from django.shortcuts import render, redirect

from .forms import RepairForm
from .models import *
from . import forms
# Create your views here.

def index(request):
    return  render(request,"index.html")

def add_repair(request):
    if request.method == 'POST':
        form = RepairForm(request.POST,request.FILES)
        if form.is_valid():
            repair = form.save(commit=False)
            repair.user = request.user
            repair.image = form.cleaned_data["image"]
            repair.save()
            return redirect("add")

    context = {
        "form": forms.RepairForm,
        # "repairs":Service.objects.filter(user=request.user,car__type="Sedan")
        "repairs": Service.objects.all()
    }
    return  render(request,"repairs.html",context)
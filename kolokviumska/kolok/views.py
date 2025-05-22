from lib2to3.fixes.fix_input import context

from django.db.transaction import commit
from django.shortcuts import render, redirect

from .forms import TravelForm
from .models import  *
# Create your views here.

def index(request):
    travels = Travel.objects.filter(duration__gt=1)
    return render(request, 'index.html',context={'travels':travels})

def add_destination(request):
    if request.method=='POST':
        form = TravelForm(request.POST,request.FILES)
        if form.is_valid():
            travel = form.save(commit=False)
            travel.guide=Guide.objects.filter(user=request.user).first()
            travel.save()
        return redirect('index')
    form = TravelForm()
    return  render(request,'add_destination.html',context={'form':form})
from django.shortcuts import render, redirect

# Create your views here.
from .forms import *
from .models import *

# Create your views here.
def index(request):
    # Show flights in the past
    books = Book.objects.all()
    context = {'book_list': books, 'app_name': 'booksApp'}
    return render(request, 'index.html', context)

def details(request, book_id):
    book = Book.objects.filter(id=book_id).first()
    context = {'book_data': book, 'app_name': 'booksApp'}
    return render(request, 'details.html', context)

def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return redirect('index')

    form = BookForm()
    return render(request, "add_book.html", context={'form': form})
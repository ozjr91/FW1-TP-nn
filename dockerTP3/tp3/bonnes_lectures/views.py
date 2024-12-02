from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def about(request):
    return HttpResponse("Application Bonnes Lectures, développée en TP de Framework Web, Université d’Orléans, 2024.")


from django.shortcuts import render
def welcome(request):
    return render(request,'welcome.html')


from django.shortcuts import render
from .models import Book
def all_books(request):
    books=Book.objects.all()
    return render(request,'all_books.html',{'books':books})

from django.shortcuts import render, get_object_or_404
from .models import Book
def details(request,book_id):
    book=get_object_or_404(Book,pk=book_id)
    return render(request,'details.html',{'book':book})


from django.shortcuts import render, redirect
from .forms import BookForm

def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('all_books')  # Redirige vers la liste des livres
    else:
        form = BookForm()
    return render(request, 'add_book.html', {'form': form})


from django.shortcuts import get_object_or_404
from django.views.decorators.http import require_POST
from django.http import HttpResponseRedirect
from django.urls import reverse

def delete_book(request, book_id):
    book = get_object_or_404(Book, pk=book_id)

    if request.method == 'POST':
        book.delete()
        return HttpResponseRedirect(reverse('all_books'))

    return render(request, 'delete_book.html', {'book': book})


from django.shortcuts import get_object_or_404, redirect
from .forms import BookForm

def edit_book(request, book_id):
    # Récupérer le livre à modifier
    book = get_object_or_404(Book, pk=book_id)

    if request.method == 'POST':
        # Liaison des données POST avec le formulaire
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()  # Enregistre les modifications
            return redirect('all_books')  # Redirige vers la liste des livres
    else:
        # Pré-remplit le formulaire avec les données existantes
        form = BookForm(instance=book)

    return render(request, 'edit_book.html', {'form': form, 'book': book})



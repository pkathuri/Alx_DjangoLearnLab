from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from .models import Book
from .models import Library
# Create your views here.
# Finctional view for the book model
def list_books(request):
    books = Book.objects.all()
    return render(request, 'templates/relationship_app/list_books.html', {'books': books})
# Class view for the library model
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'templates/relationship_app/library_detail.html'
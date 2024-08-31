from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth.views import LoginView,LogoutView
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
# The registration registration view
# This is a function based view
def register(request):
    if request.method == "POST":
        # A form for creating new users providing a username and password.
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
        else:
            form = UserCreationForm()
        return render(request,"relationship_app/templates/register.html",{"form":form})
# The login view
class LoginView(LoginView):
    template_name = "login.html"

# The logout view
class LogoutView(LogoutView):
    template_name = "logout.html"

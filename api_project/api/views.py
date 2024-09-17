from django.shortcuts import render
from rest_framework import generics
from .models import Book
# Importing from the serializer 
from .serializers import BookSerializer

# Create your views here.
# creating a view named BookList that extends rest_framework.generics.ListAPIView
class BookList(generics.ListCreateAPIView):
    # A queryset containing all the data that is going to be rendered in the front-end
    queryset = Book.object.all()
    # Using the BookSerializer to serialize the data and the Book model as the queryset.
    serializer_class = BookSerializer
from django.contrib import admin
# Importing the book model
from .models import Book
# Register your models here.
admin.site.register(Book)
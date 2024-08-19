from django.contrib import admin
# Importing the book model
from bookshelf.models import Book
# Register your models here.
admin.site.register(Book)
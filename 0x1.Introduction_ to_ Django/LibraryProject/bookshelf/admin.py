from django.contrib import admin
# Importing the book model
from .models import Book
# Register your models here.
admin.site.register(Book)
# This enables the customization of of list display and search functionalities
class BookAdmin(admin.ModelAdmin):
    list_display = ('title','author','publication_year')
    list_filter = ('publication_year', 'author')
    search_fields = ('title','author')
# Registering the Book and BookAdmin classes
admin.site.register(Book,BookAdmin)
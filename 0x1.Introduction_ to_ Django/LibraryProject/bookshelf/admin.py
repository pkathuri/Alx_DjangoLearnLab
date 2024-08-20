from django.contrib import admin
# Importing the book model
from bookshelf.models import Book
# Register your models here.
admin.site.register(Book)
# This enables the customization of of list display and search functionalities
class BookAdmin(admin.ModelAdmin):
    list_display = ('title','author','publication_year')
    search_fields = ('title','author')
# Registering the Book and BookAdmin classes
admin.site.register(Book,BookAdmin)
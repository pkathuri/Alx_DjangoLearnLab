from relationship_app.models import Book
from relationship_app.models import Library

# Obtaining all books by a specific author
books = Book.objects.get(author="John Doe")
# obtaining all books in a library
library_books = Library.books.all()
# Obtaining all the


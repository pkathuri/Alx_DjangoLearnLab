from relationship_app.models import Book
from relationship_app.models import Library

# A query of all books by a specific author
books_by_author = Book.objects.filter(author = "John Doe")


from django.urls import path,include
from .views import BookListCreateAPIView
urlpatterns = [
    path('books/', BookList.as_view(), name='book-list'),  # Maps to the BookList view
]
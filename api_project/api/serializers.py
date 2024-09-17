# Importing from the same directory
from .models import Book
import json

# Defining a BookSerializer class that extends rest_framework.serializers.ModelSerializer and includes all fields of the Book model
class BookSerializer(rest_framework.serializers.ModelSerializer):
    # The meta class sefines the behaviour of a class
    class Meta:
        model = Book
        # This displays all the fields of the Book to the front-end
        fields = "__all__"
    

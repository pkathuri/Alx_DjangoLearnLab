from django.db import models
# This is for buildinng the authentication or using the built in user authentication
from django.contrib.auth.models import User,AbstractBaseUser
# Importing the postsave for the purpose of automating the saving of an entry
from django.db.models.signals import post_save
from django.dispatch import receiver
class Author(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name



class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Library(models.Model):
    name = models.CharField(max_length=255)
    books = models.ManyToManyField(Book)

    def __str__(self):
        return self.name

class Librarian(models.Model):
    name = models.CharField(max_length=255)
    library = models.OneToOneField(Library, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

#  The UserProfile model
class UserProfile(models.Model):
    user = models.OneToOneField(User,on_delete = models.CASCADE)
    role = models.CharField(max_length = 100,choices=["Admin","Librarian","Member"])
# Use Django signals to automatically create a UserProfile when a new user is registered.
@receiver(post_save,sender = User)
def create_user_profile(sender,instance,created,**kwargs):
    if created:
        UserProfile.objects.create(user=instance)

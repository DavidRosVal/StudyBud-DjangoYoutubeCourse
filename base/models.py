from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Topic(models.Model):
    name = models. CharField(max_length=200)

    def __str__(self):
        return self.name

class Room(models.Model):
    host = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    topic = models.ForeignKey(Topic, on_delete=models.SET_NULL, null=True) # on_delete=models.SET_NULL When a Topic is deleted, its Rooms dont - null=True its allowing the table to have empty values
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True) # It cant be blank
    # participants =
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-updated', '-created']

    # everytime we use str() or print() with an object of this class, what is gonna be returned is the attribute name
    def __str__(self): 
        return self.name
    
class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE) # One User can have many Messages
    room = models.ForeignKey(Room, on_delete=models.CASCADE) # Room comes to be the parent, and Message children (one to many relation) - on_delete=models.CASCADE means when a Room (parent) is deleted all the Messages(children) are deleted to
    body = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self): 
        return self.body[0:50] # at max the first 50 characters
    
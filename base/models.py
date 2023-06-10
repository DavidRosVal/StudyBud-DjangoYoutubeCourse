from django.db import models

# Create your models here.

class Room(models.Model):
    # host = 
    # topic =
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True) # It cant be blank
    # participants =
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    # everytime we use str() or print() with an object of this class, what is gonna be returned is the attribute name
    def __str__(self): 
        return self.name
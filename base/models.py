from django.db import models

class Room(models.Model):
    # host = models.CharField(max_length=255)
    # topic
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True) # null=True means if the user doesn't enter a description, it will not exist in the database

    def __str__(self):
        return self.name

# Create your models here.

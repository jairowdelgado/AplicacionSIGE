from django.db import models

# Create your models here.


class Electiva(models.Model):
    name=models.CharField(max_length=44)
    password = models.CharField(max_length=44)
    
    def __str__(self):
        return self.name

class Users(models.Model):
    name=models.CharField(max_length=44)
    password = models.CharField(max_length=44)
    
    def __str__(self):
        return self.name

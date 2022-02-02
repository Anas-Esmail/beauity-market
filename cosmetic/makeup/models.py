from pydoc import describe
from pyexpat import model
from tkinter import CASCADE
from django.db import models

# Create your models here.
class brands(models.Model):
    name=models.CharField(max_length=100)
    origin=models.CharField(max_length=100)
    
    def __str__(self):
         return "brands details"
    def get_absolute_url(self):
       return "something"

class products(models.Model):
     name=models.CharField(max_length=100)
     kind=models.CharField(max_length=100)
     description=models.CharField(max_length=100)
     expire_date=models.DateField()
     price=models.IntegerField()
    #  brand = models.ForeignKey(brands, models.CASCADE)
 
     

     def __str__(self):
         return "products detail"
     def get_absolute_url(self):
       return "something"
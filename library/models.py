from django.db import models
from datetime import datetime, date 
# Create your models here.

class Book(models.Model): 
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=100,blank=True)
    date = models.DateField(auto_now_add=False, auto_now=False, blank=True)     
    # date = models.DateField(auto_now_add=True, auto_now=False, blank=True)  

# datetime = models.DateTimeField(max_length=100,blank=True)
        
def __str__(self):
    return self.id
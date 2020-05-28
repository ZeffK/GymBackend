from django.db import models


# Create your models here.

# models.py
from django.db import models
class customer(models.Model):
    name = models.CharField(max_length=60)
    address=models.TextField(max_length=100)
    email = models.EmailField(max_length=70,blank=False, null= False, unique= True)
    mobile=models.CharField(max_length=20,unique=False)
    
    def __str__(self):
        return self.name

class User(models.Model):
    name=models.CharField(max_length=60,null=False)
    email = models.EmailField(max_length=70,blank=True, null= False, unique= True)
    password=models.CharField(max_length=10)
    def __str__(self):
        return self.email
    
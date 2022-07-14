from ctypes import addressof
from distutils.command.upload import upload
from pyexpat import model
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class Users(models.Model):
    uid = models.AutoField(primary_key=True)
    
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField(max_length = 254)
    phone = models.BigIntegerField()
    passw =models.CharField(max_length=200)
    address =models.CharField(max_length=300)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    zip = models.IntegerField()

    def __str__(self):
        return self.first_name + " " + self.last_name + " " + self.passw + " " + self.address + " " + self.city + " " + self.state 
# class UserCredential(models.Model):
class Home(models.Model):
    home_id = models.AutoField(primary_key=True)
    location =models.CharField(max_length=200)
    contact = models.BigIntegerField()
    zip     = models.IntegerField()
    price   = models. IntegerField()
    image = models.ImageField(upload_to='login_system/static/images/')
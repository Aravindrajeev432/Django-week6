from ctypes import addressof
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class Users(models.Model):
    uid = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField(max_length = 254)
    phone = models.IntegerField()
    passw =models.CharField(max_length=200)
    address =models.CharField(max_length=300)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    zip = models.IntegerField()

    def __str__(self):
        return self.first_name + " " + self.last_name + " " + self.passw + " " + self.address + " " + self.city + " " + self.state 
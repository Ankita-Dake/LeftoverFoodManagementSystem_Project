# Create your models here.
from django.db import models


class Agent(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=500)
    contact = models.IntegerField()
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=50)


class Donor(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=500)
    contact = models.IntegerField()
    restaurantname = models.CharField(max_length=50)
    restaurantaddress = models.CharField(max_length=50)
    city = models.CharField(max_length=50)


class Donate(models.Model):
    Agent_name = models.CharField(max_length=50)
    email = models.EmailField()
    Donor_name = models.CharField(max_length=20)
    DateOfCollectingFood = models.DateField()
    TimeOfCollectingFood = models.TimeField()
    Quantity = models.CharField(max_length=50)
    Orphanage_name = models.CharField(max_length=50)
    city = models.CharField(max_length=50)


class Donorform(models.Model):
    Donor_name = models.CharField(max_length=50)
    email = models.EmailField()
    contact = models.IntegerField()
    Donor_address = models.CharField(max_length=50)
    restaurant_name = models.CharField(max_length=20)
    restaurant_address = models.CharField(max_length=30)
    TypeOfFood = models.CharField(max_length=50)
    DateOfCooking = models.DateField()
    Quantity = models.CharField(max_length=50)
    city = models.CharField(max_length=20)

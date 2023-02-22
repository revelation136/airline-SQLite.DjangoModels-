from django.db import models


# Create your models here.
# !!!Note:everytime you make changes in models.py, you have to make migrations and then migrate
# Creating objects is done on shell - python manage.py shell, don't forget to import this model in the shell

class Airport(models.Model):
    code = models.CharField(max_length=3)
    city = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.city} ({self.code})"


class Flight(models.Model):
    origin = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="departure")
    destination = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="arrivals")
    duration = models.IntegerField()

    # on_delete=models.CASCADE In this case, we specify that when an airport is deleted, all flights associated
    # with it should be also deleted.
    # related_name="" Which gives us a way to search for all flights with a given airport as their origin or destination

    # to fix query view from shell. we add formatted string for more detailed object
    def __str__(self):
        return f"{self.id}: {self.origin} to {self.destination}"


class Passengers(models.Model):
    first = models.CharField(max_length=64)
    last = models.CharField(max_length=64)
    flights = models.ManyToManyField(Flight, blank=True, related_name="passengers")

    # ManyToMany is to define this class (Passengers) which means Passengers can have 1 or more flights
    # argument blank=True which means a passenger can have no flights.

    def __str__(self):
        return f"{self.first} {self.last}"

from django.shortcuts import render
from .models import Flight, Airport


# Create your views here.

def index(request):
    return render(request, "flights/index.html", {
        "flights": Flight.objects.all()
    })


# "flights": Flight.objects.all() this means flights is the variable in the HTML file
# and is equals to Flight.objects.all(), this is Django APi

def flight(request, flight_id):
    flight = Flight.objects.get(id=flight_id)
    return render(request, "flights/flight.html", {
        "flight": flight
    })

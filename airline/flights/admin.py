from django.contrib import admin
from .models import Flight, Airport, Passengers


class FlightAdmin(admin.ModelAdmin):
    list_display = ("id", "origin", "destination", "duration")


class PassengerAdmin(admin.ModelAdmin):
    filter_horizontal = ("flights",)


# Register your models here.
admin.site.register(Flight, FlightAdmin)
# register the flight but use the FlightAdmin interface.
admin.site.register(Airport)
admin.site.register(Passengers, PassengerAdmin)

# user: jones, password: 1234, email: jones@a.com

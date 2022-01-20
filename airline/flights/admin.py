from django.contrib import admin
from .models import Flight, Airport, Passengers


class FlightAdmin(admin.ModelAdmin):
    list_display = ("id", "origin", "destination", "duration")


# Register your models here.
admin.site.register(Flight, FlightAdmin)
admin.site.register(Airport)
admin.site.register(Passengers)

# user: jones, password: 1234, email: jones@a.com

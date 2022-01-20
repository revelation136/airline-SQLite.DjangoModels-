from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name='index'),
    path("<int:flight_id>", views.flight, name="flight"),
    path("<int:flight_id>/books", views.book, name="book")
    # <int:flight_id> this will show the directory of url in this case it is 127:0.0.1:8000/flights/2 if you click
    # flight Flight 2
]

from django.urls import path
from . import views

urlpatterns= [
    path("getListOfHotels/", views.Hotel_List, name="hotels"),
    path("reservationConfirmation/", views.ReservationList, name="home"),

]
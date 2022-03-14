from django.shortcuts import render
from django.http import  HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Hotels
from .models import Reservation
from .serializers import HotelSerializer
from .serializers import GuestSerializer
from .serializers import ReservationSerializer

from rest_framework import generics
from rest_framework import filters


@api_view(['GET','POST'])
def Hotel_List(request):
    if request.method == 'GET':
        hotellist = Hotels.objects.all()
        hotelSerializer = HotelSerializer(hotellist,many=True)
        return Response({"hotel_list":hotelSerializer.data})
    elif request.method == 'POST':
        hotel_request = request.data
        serializeHotelData = HotelSerializer(data=hotel_request)
        if serializeHotelData.is_valid():
                serializeHotelData.save()
                obj = Hotels.objects.latest('id')
                return Response({"hotel_id":obj.pk})
        return Response({"status":"Failed"})


@api_view(['GET','POST'])
def ReservationList(request):
    if request.method == 'GET':
        reservationList = Reservation.objects.all()
        reservationSerializer = ReservationSerializer(reservationList,many=True)
        return Response({"hotel_list":reservationSerializer.data})
    elif request.method == 'POST':
        hotel_request = request.data
        serializeReservationData = reservationSerializer(data=hotel_request)
        if serializeReservationData.is_valid():
                serializeReservationData.save()
                id = Reservation.objects.latest('id')
                return Response({"confirmation_number":id.pk})
        return Response({"status":"Failed"})




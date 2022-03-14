from rest_framework import serializers
from .models import Hotels
from .models import Guest
from .models import Reservation


class HotelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hotels
        fields = ['id','name', 'price', 'available']

class GuestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Guest
        fields = ['guest_name','gender']


class ReservationSerializer(serializers.ModelSerializer):
    guests_list = GuestSerializer(many=True,)
    class Meta:
        model = Reservation
        fields = ['hotelname','checkin_date','checkout_date',"guests_list"]

    def create(self, validated_data):
        choice_validated_data = validated_data.pop('guests_list')
        question = Reservation.objects.create(**validated_data)
        choice_set_serializer = self.fields['guests_list']
        for each in choice_validated_data:
            each['Reservation'] = question
        choices = choice_set_serializer.create(choice_validated_data)
        return question
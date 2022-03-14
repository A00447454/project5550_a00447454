from django.db import models
# Create your models here.

class Hotels(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, null=False)
    price = models.IntegerField()
    available = models.BooleanField()

    def __str__(self):
        return self.name

class Reservation(models.Model):
    id = models.AutoField(primary_key=True)
    hotelname = models.CharField(max_length=100, null=False)
    checkin_date = models.CharField(max_length=100)
    checkout_date = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Guest(models.Model):
    id = models.AutoField(primary_key=True)
    Reservation = models.ForeignKey(Reservation, related_name='guest_list', on_delete=models.CASCADE)
    guest_name = models.CharField(max_length=100, null=True)
    gender = models.CharField(max_length=10)

    def __str__(self):
        return self.guest_name
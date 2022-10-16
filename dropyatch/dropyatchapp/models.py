from datetime import datetime
from django.db import models

# Create your models here.
class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    address = models.TextField()

    def __str__(self):
        return self.first_name


## Movie Ticket Bookings

class Movie(models.Model):
    movie_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name


class Screen(models.Model):
    screen_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    total_availabe_seats = models.IntegerField()

    def __str__(self):
        return self.name


class AvaialbeBooking(models.Model):
    id = models.AutoField(primary_key=True)
    date = models.DateTimeField()
    movie = models.ForeignKey('Movie',on_delete=models.CASCADE)
    screen = models.ForeignKey('Screen',on_delete=models.CASCADE)

class Booking(models.Model):
    booking_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    date = models.DateTimeField(default=datetime.now)
    slot = models.ForeignKey("AvaialbeBooking",on_delete=models.CASCADE)
    seat_number = models.IntegerField()











import imp
from django.contrib import admin
from .models import User, Movie, Screen, AvaialbeBooking, Booking

# Register your models here.
admin.site.register(User)
admin.site.register(Movie)
admin.site.register(Screen)
admin.site.register(AvaialbeBooking)
admin.site.register(Booking)

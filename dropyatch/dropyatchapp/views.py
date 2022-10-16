
from ast import Return
import re
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from django.core.exceptions import ObjectDoesNotExist

from .models import User, Movie, Screen, AvaialbeBooking, Booking
from .serializer import UserSerializer, MovieSerializer, AvaialbeBookingSerializer, BookingSerializer, BookingWriteSerializer

class UserList(APIView):

    def get(self,request):
        users = User.objects.all()
        serializer = UserSerializer(users,many=True)
        return Response(serializer.data)

    def post(self,request):
        serializer = UserSerializer(data = request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserListDetail(APIView):
    def get_object(self, user_id):
        try:
            return User.objects.get(user_id=user_id)
        except ObjectDoesNotExist:
            return None

    def get(self, request, user_id, *args, **kwargs):
        user_instance = self.get_object(user_id)
        if not user_instance:
            return Response(
                {"res": "Object with user id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = UserSerializer(user_instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, user_id, *args, **kwargs):
        user_instance = self.get_object(user_id)
        if not user_instance:
            return Response(
                {"res": "Object with user id does not exists"}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        data = request.data
        serializer = UserSerializer(instance = user_instance, data=data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, user_id, *args, **kwargs):
    
        user_instance = self.get_object(user_id)
        if not user_instance:
            return Response(
                {"res": "Object with todo id does not exists"}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        user_instance.delete()
        return Response(
            {"res": "Object deleted!"},
            status=status.HTTP_200_OK
        )


class MoviesList(APIView):

    def get(self,request):
        movies = Movie.objects.all()
        serializer = MovieSerializer(movies,many=True)
        return Response(serializer.data)

    def post(self,request):
        serializer = MovieSerializer(data = request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AvailableSeats(APIView):

    def get(self,request):
        movie_id = request.GET.get('movie_id', None)
        date = request.GET.get('date', None)
        bookings = AvaialbeBooking.objects.filter(movie__movie_id=movie_id)
        if date:
            bookings = bookings.filter(date=date)
        serializers = AvaialbeBookingSerializer(bookings,many=True)


        return Response(serializers.data)


class BookingList(APIView):

    def get(self,request):
        # Considering the email to be unique
        user_email = request.GET.get('user_email', None)
        if user_email:
            booking = Booking.objects.filter(email=user_email)
            serializer = BookingSerializer(booking,many=True)
            return Response(serializer.data)
        else:
            return Response("Please pass the user_email", status=status.HTTP_400_BAD_REQUEST)
        

    def post(self,request):
        
        serializer = BookingWriteSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

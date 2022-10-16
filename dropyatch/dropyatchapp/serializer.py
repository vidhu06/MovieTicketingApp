from rest_framework import serializers
from .models import User, Movie, AvaialbeBooking, Booking

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = "__all__"
class MovieSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = "__all__"

class AvaialbeBookingSerializer(serializers.ModelSerializer):
    movie = serializers.CharField(source='movie.name')
    screen = serializers.CharField(source='screen.name')
    date = serializers.DateTimeField(format="%Y-%m-%d")
    time_slot = serializers.SerializerMethodField()
    available_seats = serializers.SerializerMethodField()

    class Meta:
        model = AvaialbeBooking
        fields = ['date','time_slot','movie','screen','available_seats']

    def get_time_slot(self,obj):
        date = obj.date
        return date.time()

    def get_available_seats(self,obj):
        booking_list = Booking.objects.filter(slot__id = obj.id)
        booked_seats = []
        for b in booking_list:
            booked_seats.append(b.seat_number)

        ## Assuming it has 10 seats only for simplicity
        available_seats = [item for item in range(1, 10) if item not in booked_seats]
        return str(available_seats)

class BookingSerializer(serializers.ModelSerializer):
    booking_details = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Booking
        fields = ['booking_id','name','email','seat_number','booking_details']

    def get_booking_details(self,obj):
        detail_obj = AvaialbeBooking.objects.get(id=obj.slot.id)
        if detail_obj:
            detail = {
                "movie" : detail_obj.movie.name,
                "screen": detail_obj.screen.name,
                "date": detail_obj.date.date(),
                "time": detail_obj.date.time()

            }       
            return detail

        return None

class BookingWriteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Booking
        fields = "__all__" 
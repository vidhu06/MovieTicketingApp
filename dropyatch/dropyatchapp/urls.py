from django.urls import path

from . import views

urlpatterns = [
    path('users/', views.UserList.as_view()),
    path('users/<int:user_id>/', views.UserListDetail.as_view()),
    path('movies/', views.MoviesList.as_view()),
    path('available_seats/', views.AvailableSeats.as_view()),
    path('booking/',views.BookingList.as_view())
]
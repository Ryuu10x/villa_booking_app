"""define URL patterns for the villa_booking_app"""

from django.urls import path

from . import views

app_name = 'villa_booking_app'
urlpatterns = [
    #Home page
    path('', views.index, name="index"),
]
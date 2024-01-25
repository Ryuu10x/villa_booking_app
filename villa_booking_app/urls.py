"""define URL patterns for the villa_booking_app"""

from django.urls import path
from . import views

app_name = 'villa_booking_app'
urlpatterns = [
    #Home page
    path('', views.index, name="index"),
    path('villa/<int:villa_id>/', views.villa_detail, name='villa_info'),
    path('villa/<int:villa_id>/book/', views.book_villa, name='book_villa'),
]


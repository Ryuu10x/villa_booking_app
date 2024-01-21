from django.shortcuts import render

# Create your views here.

def index(request):
    # The home page for villa_booking_app
    return render(request, 'villa_booking_app/index.html')
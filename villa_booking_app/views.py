from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from .models import Villa, Booking
from .forms import BookingForm #Create a form in the next step

# Create your views here.

def index(request):
    # The home page for villa_booking_app
    villas = Villa.objects.all()
    context = {'villas': villas}
    return render(request, 'villa_booking_app/home.html', context)

#display villa info
def villa_detail(request, villa_id):
    villa = get_object_or_404(Villa, pk = villa_id)

    #get booked dates for the villa
    booked_dates = Booking.objects.filter(villa=villa).values_list('check_in_date', 'check_out_date')

    context = {
        'villa':villa,
        'booked_dates': booked_dates,
    }
    return render(request, 'villa_booking_app/villa_info.html', context)

#view to handle booking data
#function to handle date overlaps and calculations (probabaly better refactored)
def book_villa(request, villa_id):
    villa = get_object_or_404(Villa, pk=villa_id)

    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)

            #check availablity (overlaps)
            if Booking.objects.filter(
            (Q(check_in_date__range=[booking.check_in_date, booking.check_out_date]) |
            Q(check_out_date__range=[booking.check_in_date, booking.check_out_date])),
            villa=villa
            ).exists():
                return render(request, 'villa_booking_app/booking_error.html', {'error_message': 'Selected dates are not available.', 'villa': villa})

            booking.villa = villa
            booking.user = request.user

            #cost calculation
            booking.total_cost = (booking.check_out_date - booking.check_in_date).days * villa.price_per_night
            booking.save()
            return redirect('villa_booking_app:villa_info', villa_id=villa_id)
    else:
        form = BookingForm()
    

    context = {'form': form, 'villa': villa}
    return render(request, 'villa_booking_app/booking_form.html', context)
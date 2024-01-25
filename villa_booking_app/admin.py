from django.contrib import admin

# Register your models here.
from .models import Villa, Booking

admin.site.register(Villa)
admin.site.register(Booking)
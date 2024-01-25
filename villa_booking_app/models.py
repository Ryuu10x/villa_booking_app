from django.db import models
from django.contrib.auth.models import User #using Django default authentication

# Create your models here.
# datatables

class Villa(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    capacity = models.IntegerField()
    price_per_night = models.DecimalField(max_digits=8, decimal_places = 2)

    def __str__(self):
        return self.name


class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    villa = models.ForeignKey(Villa, on_delete=models.CASCADE)
    check_in_date = models.DateField()
    check_out_date = models.DateField()
    total_cost = models.DecimalField(max_digits = 8, decimal_places = 2)

    def __str__(self):
        return f"{self.user.username} - {self.villa.name}"
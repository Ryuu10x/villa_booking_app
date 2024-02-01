from django.shortcuts import render

# Create your views here.
# users/views.py
from django.shortcuts import redirect
from django.urls import reverse

def redirect_to_login(request):
    return redirect('users:login')

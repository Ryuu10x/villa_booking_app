"""Define URL patterns for users"""

from django.urls import path, include
from django.contrib.auth.views import LoginView

app_name = 'users'
urlpatterns = [
    #include default auth urls
    path('login/', LoginView.as_view(), name='login'),
    path('', include('django.contrib.auth.urls')),
]
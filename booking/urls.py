from django.urls import path

from .views import booking_page, booking_success


urlpatterns = [
    path('', booking_page, name='booking'),
    path('BOOK-PLAN/', booking_page, name='booking_page'),
    path('success/', booking_success, name='booking_success'),
    
]
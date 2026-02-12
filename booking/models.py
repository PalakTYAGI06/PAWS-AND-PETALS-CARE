

# Create your models here.
from django.db import models
from django.conf import settings

class Booking(models.Model):
    SERVICE_CHOICES = (
        ('pet', 'Pet Care'),
        ('plant', 'Plant Care'),
    )

    DURATION_CHOICES = (
        ('1_day', '1 Day'),
        ('1_week', '1 Week'),
        ('1_month', '1 Month'),
    )
    PLAN_CHOICES =[
        ('basic', 'Basic Care'),
        ('scavo', 'Scavo Care'),
        ('premium', 'Premium Care'),
        ('bloom', 'Premium Bloom'),
    ]

    
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE)
    plan = models.CharField(max_length=20, choices=PLAN_CHOICES, default='basic')
    price = models.CharField(max_length=50, default='0')
    created_at = models.DateTimeField(auto_now_add=True)
    

    service_type = models.CharField(max_length=20, choices=SERVICE_CHOICES)
    duration = models.CharField(max_length=20, choices=DURATION_CHOICES)
    location = models.CharField(max_length=255)
    start_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.service_type}"

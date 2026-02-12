from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Booking

@login_required
def booking_page(request):
    if request.method == "POST":
        plan_name = request.POST.get('plan_name')
        price = request.POST.get('price')
        
        # Map plan names to plan choices
        plan_mapping = {
            'Basic Care': 'basic',
            'Scavo Care': 'scavo',
            'Premium Care': 'premium',
            'Premium Bloom': 'bloom'
        }
        
        plan = plan_mapping.get(plan_name, 'basic')
        
        Booking.objects.create(
            user=request.user,
            plan=plan,
            price=price,
            service_type=request.POST.get('service_type', 'pet'),
            duration=request.POST.get('duration', '1_day'),
            location=request.POST.get('location', 'Unknown'),
            start_date=request.POST.get('start_date', '2026-02-10')
        )
        return redirect('booking_success')

    return render(request, 'service.html')

def booking_success(request):
    return render(request, 'booking_success.html')
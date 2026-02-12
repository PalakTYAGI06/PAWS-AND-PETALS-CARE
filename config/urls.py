"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include
from django.contrib import admin
from django.urls import path
from core import views
from django.contrib.auth import views as auth_views


from core import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),   # ✅ ONLY ONE URL
    path('register/', views.register_view, name='register'),
    path('plan/', views.plan_page, name='plan'),
    path('service/', views.service, name='service'),
    path('care/',views.care, name='care'),
    
   path('login/', views.login_view, name='login'),
   path('booking/', include('booking.urls')),
    # Redirect target
    path('services/', views.services_page, name='services'),
    
    path('live.Login/', views.login_view, name='live.login'),
    path('plan/', views.plan_page, name='plan_page'),
    path('camera/', views.camera_page, name='camera_page'),



    path('admin/', admin.site.urls),
     path('live/', views.live_page, name='live_page'),
    path('feed/', views.live_feed, name='live_feed'),
    path('snapshot/', views.save_snapshot, name='save_snapshot'),
     path('live.login/', views.login_view, name='login'),
     # path('accounts/', include('django.contrib.auth.urls')),   # login, logout, password reset
   

    #feedback#
    path('feedback/', views.feedback_view, name='feedback'),
    path('feedback/success/', views.feedback_success, name='feedback_success'),
    
]
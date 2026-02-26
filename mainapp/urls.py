from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('colleges/', views.colleges, name='colleges'),
    path('students/', views.students, name='students'),
    path('address/', views.address, name='address'),
    path('contact_us/',views.contact_us,name='contact_us'),
]

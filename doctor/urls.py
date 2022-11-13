from django.urls import path
from . import views

app_name = 'doctor'

urlpatterns = [
    path('doctor/profile', views.doctor_profile, name='profile'),
    path('doctor/appointments', views.doctor_appointments, name='appointments'),
    path('doctor/edit-appointment/<str:id>/', views.edit_appointment, name='edit_appointment'),
]

from django.urls import path
from . import views

app_name = 'patient'

urlpatterns = [
    path('patient/profile', views.patient_profile, name='profile'),
    path('patient/book-appointment', views.book_appointment, name='book_appointment'),
    path('patient/appointments', views.appointments, name='appointments'),
]

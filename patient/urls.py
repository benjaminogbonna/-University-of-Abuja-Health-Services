from django.urls import path
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy
from . import views

app_name = 'patient'

urlpatterns = [
    path('patient/profile', views.patient_profile, name='profile'),
    path('patient/book-appointment', views.book_appointment, name='book_appointment'),
    path('patient/appointments', views.appointments, name='appointments'),



    # change password urls from account
    path('patient/password-change/',
         auth_views.PasswordChangeView.as_view(success_url=reverse_lazy('patient:password_change_done')),
         name='password_change'),
    path('patient/password-change/done/', auth_views.PasswordChangeDoneView.as_view(),
         name='password_change_done'),

    # reset password urls in case you forget
    path('patient/password-reset/', auth_views.PasswordResetView.as_view(
        success_url=reverse_lazy('patient:password_reset_done')), name='password_reset'),
    path('patient/password-reset/done/', auth_views.PasswordResetDoneView.as_view(),
         name='password_reset_done'),
    path('patient/reset-password/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        success_url=reverse_lazy('patient:password_reset_complete')), name='password_reset_confirm'),
    path('patient/reset-password/done/', auth_views.PasswordResetCompleteView.as_view(),
         name='password_reset_complete'),

]

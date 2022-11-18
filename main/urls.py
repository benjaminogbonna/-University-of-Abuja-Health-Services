from django.urls import path, reverse_lazy
from django.contrib.auth import views as auth_views
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('staffs', views.staffs, name='staffs'),
    path('contact', views.contact, name='contact'),
    path('account/login/', views.user_login, name='login'),
    path('account/logout/', views.log_out, name='logout'),


    # change password urls from account
    path('account/password-change/',
         auth_views.PasswordChangeView.as_view(success_url=reverse_lazy('main:password_change_done')),
         name='password_change'),
    path('account/password-change/done/', auth_views.PasswordChangeDoneView.as_view(),
         name='password_change_done'),

    # reset password urls in case you forget
    path('account/password-reset/', auth_views.PasswordResetView.as_view(
        success_url=reverse_lazy('main:password_reset_done')), name='password_reset'),
    path('account/password-reset/done/', auth_views.PasswordResetDoneView.as_view(),
         name='password_reset_done'),
    path('account/reset-password/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        success_url=reverse_lazy('main:password_reset_complete')), name='password_reset_confirm'),
    path('account/reset-password/done/', auth_views.PasswordResetCompleteView.as_view(),
         name='password_reset_complete'),
]

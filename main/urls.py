from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('staffs', views.staffs, name='staffs'),
    path('contact', views.contact, name='contact'),
    path('account/login/', views.user_login, name='login'),
    path('account/logout/', views.log_out, name='logout'),
]

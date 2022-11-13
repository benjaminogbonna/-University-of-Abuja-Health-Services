from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from .forms import LoginForm
from patient.models import Patient
from doctor.models import Doctor


def index(request):
    return render(request, 'main/index.html')


def about(request):
    return render(request, 'main/about.html')


def staffs(request):
    return render(request, 'main/staffs.html')


def contact(request):
    return render(request, 'main/contact.html')


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user_authenticate = authenticate(request,
                                             username=cd['username'],
                                             password=cd['password'])
            if user_authenticate is not None:
                user = User.objects.get(username=cd['username'])
                try:
                    data = Patient.objects.get(username=user)
                    login(request, user)
                    return redirect('patient:profile')
                except:
                    try:
                        data = Doctor.objects.get(username=user)
                        login(request, user)
                        return redirect('doctor:profile')
                    except:
                        return redirect('main:index')
            else:

                messages.error(request, 'Please enter correct credentials. Note that both fields may be case-sensitive.')
    else:
        form = LoginForm()
    return render(request, 'main/login.html', {'form': form})


def log_out(request):
    logout(request)
    return redirect("main:login")

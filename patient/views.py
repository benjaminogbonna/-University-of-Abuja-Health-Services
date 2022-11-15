from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.decorators.cache import cache_control
from django.contrib.auth.decorators import login_required
from .forms import ProfileEditForm, AppointmentForm


# a view for users to edith their profile
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required
def patient_profile(request):
    if request.method == 'POST':
        profile_form = ProfileEditForm(instance=request.user.patient,
                                       data=request.POST,
                                       files=request.FILES)
        if profile_form.is_valid():
            profile_form.save()
            messages.success(request, 'Profile updated successfully!')
            return redirect('patient:profile')
        else:
            messages.error(request, 'Error updating your profile!')
    else:
        profile_form = ProfileEditForm(instance=request.user.patient)

    context = {
        'profile_form': profile_form,
    }
    return render(request, 'patient/patient_profile.html', context)


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required
def book_appointment(request):
    if request.method == "POST":
        form = AppointmentForm(request.POST)
        if form.is_valid():
            appointment = form.save(commit=False)
            appointment.patient = request.user.patient
            appointment.save()
            messages.success(request, 'appointment booked successfully!')
            return redirect('patient:appointments')
        else:
            messages.error(request, "An error occurred, please try again!")
    else:
        form = AppointmentForm()

    context = {
        'form': form,
    }
    return render(request, 'patient/book_appointment.html', context)


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required
def appointments(request):
    user = request.user.patient
    appointment_list = user.appointments.all().order_by('date')
    context = {
        'appointment_list': appointment_list,

    }
    return render(request, 'patient/appointments.html', context)


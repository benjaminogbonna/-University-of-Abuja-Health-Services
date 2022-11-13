from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.views.decorators.cache import cache_control
from django.contrib.auth.decorators import login_required
from patient.models import Patient, Appointment
from .forms import ProfileEditForm, AppointmentEditForm


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required
def doctor_profile(request):
    if request.method == 'POST':
        profile_form = ProfileEditForm(instance=request.user.doctor,
                                       data=request.POST,
                                       files=request.FILES)
        if profile_form.is_valid():
            profile_form.save()
            messages.success(request, 'Profile updated successfully!')
            return redirect('doctor:profile')
        else:
            messages.error(request, 'Error updating your profile!')
    else:
        profile_form = ProfileEditForm(instance=request.user.doctor)

    context = {
        'profile_form': profile_form,
    }
    return render(request, 'doctor/doctor_profile.html', context)


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required
def doctor_appointments(request):
    user = request.user.doctor
    appointment_list = user.appointments.all().order_by('date')
    context = {
        'appointment_list': appointment_list,

    }
    return render(request, 'doctor/appointments.html', context)


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required
def edit_appointment(request, id):
    appointment = get_object_or_404(Appointment, id=id)
    if request.user == appointment.doctor.username:
        if request.method == 'POST':
            form = AppointmentEditForm(instance=appointment, data=request.POST, files=request.FILES)
            if form.is_valid():
                appointment = form.save(commit=False)
                appointment.save()
                messages.success(request, f'appointment updated successfully!')
                return redirect('doctor:appointments')
            else:
                messages.error(request, 'Error updating appointment!')
        else:
            form = AppointmentEditForm(instance=appointment)
    else:
        return redirect('doctor:profile')
    context = {
        'appointment': appointment,
        'form': form,
    }
    return render(request, 'doctor/edit_appointment.html', context=context)

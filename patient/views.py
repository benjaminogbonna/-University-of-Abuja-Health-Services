from django.shortcuts import render
from django.contrib.auth import logout
from django.shortcuts import render, redirect, HttpResponseRedirect, get_object_or_404
from django.urls import reverse
from django.contrib import messages
from django.views.decorators.cache import cache_control
from django.contrib.auth.decorators import login_required
from django.conf import settings
from .forms import ProfileEditForm


def log_out(request):
    logout(request)
    return redirect("patient:login")


# a view for users to edith their profile
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required
def profile(request):
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


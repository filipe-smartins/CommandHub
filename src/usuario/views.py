from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login as auth_login
from django.contrib import messages
from django.contrib.auth.models import User
from .forms import RegistrationForm, ProfileForm
from .models import Profile


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Ensure a Profile exists (signals should create it, but be explicit)
            Profile.objects.get_or_create(user=user)
            auth_login(request, user)
            messages.success(request, 'Registration successful. Welcome!')
            return redirect('usuario:profile', username=user.username)
    else:
        form = RegistrationForm()
    return render(request, 'usuario/register.html', {'form': form})


def profile(request, username):
    user = get_object_or_404(User, username=username)
    # Ensure profile exists for display
    profile, _ = Profile.objects.get_or_create(user=user)
    return render(request, 'usuario/profile.html', {'profile_user': user, 'profile': profile})


@login_required
def edit_profile(request):
    # Ensure current user has a profile instance
    profile, _ = Profile.objects.get_or_create(user=request.user)
    if request.method == 'POST':
        pform = ProfileForm(request.POST, request.FILES, instance=profile)
        if pform.is_valid():
            pform.save()
            messages.success(request, 'Profile updated successfully.')
            return redirect('usuario:profile', username=request.user.username)
    else:
        pform = ProfileForm(instance=profile)
    return render(request, 'usuario/edit_profile.html', {'pform': pform})

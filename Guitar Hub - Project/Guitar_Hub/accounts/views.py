from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from .forms import CustomUserCreationForm
from .forms import ProfileForm

def register(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.email = form.cleaned_data["email"]
            user.save()
            login(request, user)
            return redirect("home")
        else:
            print(form.errors)
    else:
        form = CustomUserCreationForm()

    return render(request, "accounts/register.html", {"form": form})


@login_required
def profile(request):
    profile = request.user.profile

    if request.method == "POST":
        profile_form = ProfileForm(request.POST, request.FILES, instance=profile)
        if profile_form.is_valid():
            profile_form.save()
            return redirect("profile")
    else:
        profile_form = ProfileForm(instance=profile)

    return render(request, "accounts/profile.html", {
        "profile": profile,
        "profile_form": profile_form,
    })

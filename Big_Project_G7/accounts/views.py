# accounts/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login as auth_login, authenticate
from django.contrib.auth import logout
from django.conf import settings
from .forms import SignupForm
from .models import Profile

def custom_logout_view(request):
    logout(request)
    return redirect('index')


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            # new_user = Profile(user=user,
            #                                     user_type=form.cleaned_data.get('user_type'),
            #                                     name=form.cleaned_data.get('name'),
            #                                     phone_number=form.cleaned_data.get('phone_number'))
            # new_user.save()
            if user is not None:
                auth_login(request, user)
                return redirect(settings.LOGIN_REDIRECT_URL)
    else:
        form = SignupForm()
    return render(request, 'registration/signup.html', {'form': form})


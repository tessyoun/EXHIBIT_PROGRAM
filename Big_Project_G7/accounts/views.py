# accounts/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login as auth_login, authenticate
from django.contrib.auth import logout
from django.conf import settings
from .forms import SignupForm
from .models import Profile
from django.contrib.auth.decorators import login_required

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
            if user is not None:
                auth_login(request, user)
                return redirect(settings.LOGIN_REDIRECT_URL)
    else:
        form = SignupForm()
    return render(request, 'registration/signup.html', {'form': form})

@login_required
def mypage_view(request):
    user = request.user
    is_regular = user.group.filter(name='일반고객').exists()
    is_business = user.groups.filter(name='기업고객').exists()
    context = {
        'is_regular' : is_regular,
        'is_business': is_business,
    }
    return render(request, 'mypage.html', context)
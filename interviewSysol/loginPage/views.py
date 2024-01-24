from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .forms import UserRegisterForm, UserProfileForm
from django.shortcuts import render
from .models import UserProfile
from django.contrib.auth.decorators import login_required


def signup_page(request):
    if request.method == 'POST':
        user_form = UserRegisterForm(request.POST)
        profile_form = UserProfileForm(request.POST, request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            login(request, user)
            messages.success(request, 'Your account has been created!')
            return redirect('user_profile')
    else:
        user_form = UserRegisterForm()
        profile_form = UserProfileForm()
    
    context = {
        'user_form': user_form,
        'profile_form': profile_form
    }
    return render(request, 'signup_page.html', context)

def login_page(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            try:
                user = User.objects.get(username=username)
            except:
                messages.error(request, 'User does not Exist')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('user_profile')
            else:
                messages.error(request, 'Username Or Password Does not Exist')

    context = {}
    return render(request, 'login_page.html', context)

def logout_page(request):
    logout(request)
    return redirect('home')


def home(request):
    return render(request, 'home.html')


@login_required
def user_profile(request):
    user_profile = request.user.profile
    user_details = {
        'username': request.user.username,
        'first_name': request.user.first_name,
        'last_name': request.user.last_name,
        'email': request.user.email,
    }
    context = {'user_profile': user_profile, 'user_details': user_details}
    return render(request, 'user_profile.html', context)


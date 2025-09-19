from django.shortcuts import render, redirect
from . import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, update_session_auth_hash, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from car_post.models import Car
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
# Create your views here.

def register(request):
    if request.method == 'POST':
        register_form = forms.RegistrationForm(request.POST)
        if register_form.is_valid():
            register_form.save()
            messages.success(request, 'Account Created Successfully')
            return redirect('register')
        
    else:
        register_form = forms.RegistrationForm
    return render(request, 'register.html', {'form': register_form, 'type':'Register'})
    

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            user_name = form.cleaned_data['username']
            user_pass = form.cleaned_data['password']
            user = authenticate(username = user_name, password =user_pass)
            if user is not None:
                messages.success(request, 'logged in Successfully')
                login(request, user)
                return redirect('profile')
            else:
                 messages.warning(request, 'login information incorrect')
                 return redirect('register')
            
    else: 
        form = AuthenticationForm()
        return render(request, 'register.html', {'form':form, 'type': 'Login'})
    



@login_required
def profile(request):
    data = Car.objects.filter(owner = request.user )
    return render(request, 'profile.html', {'data' : data})

@login_required
def edit_profile(request):
    if request.method == 'POST':
        profile_form = forms.ChangeUserForm(request.POST, instance = request.user)
        if profile_form.is_valid():
            profile_form.save()
            messages.success(request, 'profile Updated Successfully')
            return redirect('profile')
        

    else:
        profile_form = forms.ChangeUserForm(instance = request.user)

    return render(request, 'update_profile.html', {'form' : profile_form})



def user_logout(request):
    logout(request)
    return redirect('user_login')
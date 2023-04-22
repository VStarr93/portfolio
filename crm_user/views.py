# crm_user/views.py
#-------------------------------------------------------------
#-------------------------------------------------------------
# IMPORTS

from django.shortcuts import render, redirect
from django.http import HttpResponse 
from django.contrib.auth.forms import UserCreationForm
from crm_user.forms import *

#-------------------------------------------------------------
#-------------------------------------------------------------
# Create your views here.

# INDEX view
def index(request):
    """
        This is a basic view for crm_user app.
    """
    return HttpResponse("This is the Index for CRM_USER app.")

# User Registration View
def user_registration(request):
    """
        This is a user registration view.
    """
    if request.method == 'GET':
        form = CustomUserCreationForm
        return render(request, 'registration/user_registration.html', context={'form':form})

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/accounts/login/')
        else:
            message = form.errors
            context = {
                'form': CustomUserCreationForm(request.POST),
                'message': message,
            }
            return render(request, 'registration/user_registration.html', context)

# User Change View
def user_change(request):
    """
        This is a user change view.
    """
    if request.method == 'GET':
        form = CustomUserChangeForm(instance=request.user)
        return render(request, 'registration/user_change.html', context={'form': form})

    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            return render(request, 'registration/user_change.html', context={'form':form})
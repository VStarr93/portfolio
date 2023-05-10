# crm_user/views.py
#-------------------------------------------------------------
#-------------------------------------------------------------
# IMPORTS

from django.shortcuts import render, redirect
from django.http import HttpResponse 
from django.contrib.auth.forms import UserCreationForm
from crm_user.forms import *
from django.apps import apps
from crm_user.models import Address

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
    
# User Profile View
def profile_view(request):
    """ This is a User Profile view"""
    
    context = {
        'user': request.user,
        'apps': {
            'crm_user': apps.is_installed('crm_user'), 
            'crm_invoice': apps.is_installed('crm_invoice'),
        },
        'address_list': Address.objects.filter(user=request.user),
    }
    
    if request.method == 'GET':
        context['changeForm'] = CustomUserChangeForm(instance=request.user)
        return render(request, 'crm_user/profile.html', context=context)
    
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('crm_user:profile')
        else:
            context['changeForm'] = form
            return render(request, 'crm_user/profile.html', context=context)
        
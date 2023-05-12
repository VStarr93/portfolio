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
from django.forms.models import modelformset_factory 

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
        if 'customerBtn' in request.GET:
            context = {
                'form': CustomerCreationForm
            }
            return render(request, 'crm_user/registration.html', context)

        if 'empBtn' in request.GET:
            context = {
                'form': SimpleEmployeeCreationForm
            }
            return render(request, 'crm_user/registration.html', context)

        if 'adminBtn' in request.GET:
            context = {
                'form': SimpleAdminCreationForm
            }
            return render(request, 'crm_user/registration.html', context)
        else:
            context = {}
            return render(request, 'crm_user/user_registration.html', context)

    if request.method == 'POST':
        
        if 'submitCustomer' in request.POST:
            form = CustomerCreationForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('/accounts/login/')
            else:
                context = {
                    'form': CustomerCreationForm(request.POST)
                }
                return render(request, 'crm_user/registration.html', context)
        
    
# User Profile View
def profile_view(request):
    """ This is a User Profile view"""
    
    #FormSet 
    AddressFormSet = modelformset_factory(Address, form=AddressForm, extra=1, can_delete=True)
    
    # Global context for this view
    context = {
        'user': request.user,
        'apps': {
            'crm_user': apps.is_installed('crm_user'), 
            'crm_invoice': apps.is_installed('crm_invoice'),
        },
        'address_list': Address.objects.filter(user=request.user),
        'addressFormSet': AddressFormSet(queryset=Address.objects.filter(user=request.user)),
        'addressFormHelper': AddressFormHelper(),
    }
    
    if request.method == 'GET':
        context['changeForm'] = CustomUserChangeForm(instance=request.user)
        return render(request, 'crm_user/profile.html', context=context)
    
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance=request.user)
        AddressFormSet = modelformset_factory(Address, form=AddressForm, can_delete=True)
        addressFormSet = AddressFormSet(request.POST)
        
        if 'submitChange' in request.POST:
            if form.is_valid():
                form.save()
            else:
                context['changeForm'] = form
                return render(request, 'crm_user/profile.html', context=context)
        
        if 'submitAddress' in request.POST:
            if addressFormSet.is_valid():
                addresses = addressFormSet.save(commit = False)
                for address in addresses:
                    address.user = request.user 
                    address.save()
            else:
                context['addressFormSet'] = addressFormSet
                return render(request, 'crm_user/profile.html', context=context)
        
        return redirect('crm_user:profile')
        
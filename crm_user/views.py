# crm_user/views.py
#-------------------------------------------------------------
#-------------------------------------------------------------
# IMPORTS

from django.shortcuts import render, redirect
from django.http import HttpResponse 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from crm_user.forms import *
from django.apps import apps
from crm_user.models import Address
from django.forms.models import modelformset_factory 

from guardian.decorators import permission_required_or_403

#-------------------------------------------------------------
#-------------------------------------------------------------
# Create your views here.

# INDEX view
def index(request):
    """ This is a basic view for crm_user app. """
    context = {
        'user': request.user,
    }
    if request.user.is_authenticated and request.user.email != settings.ANONYMOUS_USER_NAME:
        return render(request, 'crm_user/home.html', context)
    else:
        return redirect('login')
        
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
        
        if 'submitEmployeeSimple' in request.POST:
            form = SimpleEmployeeCreationForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('/accounts/login/')
            else:
                context = {
                    'form': SimpleEmployeeCreationForm(request.POST),
                }
                return render(request, 'crm_user/registration.html', context)
        
        if 'submitAdminSimple' in request.POST:
            form = SimpleAdminCreationForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('/accounts/login/')
            else:
                context = {
                    'form': SimpleAdminCreationForm(request.POST),
                }
                return render(request, 'crm_user/registration.html', context)
        
    
# User Profile View
def profile_view(request):
    """ This is a User Profile view"""
    
    #FormSet 
    AddressFormSet = modelformset_factory(Address, form=AddressForm, extra=1, can_delete=True)
    
    #Global Variables
    if request.user.type == 'CUSTOMER':
        profile = CustomerProfile.objects.get(user=request.user)
    if request.user.type == 'ADMIN':
        profile = AdminProfile.objects.get(user=request.user)
    if request.user.type == 'EMPLOYEE':
        profile = EmployeeProfile.objects.get(user=request.user)
    
    # Global context for this view
    context = {
        'user': request.user,
        'apps': {
            'crm_user': apps.is_installed('crm_user'), 
            'crm_invoice': apps.is_installed('crm_invoice'),
        },
        'addressFormSet': AddressFormSet(queryset=Address.objects.filter(user=request.user)),
        'addressFormHelper': AddressFormHelper(),
        'changeForm': CustomUserChangeForm(instance=request.user),
    }
    
    if request.user.type == 'CUSTOMER':
        context['customizeForm'] = CustomerCustomizeForm(instance=profile)
    elif request.user.type == 'ADMIN':
        context['customizeForm'] = AdminCustomizeForm(instance=profile)
    elif request.user.type == 'EMPLOYEE':
        context['customizeForm'] = EmployeeCustomizeForm(instance=profile)
    
    # GEt Method
    if request.method == 'GET':
        return render(request, 'crm_user/profile.html', context=context)
    
    # POST Method
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance=request.user)
        AddressFormSet = modelformset_factory(Address, form=AddressForm, can_delete=True)
        addressFormSet = AddressFormSet(request.POST)
        
        if request.user.type == 'CUSTOMER':
            customizeForm = CustomerCustomizeForm(request.POST, instance=profile)
        elif request.user.type == 'ADMIN':
            customizeForm = AdminCustomizeForm(request.POST, instance=profile)
        elif request.user.type == 'EMPLOYEE':
            customizeForm = EmployeeCustomizeForm(request.POST, instance=profile)
            
        if 'submitChange' in request.POST:
            if form.is_valid():
                user = request.user
                if user.type == "CUSTOMER":
                    user.profile.last_modified_by = user 
                    user.profile.save()
                elif user.type == "ADMIN":
                    user.admin_profile.last_modified_by = user 
                    user.admin_profile.save()
                elif user.type == "EMPLOYEE":
                    user.emp_profile.last_modified_by = user 
                    user.emp_profile.save()
                    
                form.save()
                
            else:
                context['changeForm'] = form
                return render(request, 'crm_user/profile.html', context=context)
        
        if 'submitAddress' in request.POST:
            if addressFormSet.is_valid():
                addresses = addressFormSet.save(commit = False)
                for obj in addressFormSet.deleted_objects:
                    obj.delete()
                    
                for address in addresses:
                    address.user = request.user 
                    address.save()
                    
                user = request.user
                if user.type == "CUSTOMER":
                    user.profile.last_modified_by = user 
                    user.profile.save()
                elif user.type == "ADMIN":
                    user.admin_profile.last_modified_by = user 
                    user.admin_profile.save()
                elif user.type == "EMPLOYEE":
                    user.emp_profile.last_modified_by = user 
                    user.emp_profile.save()
                    
            else:
                context['addressFormSet'] = addressFormSet
                return render(request, 'crm_user/profile.html', context=context)
        
        if 'submitCustomize' in request.POST:
            if customizeForm.is_valid():
                user = request.user
                if user.type == "CUSTOMER":
                    user.profile.last_modified_by = user 
                    user.profile.save()
                elif user.type == "ADMIN":
                    user.admin_profile.last_modified_by = user 
                    user.admin_profile.save()
                elif user.type == "EMPLOYEE":
                    user.emp_profile.last_modified_by = user 
                    user.emp_profile.save()
                    
                customizeForm.save()
            else:
                context['customizeForm'] = customizeForm
                return render(request, 'crm_user/profile.html', context=context)
        
        return redirect('crm_user:profile')
        
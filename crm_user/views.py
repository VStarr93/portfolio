# crm_user/views.py
#-------------------------------------------------------------
#-------------------------------------------------------------
# IMPORTS

from django.shortcuts import render, redirect
from django.http import HttpResponse 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required, user_passes_test
from crm_user.forms import *
from django.apps import apps
from crm_user.models import Address
from django.forms.models import modelformset_factory 
from django.conf import settings 

from guardian.decorators import permission_required_or_403

#-------------------------------------------------------------
#-------------------------------------------------------------
# Create your functions here.

def not_anonymous(user):
    if user.is_anonymous or user.email == settings.ANONYMOUS_USER_NAME:
        return False 
    else:
        return True

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
    """ This is a user registration view. """
    if request.method == 'GET':
        if 'customerBtn' in request.GET:
            if request.user.is_anonymous or request.user.type == 'EMPLOYEE' or request.user.type == 'ADMIN':
                context = {
                    'form': CustomerCreationForm
                }
                return render(request, 'crm_user/registration.html', context)
            else:
                return redirect('crm_user:home')

        if 'empBtn' in request.GET:
            if request.user.is_anonymous or request.user.email == settings.ANONYMOUS_USER_NAME:
                return redirect('crm_user:home')
            elif request.user.type == 'ADMIN' or (request.user.type == 'EMPLOYEE' and request.user.emp_profile.is_manager == True):
                context = {
                    'form': SimpleEmployeeCreationForm
                }
                return render(request, 'crm_user/registration.html', context)
            else:
                return redirect('crm_user:home')

        if 'adminBtn' in request.GET:
            if request.user.is_anonymous or request.user.email == settings.ANONYMOUS_USER_NAME:
                return redirect('crm_user:home')
            elif request.user.type == 'ADMIN' or (request.user.type == 'EMPLOYEE' and request.user.emp_profile.is_manager == True):
                context = {
                    'form': SimpleAdminCreationForm
                }
                return render(request, 'crm_user/registration.html', context)
            else:
                return redirect('crm_user:home')
        else:
            if request.user.is_anonymous or request.user.email == settings.ANONYMOUS_USER_NAME or request.user.type == 'EMPLOYEE' or request.user.type == 'ADMIN':
                context = {}
                return render(request, 'crm_user/user_registration.html', context)
            else:
                return redirect('crm_user:home')

    if request.method == 'POST':
        
        if 'submitCustomer' in request.POST:
            if request.user.is_anonymous or request.user.email == settings.ANONYMOUS_USER_NAME or request.user.type == 'EMPLOYEE' or request.user.type == 'ADMIN':
                form = CustomerCreationForm(request.POST)
                if form.is_valid():
                    form.save()
                    return redirect('/accounts/login/')
                else:
                    context = {
                        'form': CustomerCreationForm(request.POST)
                    }
                    return render(request, 'crm_user/registration.html', context)
            else:
                return redirect('crm_user:home')
        
        if 'submitEmployeeSimple' in request.POST:
            if request.user.is_anonymous or request.user.email == settings.ANONYMOUS_USER_NAME:
                return redirect('crm_user:home')
            elif request.user.type == 'ADMIN' or (request.user.type == 'EMPLOYEE' and request.user.emp_profile.is_manager == True):
                form = SimpleEmployeeCreationForm(request.POST)
                if form.is_valid():
                    form.save()
                    return redirect('/accounts/login/')
                else:
                    context = {
                        'form': SimpleEmployeeCreationForm(request.POST),
                    }
                    return render(request, 'crm_user/registration.html', context)
            else:
                return redirect('crm_user:home')
        
        if 'submitAdminSimple' in request.POST:
            if request.user.is_anonymous or request.user.email == settings.ANONYMOUS_USER_NAME:
                return redirect('crm_user:home')
            elif request.user.type == 'ADMIN' or (request.user.type == 'EMPLOYEE' and request.user.emp_profile.is_manager == True):
                form = SimpleAdminCreationForm(request.POST)
                if form.is_valid():
                    form.save()
                    return redirect('/accounts/login/')
                else:
                    context = {
                        'form': SimpleAdminCreationForm(request.POST),
                    }
                    return render(request, 'crm_user/registration.html', context)
            else:
                return redirect('crm_user:home')
       
# User Profile View
@user_passes_test(not_anonymous)
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
    
    # GET Method
    if request.method == 'GET':
        return render(request, 'crm_user/profile.html', context=context)
    
    # POST Method
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, request.FILES, instance=request.user)
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
                user.last_modified_by = user 
                user.save()    
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
                user.last_modified_by = user 
                user.save()
                    
            else:
                context['addressFormSet'] = addressFormSet
                return render(request, 'crm_user/profile.html', context=context)
        
        if 'submitCustomize' in request.POST:
            if customizeForm.is_valid():
                user = request.user
                user.last_modified_by = user 
                user.save()
                    
                customizeForm.save()
            else:
                context['customizeForm'] = customizeForm
                return render(request, 'crm_user/profile.html', context=context)
        
        return redirect('crm_user:profile')
        
# User Details View
@user_passes_test(not_anonymous)
@permission_required_or_403('crm_user.view_user', (User, 'id', 'id'))
def user_details_view(request, id):
    """ Define a view to display customer details """
    # Global Variables
    context = {}
    user = User.objects.get(id=id)
    if user.type == 'CUSTOMER':
        context['customer'] = user 
    if user.type == 'ADMIN':
        context['admin'] = user 
    if user.type == 'EMPLOYEE':
        context['employee'] = user 
        
    # GET Method
    if request.method == 'GET':
        return render(request, 'crm_user/user_details.html', context)

# crm_user/signals/handlers.py
#-------------------------------------------------------------
#-------------------------------------------------------------
# IMPORTS

from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver 
from crm_user.models import User, Customer, Employee, Admin, CustomerProfile, EmployeeProfile, AdminProfile, Address
from django.contrib.auth.forms import PasswordResetForm
from django.http import HttpRequest 
from django.conf import settings 
from django.utils import timezone 

#-------------------------------------------------------------
#-------------------------------------------------------------
# Create your handlers here.

# Add Receiver for creating Customer Profile from Customer Model
@receiver(post_save, sender=Customer)
def create_customer_profile(sender, **kwargs):
    user = kwargs['instance']
    created = kwargs['created']
    if created :
        new_profile = CustomerProfile.objects.create(
            user = user,
            last_modified_by = user,
        )
        form = PasswordResetForm({'email': new_profile.user.email,})
        assert form.is_valid()
        request = HttpRequest()
        request.META['SERVER_NAME'] = 'localhost'
        request.META['SERVER_PORT'] = '8000'
        form.save(
            request=request, 
            use_https=False,
            from_email='veronicastarr93@gmail.com',
            email_template_name='registration/password_reset_email.html'
        )

# Add Receiver for creating Employee Profile from Employee Model
@receiver(post_save, sender=Employee)
def create_employee_profile(sender, **kwargs):
    user = kwargs['instance']
    created = kwargs['created']
    if created :
        new_profile = EmployeeProfile.objects.create(
            user = user,
            last_modified_by = user,
        )
        form = PasswordResetForm({'email': new_profile.user.email,})
        assert form.is_valid()
        request = HttpRequest()
        request.META['SERVER_NAME'] = 'localhost'
        request.META['SERVER_PORT'] = '8000'
        form.save(
            request=request, 
            use_https=False,
            from_email='veronicastarr93@gmail.com',
            email_template_name='registration/password_reset_email.html'
        )

# Add Receiver for creating Admin Profile from Admin Model
@receiver(post_save, sender=Admin)
def create_admin_profile(sender, **kwargs):
    user = kwargs['instance']
    created = kwargs['created']
    if created :
        new_profile = AdminProfile.objects.create(
            user = user,
            last_modified_by = user,
        )
        form = PasswordResetForm({'email': new_profile.user.email,})
        assert form.is_valid()
        request = HttpRequest()
        request.META['SERVER_NAME'] = 'localhost'
        request.META['SERVER_PORT'] = '8000'
        form.save(
            request=request, 
            use_https=False,
            from_email='veronicastarr93@gmail.com',
            email_template_name='registration/password_reset_email.html'
        )
        
# Add Receiver for creating Profiles from User Model
@receiver(post_save, sender=User)
def create_profile(sender, **kwargs):
    user = kwargs['instance']
    created = kwargs['created']
    if created and user.type == "CUSTOMER":
        new_profile = CustomerProfile.objects.create(
            user = user,
            last_modified_by = user,
        )
        customer = Customer.objects.get(email=user.email)
        customer.welcome()
        form = PasswordResetForm({'email': user.email,})
        assert form.is_valid()
        request = HttpRequest()
        request.META['SERVER_NAME'] = 'localhost'
        request.META['SERVER_PORT'] = '8000'
        form.save(
            request=request, 
            use_https=False,
            from_email='veronicastarr93@gmail.com',
            email_template_name='registration/password_reset_email.html'
        )
        
    elif created and user.type == "EMPLOYEE":
        new_profile = EmployeeProfile.objects.create(
            user = user,
            last_modified_by = user,
        )
        employee = Employee.objects.get(email=user.email)
        employee.welcome()
        form = PasswordResetForm({'email': user.email,})
        assert form.is_valid()
        request = HttpRequest()
        request.META['SERVER_NAME'] = 'localhost'
        request.META['SERVER_PORT'] = '8000'
        form.save(
            request=request, 
            use_https=False,
            from_email='veronicastarr93@gmail.com',
            email_template_name='registration/password_reset_email.html'
        )
        
    elif created and user.type == "ADMIN":
        new_profile = AdminProfile.objects.create(
            user = user,
            last_modified_by = user,
        )
        admin = Admin.objects.get(email=user.email)
        admin.welcome()
        form = PasswordResetForm({'email': user.email,})
        assert form.is_valid()
        request = HttpRequest()
        request.META['SERVER_NAME'] = 'localhost'
        request.META['SERVER_PORT'] = '8000'
        form.save(
            request=request, 
            use_https=False,
            from_email='veronicastarr93@gmail.com',
            email_template_name='registration/password_reset_email.html'
        )
        
    
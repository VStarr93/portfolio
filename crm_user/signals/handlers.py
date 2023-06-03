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
        )
        user.last_modified_by = user 
        user.save()
        
# Add Receiver for sending password reset on new user creation
@receiver(post_save, sender=User)
@receiver(post_save, sender=Admin)
@receiver(post_save, sender=Employee)
@receiver(post_save, sender=Customer)
def send_password_reset(sender, **kwargs):
    user = kwargs['instance']
    created = kwargs['created']
    if created :
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

# Add Receiver for setting permissions on new customer creation
@receiver(post_save, sender=Customer)
def customer_set_permissions(sender, **kwargs):
    """
    Set object-level permissions. 
    The customer user can view and change the object, 
    The Admin group can view, change, and delete the object,
    The Employee - Manager group can view, change, and delete the object,
    The Employee - Standard group can view the object.
    """
    
    user, created = kwargs["instance"], kwargs["created"]
    if created and user.email != settings.ANONYMOUS_USER_NAME:      
        # Get permissions
        content_type = ContentType.objects.get_for_model(Customer)
        view_perm = Permission.objects.get(content_type__app_label='crm_user', codename='view_user')  
        change_perm = Permission.objects.get(content_type__app_label='crm_user', codename='change_user')  
        delete_perm = Permission.objects.get(content_type__app_label='crm_user', codename='delete_user')  
        
        # Assign the customer view and change permission
        assign_perm(view_perm, user, user)
        assign_perm(change_perm, user, user)

        # Assign Admin Group all permissions
        group, created = Group.objects.get_or_create(name='Admins')
        for perm in [view_perm, change_perm, delete_perm]:
            assign_perm(perm, group, user)

        # Assign Employee - Manager Group all permissions
        group, created = Group.objects.get_or_create(name='Employee - Manager')
        for perm in [view_perm, change_perm, delete_perm]:
            assign_perm(perm, group, user)

        # Assign Employee - Standard Group view permission
        group, created = Group.objects.get_or_create(name='Employee - Standard')
        assign_perm(view_perm, group, user)
        
        # Add customer user to Customer Group
        group, create = Group.objects.get_or_create(name='Customer')
        user.groups.add(group)
    
# Add Receiver for creating Employee Profile from Employee Model
@receiver(post_save, sender=Employee)
def create_employee_profile(sender, **kwargs):
    user = kwargs['instance']
    created = kwargs['created']
    if created :
        new_profile = EmployeeProfile.objects.create(
            user = user,
        )
        user.last_modified_by = user 
        user.save()
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
        )
        user.last_modified_by = user 
        user.save()
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
        )
        user.last_modified_by = user 
        user.save()
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
        )
        user.last_modified_by = user 
        user.save()
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
        )
        user.last_modified_by = user 
        user.save()
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
        
# Add Receiver for Updated last modified from Address Model
@receiver(post_save, sender=Address)
def address_change_update_last_modified(sender, **kwargs):
    address = kwargs['instance']
    user = address.user 
    user.last_modified = timezone.now()
    user.save()
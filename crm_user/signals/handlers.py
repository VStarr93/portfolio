# crm_user/signals/handlers.py
#-------------------------------------------------------------
#-------------------------------------------------------------
# IMPORTS

from django.db.models.signals import post_save 
from django.dispatch import receiver 
from crm_user.models import User, Customer, Employee, Admin, CustomerProfile, EmployeeProfile, AdminProfile


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
    elif created and user.type == "EMPLOYEE":
        new_profile = EmployeeProfile.objects.create(
            user = user,
            last_modified_by = user,
        )
    elif created and user.type == "ADMIN":
        new_profile = AdminProfile.objects.create(
            user = user,
            last_modified_by = user,
        )

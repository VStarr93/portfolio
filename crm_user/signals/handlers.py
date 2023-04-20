# crm_user/signals/handlers.py
#-------------------------------------------------------------
#-------------------------------------------------------------
# IMPORTS

from django.db.models.signals import post_save 
from django.dispatch import receiver 
from crm_user.models import Customer, Employee, Admin, CustomerProfile, EmployeeProfile


#-------------------------------------------------------------
#-------------------------------------------------------------
# Create your handlers here.

@receiver(post_save, sender=Customer)
def create_customer_profile(sender, **kwargs):
    user = kwargs['instance']
    created = kwargs['created']
    if created :
        new_profile = CustomerProfile.objects.create(
            user = user,
            last_modified_by = user,
        )

@receiver(post_save, sender=Employee)
def create_employee_profile(sender, **kwargs):
    user = kwargs['instance']
    created = kwargs['created']
    if created :
        new_profile = EmployeeProfile.objects.create(
            user = user,
            last_modified_by = user,
        )
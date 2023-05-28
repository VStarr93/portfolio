# ./crm_user/admin.py
#-------------------------------------------------------------
#-------------------------------------------------------------
# IMPORTS

from django.contrib import admin
from crm_user.models import User, Customer, Employee, Admin, AdminProfile, CustomerProfile, EmployeeProfile 
from crm_user.models import Address 
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from crm_user.forms import CustomUserChangeForm, CustomUserCreationForm
from django.contrib.auth.models import Permission

#-------------------------------------------------------------
#-------------------------------------------------------------
# Register your models here.

admin.site.register(User)
admin.site.register(Customer)
admin.site.register(Employee)
admin.site.register(Admin)
admin.site.register(AdminProfile)
admin.site.register(CustomerProfile)
admin.site.register(EmployeeProfile)

@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    """ This is the admin interface for the Address model. """
    readonly_fields = ['id']
    
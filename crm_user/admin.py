# ./crm_user/admin.py
#-------------------------------------------------------------
#-------------------------------------------------------------
# IMPORTS

from django.contrib import admin
from crm_user.models import *


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
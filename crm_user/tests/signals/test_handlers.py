#./crm_user/tests/signals/test_handlers.py
#-------------------------------------------------------------
#-------------------------------------------------------------
# IMPORTS

from django.test import TestCase
from crm_user.models import Address, User, AdminProfile, EmployeeProfile, CustomerProfile
from crm_user.signals import handlers 

# For Testing Email Services
from django.core import mail 

#-------------------------------------------------------------
#-------------------------------------------------------------
# Create your Variables here.


#-------------------------------------------------------------
#-------------------------------------------------------------
# Create your Signal tests here.


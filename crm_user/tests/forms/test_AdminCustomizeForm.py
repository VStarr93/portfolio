#./crm_user/tests/forms/test_AdminCustomizeForm.py
#-------------------------------------------------------------
#-------------------------------------------------------------
# IMPORTS

from django.test import TestCase
from crm_user.forms import AdminCustomizeForm
from crm_user.models import User, Admin, AdminProfile
from django.core.exceptions import ValidationError 
import datetime 

# For Testing Email Services
from django.core import mail 


#-------------------------------------------------------------
#-------------------------------------------------------------
# Create your Variables here.


#-------------------------------------------------------------
#-------------------------------------------------------------
# Create your Admin Customize Form tests here.

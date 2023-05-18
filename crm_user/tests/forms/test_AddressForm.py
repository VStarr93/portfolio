#./crm_user/tests/forms/test_AddressForm.py
#-------------------------------------------------------------
#-------------------------------------------------------------
# IMPORTS

from django.test import TestCase
from crm_user.forms import AddressForm
from crm_user.models import User, Address
from django.core.exceptions import ValidationError 
import datetime 

# For Testing Email Services
from django.core import mail 


#-------------------------------------------------------------
#-------------------------------------------------------------
# Create your Variables here.


#-------------------------------------------------------------
#-------------------------------------------------------------
# Create your Address Form tests here.

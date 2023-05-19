#./crm_user/tests/forms/test_CustomerCreationForm.py
#-------------------------------------------------------------
#-------------------------------------------------------------
# IMPORTS

from django.test import TestCase
from crm_user.forms import CustomerCreationForm
from crm_user.models import User, Customer
from django.core.exceptions import ValidationError 
import datetime 
from django.core.files.uploadedfile import SimpleUploadedFile 
import shutil, tempfile 

# For Testing Email Services
from django.core import mail 
#-------------------------------------------------------------
#-------------------------------------------------------------
# Create your Variables here.

MEDIA_ROOT = tempfile.mkdtemp()


#-------------------------------------------------------------
#-------------------------------------------------------------
# Create your Customer Creation Form tests here.

# Create a TestCase for Validating CustomerCreationForm Fields
# crm_user.tests.forms.test_CustomerCreationForm.FormValTests
class FormValTests(TestCase):
    """ Define a TestCase for Validating CustomerCreationForm Fields """
    def setUp(self):
        """ FormVal setUp method to create form data """
        self.formdata = {
            'first_name': 'Sara',
            'middle_name': 'Elizabeth',
            'last_name': 'Jackson',
            'email': 'test@example.com',
            'password1': 'T3st3x@mpl3',
            'password2': 'T3st3x@mpl3'
        }
    
    def test_type_is_customer(self):
        """ Define a test to validate that type is always CUSTOMER """
        form = CustomerCreationForm(self.formdata)
        self.assertTrue(form.is_valid())
        self.assertTrue(form.type == 'CUSTOMER')
    

#./crm_user/tests/test_views.py
#-------------------------------------------------------------
#-------------------------------------------------------------
# IMPORTS

from django.test import TestCase, override_settings
from crm_user.forms import *
from crm_user.models import *
from django.core.exceptions import ValidationError 
import datetime 
from django.core.files.uploadedfile import SimpleUploadedFile 
import shutil, tempfile 

# For Testing Email Services
from django.core import mail 

# For HTTP 
from http import HTTPStatus

#-------------------------------------------------------------
#-------------------------------------------------------------
# Create your Variables here.

MEDIA_ROOT = tempfile.mkdtemp()


#-------------------------------------------------------------
#-------------------------------------------------------------
# Create your Index View tests here.
# crm_user.tests.test_views.IndexViewTests 


#-------------------------------------------------------------
#-------------------------------------------------------------
# Create your Customer Profile View tests here.
# crm_user.tests.test_views.CustProfileViewTests 
class CustProfileViewTests(TestCase):
    """ Profile View tests """
    def setUp(self):
        """ ProfileView setUp method to create test users and form data"""
        self.user = Customer.objects.create_user(email='user@example.com', password="JSm1th3x@mpl3", first_name="John", last_name="Smith")
        self.changedata = {
            'middle_name': 'Jacob',
            'email': 'jsmith@example.com',
            'submitChange': True,
        }
        self.changedataerror = {
            'middle_name': 'Jacob',
            'email': 'jsmith',
            'submitChange': True,
        }
        self.customizedata = {
            'theme': 'PURPLE',
            'submitCustomize': True,
        }
        self.customizedataerror = {
            'theme': 'INDIGO',
            'submitCustomize': True,
        }
        self.addressdata1 = {
            'form-0-name': 'home',
            'form-0-type': 'RESIDENTIAL',
            'form-0-address_line1': '123 Sara Lane',
            'form-0-city': 'Houston',
            'form-0-state': 'TX',
            'form-0-zip': '77891',
            'submitAddress': True,
        }
        self.addressdataerror = {
            'form-0-name': '',
            'form-0-type': '',
            'form-0-address_line1': '123 Sara Lane',
            'form-0-city': 'Houston',
            'form-0-state': 'Texas',
            'form-0-zip': '77891',
            'submitAddress': True,
        }
        self.addressdata2 = {
            'form-0-name': 'home',
            'form-0-type': 'RESIDENTIAL',
            'form-0-address_line1': '123 Sara Lane',
            'form-0-city': 'Houston',
            'form-0-state': 'TX',
            'form-0-zip': '77891',
            'form-1-name': 'work',
            'form-1-type': 'COMMERCIAL',
            'form-1-address_line1': '567 Business Lane',
            'form-1-city': 'Spring',
            'form-1-state': 'TX',
            'form-1-zip': '77801',
            'submitAddress': True,
        }
        
    def test_change_post_correct(self):
        """ Define a test for submitting User Change Form from Profile View """
        # Login user
        self.client.login(email=self.user.email, password="JSm1th3x@mpl3")
        # send POST data
        response = self.client.post('/user/profile/', data=self.changedata, follow=True)
        # Test that HTTPStatus is OK
        self.assertEqual(response.status_code, HTTPStatus.OK)
        # Test that Redirect was sent correctly
        self.assertEqual(response.redirect_chain[0][0], "/user/profile/")
        self.assertEqual(response.redirect_chain[0][1], 302)#Temporary redirect
        # define variable for updated user
        user = Customer.objects.get(id=self.user.id)
        # Test that values were correctly changed from form submission
        self.assertNotEqual(user.middle_name, self.user.middle_name)
        self.assertEqual(user.email, self.changedata['email'])
        self.assertNotEqual(user.email, self.user.email)
        self.assertEqual(user.middle_name, self.changedata['middle_name'])
        
    
#-------------------------------------------------------------
#-------------------------------------------------------------
# Create your User Registration View tests here.
# crm_user.tests.test_views.UserRegistrationViewTests 

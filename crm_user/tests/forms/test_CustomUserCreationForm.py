#./crm_user/tests/forms/test_CustomUserCreationForm.py
#-------------------------------------------------------------
#-------------------------------------------------------------
# IMPORTS

from django.test import TestCase
from crm_user.forms import CustomUserCreationForm
#-------------------------------------------------------------
#-------------------------------------------------------------
# Create your Variables here.


#-------------------------------------------------------------
#-------------------------------------------------------------
# Create your Custom User Creation Form tests here.

# Create a TestCase for CustomUserCreationForm Required Fields
# crm_user.tests.forms.test_CustomUserCreationForm.FormReqTests 
class FormReqTests(TestCase):
    """ Define a TestCase for CustomUserCreationForm Required Fields """
    def setUp(self):
        """ FormReq setUp method to create form data """
        self.formdata = {
            'first_name': 'Sara',
            'middle_name': 'Elizabeth',
            'last_name': 'Jackson',
            'type': 'CUSTOMER',
            'email': 'test@example.com',
            'password1': 'T3st3x@mpl3',
            'password2': 'T3st3x@mpl3'
        }
    
    def test_valid_data(self):
        """ Define a test for valid data """
        form = CustomUserCreationForm(self.formdata)
        self.assertTrue(form.is_valid())
    
    def test_no_first_name(self):
        """ Define a test for no first name """
        self.formdata['first_name'] = ''
        form = CustomUserCreationForm(self.formdata)
        self.assertTrue(form.is_valid())
    
    def test_no_middle_name(self):
        """ Define a test for no middle name """
        self.formdata['middle_name'] = ''
        form = CustomUserCreationForm(self.formdata)
        self.assertTrue(form.is_valid())
    
    def test_no_last_name(self):
        """ Define a test for no last_name """
        self.formdata['last_name'] = ''
        form = CustomUserCreationForm(self.formdata)
        self.assertTrue(form.is_valid())
    
    def test_no_type(self):
        """ Define a test for no type """
        self.formdata['type'] = ''
        form = CustomUserCreationForm(self.formdata)
        self.assertFalse(form.is_valid())
    
    def test_no_email(self):
        """ Define a test for no email """
        self.formdata['email'] = ''
        form = CustomUserCreationForm(self.formdata)
        self.assertFalse(form.is_valid())
    
    def test_no_password1(self):
        """ Define a test for no password1 """
        self.formdata['password1'] = ''
        form = CustomUserCreationForm(self.formdata)
        self.assertFalse(form.is_valid())
    
    def test_no_password2(self):
        """ Define a test for no password2 """
        self.formdata['password2'] = ''
        form = CustomUserCreationForm(self.formdata)
        self.assertFalse(form.is_valid())
    
    def test_no_password(self):
        """ Define a test for no password """
        self.formdata['password1'] = ''
        self.formdata['password2'] = ''
        form = CustomUserCreationForm(self.formdata)
        self.assertFalse(form.is_valid())
    

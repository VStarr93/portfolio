#./crm_user/tests/forms/test_SimpleCustomerCreationForm.py
#-------------------------------------------------------------
#-------------------------------------------------------------
# IMPORTS

from django.test import TestCase
from crm_user.forms import SimpleCustomerCreationForm

#-------------------------------------------------------------
#-------------------------------------------------------------
# Create your Variables here.


#-------------------------------------------------------------
#-------------------------------------------------------------
# Create your Simple Customer Creation Form tests here.

# Create a TestCase for SimpleCustomerCreationForm Required Fields
# crm_user.tests.forms.test_SimpleCustomerCreationForm.FormReqTests 
class FormReqTests(TestCase):
    """ Define a TestCase for SimpleCustomerCreationForm Required Fields """
    def setUp(self):
        """ FormReq setUp method to create form data """
        self.formdata = {
            'first_name': 'Sara',
            'middle_name': 'Elizabeth',
            'last_name': 'Jackson',
            'email': 'test@example.com',
        }
    
    def test_valid_data(self):
        """ Define a test for valid data """
        form = SimpleCustomerCreationForm(self.formdata)
        self.assertTrue(form.is_valid())
    
    def test_no_first_name(self):
        """ Define a test for no first name """
        self.formdata['first_name'] = ''
        form = SimpleCustomerCreationForm(self.formdata)
        self.assertTrue(form.is_valid())
    
    def test_no_middle_name(self):
        """ Define a test for no middle name """
        self.formdata['middle_name'] = ''
        form = SimpleCustomerCreationForm(self.formdata)
        self.assertTrue(form.is_valid())
    
    def test_no_last_name(self):
        """ Define a test for no last_name """
        self.formdata['last_name'] = ''
        form = SimpleCustomerCreationForm(self.formdata)
        self.assertTrue(form.is_valid())
    
    def test_no_email(self):
        """ Define a test for no email """
        self.formdata['email'] = ''
        form = SimpleCustomerCreationForm(self.formdata)
        self.assertFalse(form.is_valid())
    

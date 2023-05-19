#./crm_user/tests/forms/test_AdminCreationForm.py
#-------------------------------------------------------------
#-------------------------------------------------------------
# IMPORTS

from django.test import TestCase
from crm_user.forms import AdminCreationForm

#-------------------------------------------------------------
#-------------------------------------------------------------
# Create your Variables here.


#-------------------------------------------------------------
#-------------------------------------------------------------
# Create your Admin Creation Form tests here.

# Create a TestCase for Validating AdminCreationForm Fields
# crm_user.tests.forms.test_AdminCreationForm.FormValTests 
class FormValTests(TestCase):
    """ Define a TestCase for Validating AdminCreationForm Fields """
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
    
    def test_type_is_admin(self):
        """ Define a test to validate that type is always ADMIN """
        form = AdminCreationForm(self.formdata)
        self.assertTrue(form.is_valid())
        self.assertTrue(form.type == 'ADMIN')
    

#./crm_user/tests/forms/test_EmployeeCreationForm.py
#-------------------------------------------------------------
#-------------------------------------------------------------
# IMPORTS

from django.test import TestCase
from crm_user.forms import EmployeeCreationForm


#-------------------------------------------------------------
#-------------------------------------------------------------
# Create your Variables here.


#-------------------------------------------------------------
#-------------------------------------------------------------
# Create your Employee Creation Form tests here.

# Create a TestCase for Validating EmployeeCreationForm Fields
# crm_user.tests.forms.test_EmployeeCreationForm.FormValTests
class FormValTests(TestCase):
    """ Define a TestCase for Validating EmployeeCreationForm Fields """
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
    
    def test_type_is_employee(self):
        """ Define a test to validate that type is always EMPLOYEE """
        form = EmployeeCreationForm(self.formdata)
        self.assertTrue(form.is_valid())
        self.assertTrue(form.type == 'EMPLOYEE')
    

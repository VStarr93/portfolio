#./crm_user/tests/forms/test_SimpleEmployeeCreationForm.py
#-------------------------------------------------------------
#-------------------------------------------------------------
# IMPORTS

from django.test import TestCase, override_settings
from crm_user.forms import SimpleEmployeeCreationForm

#-------------------------------------------------------------
#-------------------------------------------------------------
# Create your Variables here.


#-------------------------------------------------------------
#-------------------------------------------------------------
# Create your Simple Employee Creation Form tests here.

# Create a TestCase for SimpleEmployeeCreationForm Required Fields
# crm_user.tests.forms.test_SimpleEmployeeCreationForm.FormReqTests 
class FormReqTests(TestCase):
    """ Define a TestCase for SimpleEmployeeCreationForm Required Fields """
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
        form = SimpleEmployeeCreationForm(self.formdata)
        self.assertTrue(form.is_valid())
    
    def test_no_first_name(self):
        """ Define a test for no first name """
        self.formdata['first_name'] = ''
        form = SimpleEmployeeCreationForm(self.formdata)
        self.assertTrue(form.is_valid())
    
    def test_no_middle_name(self):
        """ Define a test for no middle name """
        self.formdata['middle_name'] = ''
        form = SimpleEmployeeCreationForm(self.formdata)
        self.assertTrue(form.is_valid())
    
    def test_no_last_name(self):
        """ Define a test for no last_name """
        self.formdata['last_name'] = ''
        form = SimpleEmployeeCreationForm(self.formdata)
        self.assertTrue(form.is_valid())
    
    def test_no_email(self):
        """ Define a test for no email """
        self.formdata['email'] = ''
        form = SimpleEmployeeCreationForm(self.formdata)
        self.assertFalse(form.is_valid())
    
# Create a TestCase for SimpleEmployeeCreationForm Labels 
# crm_user.tests.forms.test_SimpleEmployeeCreationForm.FormLabelTests 
class FormLabelTests(TestCase):
    """ Define a TestCase for SimpleEmployeeCreationForm Labels """
    def setUp(self):
        """ FormLabel setUp method to create form data """
        self.formdata = {
            'first_name': 'Sara',
            'middle_name': 'Elizabeth',
            'last_name': 'Jackson',
            'email': 'test@example.com',
        }
    
    def test_simple_employee_field_first_name_label(self):
        """ Define a test for first_name field label """
        form = SimpleEmployeeCreationForm(self.formdata)
        self.assertTrue(form.fields['first_name'].label == 'First Name')
        
    def test_simple_employee_field_middle_name_label(self):
        """ Define a test for middle_name field label """
        form = SimpleEmployeeCreationForm(self.formdata)
        self.assertTrue(form.fields['middle_name'].label == 'Middle Name')
        
    def test_simple_employee_field_last_name_label(self):
        """ Define a test for last_name field label """
        form = SimpleEmployeeCreationForm(self.formdata)
        self.assertTrue(form.fields['last_name'].label == 'Last Name')
        
    def test_simple_employee_field_email_label(self):
        """ Define a test for email field label """
        form = SimpleEmployeeCreationForm(self.formdata)
        self.assertTrue(form.fields['email'].label == 'Email')
                 
# Create a TestCase for SimpleEmployeeCreationForm Help Text 
# crm_user.tests.forms.test_SimpleEmployeeCreationForm.FormHelpTests 
class FormHelpTests(TestCase):
    """ Define a TestCase for SimpleEmployeeCreationForm Help Text """
    def setUp(self):
        """ FormHelp setUp method to create form data """
        self.formdata = {
            'first_name': 'Sara',
            'middle_name': 'Elizabeth',
            'last_name': 'Jackson',
            'email': 'test@example.com',
        }
    
    def test_simple_employee_field_first_name_help_text(self):
        """ Define a test for first_name field help text """
        form = SimpleEmployeeCreationForm(self.formdata)
        self.assertTrue(form.fields['first_name'].help_text == 'Enter your first name')
        
    def test_simple_employee_field_middle_name_help_text(self):
        """ Define a test for middle_name field help text """
        form = SimpleEmployeeCreationForm(self.formdata)
        self.assertTrue(form.fields['middle_name'].help_text == 'Enter your middle name')
        
    def test_simple_employee_field_last_name_help_text(self):
        """ Define a test for last_name field help text """
        form = SimpleEmployeeCreationForm(self.formdata)
        self.assertTrue(form.fields['last_name'].help_text == 'Enter your last name')
        
    def test_simple_employee_field_email_help_text(self):
        """ Define a test for email field help text """
        form = SimpleEmployeeCreationForm(self.formdata)
        self.assertTrue(form.fields['email'].help_text == 'Enter your email address')
        
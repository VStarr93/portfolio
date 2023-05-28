#./crm_user/tests/forms/test_SimpleCustomerCreationForm.py
#-------------------------------------------------------------
#-------------------------------------------------------------
# IMPORTS

from django.test import TestCase
from crm_user.forms import SimpleCustomerCreationForm
from crm_user.models import Customer

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
    
# Create a TestCase for SimpleCustomerCreationForm Labels 
# crm_user.tests.forms.test_SimpleCustomerCreationForm.FormLabelTests 
class FormLabelTests(TestCase):
    """ Define a TestCase for SimpleCustomerCreationForm Labels """
    def setUp(self):
        """ FormLabel setUp method to create form data """
        self.formdata = {
            'first_name': 'Sara',
            'middle_name': 'Elizabeth',
            'last_name': 'Jackson',
            'email': 'test@example.com',
        }
    
    def test_simple_customer_field_first_name_label(self):
        """ Define a test for first_name field label """
        form = SimpleCustomerCreationForm(self.formdata)
        self.assertTrue(form.fields['first_name'].label == 'First Name')
        
    def test_simple_customer_field_middle_name_label(self):
        """ Define a test for middle_name field label """
        form = SimpleCustomerCreationForm(self.formdata)
        self.assertTrue(form.fields['middle_name'].label == 'Middle Name')
        
    def test_simple_customer_field_last_name_label(self):
        """ Define a test for last_name field label """
        form = SimpleCustomerCreationForm(self.formdata)
        self.assertTrue(form.fields['last_name'].label == 'Last Name')
        
    def test_simple_customer_field_email_label(self):
        """ Define a test for email field label """
        form = SimpleCustomerCreationForm(self.formdata)
        self.assertTrue(form.fields['email'].label == 'Email')
    
# Create a TestCase for SimpleCustomerCreationForm Help Text 
# crm_user.tests.forms.test_SimpleCustomerCreationForm.FormHelpTests 
class FormHelpTests(TestCase):
    """ Define a TestCase for SimpleCustomerCreationForm Help Text """
    def setUp(self):
        """ FormHelp setUp method to create form data """
        self.formdata = {
            'first_name': 'Sara',
            'middle_name': 'Elizabeth',
            'last_name': 'Jackson',
            'email': 'test@example.com',
        }
    
    def test_simple_customize_field_first_name_help_text(self):
        """ Define a test for first_name field help text """
        form = SimpleCustomerCreationForm(self.formdata)
        self.assertTrue(form.fields['first_name'].help_text == 'Enter your first name')
        
    def test_simple_customize_field_middle_name_help_text(self):
        """ Define a test for middle_name field help text """
        form = SimpleCustomerCreationForm(self.formdata)
        self.assertTrue(form.fields['middle_name'].help_text == 'Enter your middle name')
        
    def test_simple_customize_field_last_name_help_text(self):
        """ Define a test for last_name field help text """
        form = SimpleCustomerCreationForm(self.formdata)
        self.assertTrue(form.fields['last_name'].help_text == 'Enter your last name')
        
    def test_simple_customize_field_email_help_text(self):
        """ Define a test for email field help text """
        form = SimpleCustomerCreationForm(self.formdata)
        self.assertTrue(form.fields['email'].help_text == 'Enter your email address')
        
# Create a TestCase for SimpleCustomerCreationForm Methods
# crm_user.tests.forms.test_SimpleCustomerCreationForm.MethodTests
class MethodTests(TestCase):
    """ Define a TestCase for SimpleCustomerCreationForm Methods """
    def setUp(self):
        """ MethodTests setUp method to create form data """
        self.formdata = {
            'first_name': 'Sara',
            'middle_name': 'Elizabeth',
            'last_name': 'Jackson',
            'email': 'test@example.com',
        }
    
    def test_save_method(self):
        """ Test that SimpleCustomerCreationForm will create an Customer instance upon saving. """
        form = SimpleCustomerCreationForm(self.formdata)
        self.assertEqual(form.is_valid(), True)
        form.save()
        self.assertEqual(Customer.objects.filter(first_name=self.formdata['first_name']).exists(), True)
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
    
# Create a TestCase for AdminCreationForm Required Fields
# crm_user.tests.forms.test_AdminCreationForm.FormReqTests 
class FormReqTests(TestCase):
    """ Define a TestCase for AdminCreationForm Required Fields """
    def setUp(self):
        """ FormReq setUp method to create form data """
        self.formdata = {
            'first_name': 'Sara',
            'middle_name': 'Elizabeth',
            'last_name': 'Jackson',
            'email': 'test@example.com',
            'password1': 'T3st3x@mpl3',
            'password2': 'T3st3x@mpl3'
        }
    
    def test_valid_data(self):
        """ Define a test for valid data """
        form = AdminCreationForm(self.formdata)
        self.assertTrue(form.is_valid())
    
    def test_no_first_name(self):
        """ Define a test for no first name """
        self.formdata['first_name'] = ''
        form = AdminCreationForm(self.formdata)
        self.assertTrue(form.is_valid())
    
    def test_no_middle_name(self):
        """ Define a test for no middle name """
        self.formdata['middle_name'] = ''
        form = AdminCreationForm(self.formdata)
        self.assertTrue(form.is_valid())
    
    def test_no_last_name(self):
        """ Define a test for no last_name """
        self.formdata['last_name'] = ''
        form = AdminCreationForm(self.formdata)
        self.assertTrue(form.is_valid())
    
    def test_no_email(self):
        """ Define a test for no email """
        self.formdata['email'] = ''
        form = AdminCreationForm(self.formdata)
        self.assertFalse(form.is_valid())
    
    def test_no_password1(self):
        """ Define a test for no password1 """
        self.formdata['password1'] = ''
        form = AdminCreationForm(self.formdata)
        self.assertFalse(form.is_valid())
    
    def test_no_password2(self):
        """ Define a test for no password2 """
        self.formdata['password2'] = ''
        form = AdminCreationForm(self.formdata)
        self.assertFalse(form.is_valid())
    
    def test_no_password(self):
        """ Define a test for no password """
        self.formdata['password1'] = ''
        self.formdata['password2'] = ''
        form = AdminCreationForm(self.formdata)
        self.assertFalse(form.is_valid())
    
# Create a TestCase for AdminCreationForm Labels 
# crm_user.tests.forms.test_AdminCreationForm.FormLabelTests 
class FormLabelTests(TestCase):
    """ Define a TestCase for AdminCreationForm Labels """
    def setUp(self):
        """ FormLabel setUp method to create form data """
        self.formdata = {
            'first_name': 'Sara',
            'middle_name': 'Elizabeth',
            'last_name': 'Jackson',
            'email': 'test@example.com',
            'password1': 'T3st3x@mpl3',
            'password2': 'T3st3x@mpl3'
        }
    
    def test_admin_field_first_name_label(self):
        """ Define a test for first_name field label """
        form = AdminCreationForm(self.formdata)
        self.assertTrue(form.fields['first_name'].label == 'First Name')
        
    def test_admin_field_middle_name_label(self):
        """ Define a test for middle_name field label """
        form = AdminCreationForm(self.formdata)
        self.assertTrue(form.fields['middle_name'].label == 'Middle Name')
        
    def test_admin_field_last_name_label(self):
        """ Define a test for last_name field label """
        form = AdminCreationForm(self.formdata)
        self.assertTrue(form.fields['last_name'].label == 'Last Name')
        
    def test_admin_field_email_label(self):
        """ Define a test for email field label """
        form = AdminCreationForm(self.formdata)
        self.assertTrue(form.fields['email'].label == 'Email')
        
    def test_admin_field_password1_label(self):
        """ Define a test for password1 field label """
        form = AdminCreationForm(self.formdata)
        self.assertTrue(form.fields['password1'].label == 'Password')
        
    def test_admin_field_password2_label(self):
        """ Define a test for password2 field label """
        form = AdminCreationForm(self.formdata)
        self.assertTrue(form.fields['password2'].label == 'Password confirmation')
              

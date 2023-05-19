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
    
# Create a TestCase for CustomUserCreationForm Labels 
# crm_user.tests.forms.test_CustomUserCreationForm.FormLabelTests 
class FormLabelTests(TestCase):
    """ Define a TestCase for CustomUserCreationForm Labels """
    def setUp(self):
        """ FormLabel setUp method to create form data """
        self.formdata = {
            'first_name': 'Sara',
            'middle_name': 'Elizabeth',
            'last_name': 'Jackson',
            'type': 'CUSTOMER',
            'email': 'test@example.com',
            'password1': 'T3st3x@mpl3',
            'password2': 'T3st3x@mpl3'
        }
    
    def test_user_field_first_name_label(self):
        """ Define a test for first_name field label """
        form = CustomUserCreationForm(self.formdata)
        self.assertTrue(form.fields['first_name'].label == 'First Name')
        
    def test_user_field_middle_name_label(self):
        """ Define a test for middle_name field label """
        form = CustomUserCreationForm(self.formdata)
        self.assertTrue(form.fields['middle_name'].label == 'Middle Name')
        
    def test_user_field_last_name_label(self):
        """ Define a test for last_name field label """
        form = CustomUserCreationForm(self.formdata)
        self.assertTrue(form.fields['last_name'].label == 'Last Name')
        
    def test_user_field_type_label(self):
        """ Define a test for type field label """
        form = CustomUserCreationForm(self.formdata)
        self.assertTrue(form.fields['type'].label == 'Type')
        
    def test_user_field_email_label(self):
        """ Define a test for email field label """
        form = CustomUserCreationForm(self.formdata)
        self.assertTrue(form.fields['email'].label == 'Email')
        
    def test_user_field_password1_label(self):
        """ Define a test for password1 field label """
        form = CustomUserCreationForm(self.formdata)
        self.assertTrue(form.fields['password1'].label == 'Password')
        
    def test_user_field_password2_label(self):
        """ Define a test for password2 field label """
        form = CustomUserCreationForm(self.formdata)
        self.assertTrue(form.fields['password2'].label == 'Password confirmation')
              
# Create a TestCase for CustomUserCreationForm Help Text 
# crm_user.tests.forms.test_CustomUserCreationForm.FormHelpTests 
class FormHelpTests(TestCase):
    """ Define a TestCase for CustomUserCreationForm Help Text """
    def setUp(self):
        """ FormHelp setUp method to create form data """
        self.formdata = {
            'first_name': 'Sara',
            'middle_name': 'Elizabeth',
            'last_name': 'Jackson',
            'type': 'CUSTOMER',
            'email': 'test@example.com',
            'password1': 'T3st3x@mpl3',
            'password2': 'T3st3x@mpl3'
        }
    
    def test_user_field_first_name_help_text(self):
        """ Define a test for first_name field help text """
        form = CustomUserCreationForm(self.formdata)
        self.assertTrue(form.fields['first_name'].help_text == 'Enter your first name')
        
    def test_user_field_middle_name_help_text(self):
        """ Define a test for middle_name field help text """
        form = CustomUserCreationForm(self.formdata)
        self.assertTrue(form.fields['middle_name'].help_text == 'Enter your middle name')
        
    def test_user_field_last_name_help_text(self):
        """ Define a test for last_name field help text """
        form = CustomUserCreationForm(self.formdata)
        self.assertTrue(form.fields['last_name'].help_text == 'Enter your last name')
        
    def test_user_field_type_help_text(self):
        """ Define a test for type field help text """
        form = CustomUserCreationForm(self.formdata)
        self.assertTrue(form.fields['type'].help_text == 'Select the user type')
        
    def test_user_field_email_help_text(self):
        """ Define a test for email field help text """
        form = CustomUserCreationForm(self.formdata)
        self.assertTrue(form.fields['email'].help_text == 'Enter your email address')
        
    def test_user_field_password1_help_text(self):
        """ Define a test for password1 field help text """
        form = CustomUserCreationForm(self.formdata)
        self.assertTrue(form.fields['password1'].help_text == '<ul><li>Your password can’t be too similar to your other personal information.</li><li>Your password must contain at least 8 characters.</li><li>Your password can’t be a commonly used password.</li><li>Your password can’t be entirely numeric.</li></ul>')
        
    def test_user_field_password2_help_text(self):
        """ Define a test for password2 field help text """
        form = CustomUserCreationForm(self.formdata)
        self.assertTrue(form.fields['password2'].help_text == 'Enter the same password as before, for verification.')

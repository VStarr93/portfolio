#./crm_user/tests/forms/test_AdminCustomizeForm.py
#-------------------------------------------------------------
#-------------------------------------------------------------
# IMPORTS

from django.test import TestCase
from crm_user.forms import AdminCustomizeForm
from crm_user.models import User, Admin, AdminProfile
from django.core.exceptions import ValidationError 
import datetime 
from parameterized import parameterized

# For Testing Email Services
from django.core import mail 


#-------------------------------------------------------------
#-------------------------------------------------------------
# Create your Variables here.


#-------------------------------------------------------------
#-------------------------------------------------------------
# Create your Admin Customize Form tests here.

# Create a TestCase for AdminCustomizeForm Choices Field
# crm_user.tests.forms.test_AdminCustomizeForm.FormChoiceTests 
class FormChoiceTests(TestCase):
    """ Define a TestCase for AdminCustomizeForm Choice Fields """
    def setUp(self):
        """ FormReq setUp method to create form data """
        self.formdata = {
            'language': 'ENGLISH',
            'theme': 'GREEN',
        }

    @parameterized.expand([
        ('ENGLISH'),
        ('SPANISH'),
        ('MANDARIN'),
        ('HINDI'),
        ('FRENCH'),
        ('ARABIC'),
        ('RUSSIAN'),
        ('PORTUGUESE'),
    ])
    def test_valid_language_choices(self, a):
        """ Define a test for valid lanuage choices """
        self.formdata['language'] = a
        form = AdminCustomizeForm(self.formdata)
        self.assertTrue(form.is_valid())
        
    def test_invalid_language_choices(self):
        """ Define a test for invalid language choices """
        self.formdata['language'] = 'LANGUAGE'
        form = AdminCustomizeForm(self.formdata)
        self.assertFalse(form.is_valid())

    @parameterized.expand([
        ('RED'),
        ('BLUE'),
        ('GREEN'),
        ('YELLOW'),
        ('ORANGE'),
        ('PURPLE'),
        ('BLACK'),
        ('WHITE'),
    ])
    def test_valid_theme_choices(self, a):
        """ Define a test for valid theme choices """
        self.formdata['theme'] = a
        form = AdminCustomizeForm(self.formdata)
        self.assertTrue(form.is_valid())
        
    def test_invalid_theme_choices(self):
        """ Define a test for invalid theme choices """
        self.formdata['theme'] = 'LAVENDER'
        form = AdminCustomizeForm(self.formdata)
        self.assertFalse(form.is_valid())
        
# Create a TestCase for AdminCustomizeForm Required Fields
# crm_user.tests.forms.test_AdminCustomizeForm.FormReqTests 
class FormReqTests(TestCase):
    """ Define a TestCase for AdminCustomizeForm Required Fields """
    def setUp(self):
        """ FormReq setUp method to create form data """
        self.formdata = {
            'language': 'ENGLISH',
            'theme': 'GREEN',
        }

    def test_valid_data(self):
        """ Define a test for valid data """
        form = AdminCustomizeForm(self.formdata)
        self.assertTrue(form.is_valid())

    def test_no_language(self):
        """ Define a test for no language """
        self.formdata['language'] = ''
        form = AdminCustomizeForm(self.formdata)
        self.assertFalse(form.is_valid())

    def test_no_theme(self):
        """ Define a test for no theme """
        self.formdata['theme'] = ''
        form = AdminCustomizeForm(self.formdata)
        self.assertFalse(form.is_valid())
        
# Create a TestCase for AdminCustomizeForm Labels 
# crm_user.tests.forms.test_AdminCustomizeForm.FormLabelTests 
class FormLabelTests(TestCase):
    """ Define a TestCase for AdminCustomizeForm Labels """
    def setUp(self):
        """ FormLabel setUp method to create form data """
        self.formdata = {
            'language': 'ENGLISH',
            'theme': 'GREEN',
        }
    
    def test_customize_field_language_label(self):
        """ Define a test for language field label """
        form = AdminCustomizeForm(self.formdata)
        self.assertTrue(form.fields['language'].label == 'Language')
        
    def test_customize_field_theme_label(self):
        """ Define a test for theme field label """
        form = AdminCustomizeForm(self.formdata)
        self.assertTrue(form.fields['theme'].label == 'Theme')
        
# Create a TestCase for AdminCustomizeForm Help Text 
# crm_user.tests.forms.test_AdminCustomizeForm.FormHelpTests 
class FormHelpTests(TestCase):
    """ Define a TestCase for AdminCreationForm Help Text """
    def setUp(self):
        """ FormHelp setUp method to create form data """
        self.formdata = {
            'first_name': 'Sara',
            'middle_name': 'Elizabeth',
            'last_name': 'Jackson',
            'email': 'test@example.com',
            'password1': 'T3st3x@mpl3',
            'password2': 'T3st3x@mpl3'
        }
    
    def test_customize_field_language_help_text(self):
        """ Define a test for language field help text """
        form = AdminCustomizeForm(self.formdata)
        self.assertTrue(form.fields['language'].help_text == 'What language do you speak?')
        
    def test_customize_field_theme_help_text(self):
        """ Define a test for theme field help text """
        form = AdminCustomizeForm(self.formdata)
        self.assertTrue(form.fields['theme'].help_text == 'Choose a theme to use.')
        
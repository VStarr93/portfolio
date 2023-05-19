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
        

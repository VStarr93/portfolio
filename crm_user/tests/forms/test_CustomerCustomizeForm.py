#./crm_user/tests/forms/test_CustomerCustomizeForm.py
#-------------------------------------------------------------
#-------------------------------------------------------------
# IMPORTS

from django.test import TestCase, override_settings
from crm_user.forms import CustomerCustomizeForm

from parameterized import parameterized

#-------------------------------------------------------------
#-------------------------------------------------------------
# Create your Variables here.


#-------------------------------------------------------------
#-------------------------------------------------------------
# Create your Customer Customize Form tests here.

# Create a TestCase for CustomerCustomizeForm Choices Field
# crm_user.tests.forms.test_CustomerCustomizeForm.FormChoiceTests 
class FormChoiceTests(TestCase):
    """ Define a TestCase for CustomerCustomizeForm Choice Fields """
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
        form = CustomerCustomizeForm(self.formdata)
        self.assertTrue(form.is_valid())
        
    def test_invalid_language_choices(self):
        """ Define a test for invalid language choices """
        self.formdata['language'] = 'LANGUAGE'
        form = CustomerCustomizeForm(self.formdata)
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
        form = CustomerCustomizeForm(self.formdata)
        self.assertTrue(form.is_valid())
        
    def test_invalid_theme_choices(self):
        """ Define a test for invalid theme choices """
        self.formdata['theme'] = 'LAVENDER'
        form = CustomerCustomizeForm(self.formdata)
        self.assertFalse(form.is_valid())
        
# Create a TestCase for CustomerCustomizeForm Required Fields
# crm_user.tests.forms.test_CustomerCustomizeForm.FormReqTests 
class FormReqTests(TestCase):
    """ Define a TestCase for CustomerCustomizeForm Required Fields """
    def setUp(self):
        """ FormReq setUp method to create form data """
        self.formdata = {
            'language': 'ENGLISH',
            'theme': 'GREEN',
        }

    def test_valid_data(self):
        """ Define a test for valid data """
        form = CustomerCustomizeForm(self.formdata)
        self.assertTrue(form.is_valid())

    def test_no_language(self):
        """ Define a test for no language """
        self.formdata['language'] = ''
        form = CustomerCustomizeForm(self.formdata)
        self.assertFalse(form.is_valid())

    def test_no_theme(self):
        """ Define a test for no theme """
        self.formdata['theme'] = ''
        form = CustomerCustomizeForm(self.formdata)
        self.assertFalse(form.is_valid())
        
# Create a TestCase for CustomerCustomizeForm Labels 
# crm_user.tests.forms.test_CustomerCustomizeForm.FormLabelTests 
class FormLabelTests(TestCase):
    """ Define a TestCase for CustomerCustomizeForm Labels """
    def setUp(self):
        """ FormLabel setUp method to create form data """
        self.formdata = {
            'language': 'ENGLISH',
            'theme': 'GREEN',
        }
    
    def test_customize_field_language_label(self):
        """ Define a test for language field label """
        form = CustomerCustomizeForm(self.formdata)
        self.assertTrue(form.fields['language'].label == 'Language')
        
    def test_customize_field_theme_label(self):
        """ Define a test for theme field label """
        form = CustomerCustomizeForm(self.formdata)
        self.assertTrue(form.fields['theme'].label == 'Theme')
        

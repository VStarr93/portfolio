#./crm_user/tests/models/test_CustomerProfileModel.py
#-------------------------------------------------------------
#-------------------------------------------------------------
# IMPORTS

from django.test import TestCase
from crm_user.models import Customer, CustomerProfile
from django.db.models.fields import NOT_PROVIDED

# For Testing Email Services
from django.core import mail 

#-------------------------------------------------------------
#-------------------------------------------------------------
# Create your Variables here.


#-------------------------------------------------------------
#-------------------------------------------------------------
# Create your CustomerProfile Model tests here.

# Create a TestCase for Customer Profile Labels
# crm_user.tests.models.test_CustomerProfileModel.LabelTests
class LabelTests(TestCase):
    """ Define a TestCase for Customer Profile Model Labels """
    @classmethod 
    def setUpTestData(cls):
        """ Define setUpTestData method for Customer Profile Model Labels """
        Customer.objects.create_user(
            email="doe@example.com",
            first_name="Sara",
            middle_name="Lee",
            last_name="Doe",
            birth_date='1993-04-14',
            phone_number="+12125556789",
        )
        
    def setUp(self):
        """ Define setUp method for Customer Profile Model Labels """
        self.user = CustomerProfile.objects.get(id=1)
        
    def test_id_label(self):
        """ Test for Customer Profile Model ID Label """
        field_label = self.user._meta.get_field('id').verbose_name 
        self.assertEqual(field_label, 'ID')
        
    def test_acct_no_label(self):
        """ Test for Customer Profile Model Account Number Label """
        field_label = self.user._meta.get_field('acct_no').verbose_name 
        self.assertEqual(field_label, 'Account Number')
        
    def test_status_label(self):
        """ Test for Customer Profile Model Status Label """
        field_label = self.user._meta.get_field('status').verbose_name
        self.assertEqual(field_label, 'Status')
        
    def test_user_label(self):
        """ Test for Customer Profile Model User Label """
        field_label = self.user._meta.get_field('user').verbose_name 
        self.assertEqual(field_label, 'Customer')

    def test_last_job_label(self):
        """ Test for Customer Profile Model Last Job Label """
        field_label = self.user._meta.get_field('last_job').verbose_name 
        self.assertEqual(field_label, 'Last Job')

    def test_language_label(self):
        """ Test for Customer Profile Model Language Label """
        field_label = self.user._meta.get_field('language').verbose_name 
        self.assertEqual(field_label, 'Language')
        
    def test_theme_label(self):
        """ Test for Customer Profile Model Theme Label """
        field_label = self.user._meta.get_field('theme').verbose_name
        self.assertEqual(field_label, 'Theme')
        
    def test_balance_owed_label(self):
        """ Test for Customer Profile Model Balance Owed Label """
        field_label = self.user._meta.get_field('balance_owed').verbose_name 
        self.assertEqual(field_label, 'Balance Owed')
        
    def test_credit_owed_label(self):
        """ Test for Customer Profile Model Credit Owed Label """
        field_label = self.user._meta.get_field('credit_owed').verbose_name 
        self.assertEqual(field_label, 'Credit Owed')
        
# Create a TestCase for Customer Profile Max Lengths
# crm_user.tests.models.test_CustomerProfileModel.MaxLengthTests
class MaxLengthTests(TestCase):
    """ Define a TestCase for Customer Profile Model Max Lengths """
    @classmethod 
    def setUpTestData(cls):
        """ Define setUpTestData method for Customer Profile Model Max Lengths """
        Customer.objects.create_user(
            email="doe@example.com",
            first_name="Sara",
            middle_name="Lee",
            last_name="Doe",
            birth_date='1993-04-14',
            phone_number="+12125556789",
        )
        
    def setUp(self):
        """ Define setUp method for Customer Profile Model Max Lengths """
        self.user = CustomerProfile.objects.get(id=1)
        
    def test_id_max_length(self):
        """ Test for Customer Profile Model ID Max Length """
        max_length = self.user._meta.get_field('id').max_length 
        self.assertEqual(max_length, None)
        
    def test_acct_no_max_length(self):
        """ Test for Customer Profile Model Account Number Max Length """
        max_length = self.user._meta.get_field('acct_no').max_length 
        self.assertEqual(max_length, 10)
        
    def test_status_max_length(self):
        """ Test for Customer Profile Model Status Max Length """
        max_length = self.user._meta.get_field('status').max_length
        self.assertEqual(max_length, 9)
        
    def test_user_max_length(self):
        """ Test for Customer Profile Model User Max Length """
        max_length = self.user._meta.get_field('user').max_length 
        self.assertEqual(max_length, None)

    def test_last_job_max_length(self):
        """ Test for Customer Profile Model Last Job Max Length """
        max_length = self.user._meta.get_field('last_job').max_length 
        self.assertEqual(max_length, None)

    def test_language_max_length(self):
        """ Test for Customer Profile Model Language Max Length """
        max_length = self.user._meta.get_field('language').max_length 
        self.assertEqual(max_length, 10)
        
    def test_theme_max_length(self):
        """ Test for Customer Profile Model Theme Max Length """
        max_length = self.user._meta.get_field('theme').max_length
        self.assertEqual(max_length, 6)
        
    def test_balance_owed_max_length(self):
        """ Test for Customer Profile Model Balance Owed Max Length """
        max_length = self.user._meta.get_field('balance_owed').max_length
        self.assertEqual(max_length, None)
        
    def test_credit_owed_max_length(self):
        """ Test for Customer Profile Model Credit Owed Max Length """
        max_length = self.user._meta.get_field('credit_owed').max_length
        self.assertEqual(max_length, None)
        
# Create a TestCase for Customer Profile Help Text
# crm_user.tests.models.test_CustomerProfileModel.HelpTextTests
class HelpTextTests(TestCase):
    """ Define a TestCase for Customer Profile Model Help Text """
    @classmethod 
    def setUpTestData(cls):
        """ Define setUpTestData method for Customer Profile Model Help Text """
        Customer.objects.create_user(
            email="doe@example.com",
            first_name="Sara",
            middle_name="Lee",
            last_name="Doe",
            birth_date='1993-04-14',
            phone_number="+12125556789",
        )
        
    def setUp(self):
        """ Define setUp method for Customer Profile Model Help Text """
        self.user = CustomerProfile.objects.get(id=1)
        
    def test_id_help_text(self):
        """ Test for Customer Profile Model ID Help Text """
        help_text = self.user._meta.get_field('id').help_text 
        self.assertEqual(help_text, '')
        
    def test_acct_no_help_text(self):
        """ Test for Customer Profile Model Account Number Help Text """
        help_text = self.user._meta.get_field('acct_no').help_text 
        self.assertEqual(help_text, "Your customer account number is auto-generated and cannot be changed.")
        
    def test_status_help_text(self):
        """ Test for Customer Profile Model Status Help Text """
        help_text = self.user._meta.get_field('status').help_text
        self.assertEqual(help_text, "Your customer status is adjusted based on frequency of jobs.")
        
    def test_user_help_text(self):
        """ Test for Customer Profile Model User Help Text """
        help_text = self.user._meta.get_field('user').help_text 
        self.assertEqual(help_text, "The Customer these details/model are associated with.")

    def test_last_job_help_text(self):
        """ Test for Customer Profile Model Last Job Help Text """
        help_text = self.user._meta.get_field('last_job').help_text 
        self.assertEqual(help_text, "The date of which the last job for customer was performed.")

    def test_language_help_text(self):
        """ Test for Customer Profile Model Language Help Text """
        help_text = self.user._meta.get_field('language').help_text 
        self.assertEqual(help_text, "What language do you speak?")
        
    def test_theme_help_text(self):
        """ Test for Customer Profile Model Theme Help Text """
        help_text = self.user._meta.get_field('theme').help_text
        self.assertEqual(help_text, "Choose a theme to use.")
        
    def test_balance_owed_help_text(self):
        """ Test For Customer Profile Model Balance Owed Help Text """
        help_text = self.user._meta.get_field('balance_owed').help_text
        self.assertEqual(help_text, "The status of the customer's account balance.")
         
    def test_credit_owed_help_text(self):
        """ Test For Customer Profile Model Credit Owed Help Text """
        help_text = self.user._meta.get_field('credit_owed').help_text
        self.assertEqual(help_text, "The status of the customer's account credit.")
        

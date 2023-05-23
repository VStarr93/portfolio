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
        

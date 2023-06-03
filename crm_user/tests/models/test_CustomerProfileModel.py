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
        self.user = Customer.objects.get(email="doe@example.com")
        self.profile = CustomerProfile.objects.get(user=self.user)
        
    def test_id_label(self):
        """ Test for Customer Profile Model ID Label """
        field_label = self.profile._meta.get_field('id').verbose_name 
        self.assertEqual(field_label, 'ID')
        
    def test_acct_no_label(self):
        """ Test for Customer Profile Model Account Number Label """
        field_label = self.profile._meta.get_field('acct_no').verbose_name 
        self.assertEqual(field_label, 'Account Number')
        
    def test_status_label(self):
        """ Test for Customer Profile Model Status Label """
        field_label = self.profile._meta.get_field('status').verbose_name
        self.assertEqual(field_label, 'Status')
        
    def test_user_label(self):
        """ Test for Customer Profile Model User Label """
        field_label = self.profile._meta.get_field('user').verbose_name 
        self.assertEqual(field_label, 'Customer')

    def test_last_job_label(self):
        """ Test for Customer Profile Model Last Job Label """
        field_label = self.profile._meta.get_field('last_job').verbose_name 
        self.assertEqual(field_label, 'Last Job')

    def test_language_label(self):
        """ Test for Customer Profile Model Language Label """
        field_label = self.profile._meta.get_field('language').verbose_name 
        self.assertEqual(field_label, 'Language')
        
    def test_theme_label(self):
        """ Test for Customer Profile Model Theme Label """
        field_label = self.profile._meta.get_field('theme').verbose_name
        self.assertEqual(field_label, 'Theme')
        
    def test_balance_owed_label(self):
        """ Test for Customer Profile Model Balance Owed Label """
        field_label = self.profile._meta.get_field('balance_owed').verbose_name 
        self.assertEqual(field_label, 'Balance Owed')
        
    def test_credit_owed_label(self):
        """ Test for Customer Profile Model Credit Owed Label """
        field_label = self.profile._meta.get_field('credit_owed').verbose_name 
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
        self.user = Customer.objects.get(email="doe@example.com")
        self.profile = CustomerProfile.objects.get(user=self.user)
        
    def test_id_max_length(self):
        """ Test for Customer Profile Model ID Max Length """
        max_length = self.profile._meta.get_field('id').max_length 
        self.assertEqual(max_length, None)
        
    def test_acct_no_max_length(self):
        """ Test for Customer Profile Model Account Number Max Length """
        max_length = self.profile._meta.get_field('acct_no').max_length 
        self.assertEqual(max_length, 10)
        
    def test_status_max_length(self):
        """ Test for Customer Profile Model Status Max Length """
        max_length = self.profile._meta.get_field('status').max_length
        self.assertEqual(max_length, 9)
        
    def test_user_max_length(self):
        """ Test for Customer Profile Model User Max Length """
        max_length = self.profile._meta.get_field('user').max_length 
        self.assertEqual(max_length, None)

    def test_last_job_max_length(self):
        """ Test for Customer Profile Model Last Job Max Length """
        max_length = self.profile._meta.get_field('last_job').max_length 
        self.assertEqual(max_length, None)

    def test_language_max_length(self):
        """ Test for Customer Profile Model Language Max Length """
        max_length = self.profile._meta.get_field('language').max_length 
        self.assertEqual(max_length, 10)
        
    def test_theme_max_length(self):
        """ Test for Customer Profile Model Theme Max Length """
        max_length = self.profile._meta.get_field('theme').max_length
        self.assertEqual(max_length, 6)
        
    def test_balance_owed_max_length(self):
        """ Test for Customer Profile Model Balance Owed Max Length """
        max_length = self.profile._meta.get_field('balance_owed').max_length
        self.assertEqual(max_length, None)
        
    def test_credit_owed_max_length(self):
        """ Test for Customer Profile Model Credit Owed Max Length """
        max_length = self.profile._meta.get_field('credit_owed').max_length
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
        self.user = Customer.objects.get(email="doe@example.com")
        self.profile = CustomerProfile.objects.get(user=self.user)
        
    def test_id_help_text(self):
        """ Test for Customer Profile Model ID Help Text """
        help_text = self.profile._meta.get_field('id').help_text 
        self.assertEqual(help_text, '')
        
    def test_acct_no_help_text(self):
        """ Test for Customer Profile Model Account Number Help Text """
        help_text = self.profile._meta.get_field('acct_no').help_text 
        self.assertEqual(help_text, "Your customer account number is auto-generated and cannot be changed.")
        
    def test_status_help_text(self):
        """ Test for Customer Profile Model Status Help Text """
        help_text = self.profile._meta.get_field('status').help_text
        self.assertEqual(help_text, "Your customer status is adjusted based on frequency of jobs.")
        
    def test_user_help_text(self):
        """ Test for Customer Profile Model User Help Text """
        help_text = self.profile._meta.get_field('user').help_text 
        self.assertEqual(help_text, "The Customer these details/model are associated with.")

    def test_last_job_help_text(self):
        """ Test for Customer Profile Model Last Job Help Text """
        help_text = self.profile._meta.get_field('last_job').help_text 
        self.assertEqual(help_text, "The date of which the last job for customer was performed.")

    def test_language_help_text(self):
        """ Test for Customer Profile Model Language Help Text """
        help_text = self.profile._meta.get_field('language').help_text 
        self.assertEqual(help_text, "What language do you speak?")
        
    def test_theme_help_text(self):
        """ Test for Customer Profile Model Theme Help Text """
        help_text = self.profile._meta.get_field('theme').help_text
        self.assertEqual(help_text, "Choose a theme to use.")
        
    def test_balance_owed_help_text(self):
        """ Test For Customer Profile Model Balance Owed Help Text """
        help_text = self.profile._meta.get_field('balance_owed').help_text
        self.assertEqual(help_text, "The status of the customer's account balance.")
         
    def test_credit_owed_help_text(self):
        """ Test For Customer Profile Model Credit Owed Help Text """
        help_text = self.profile._meta.get_field('credit_owed').help_text
        self.assertEqual(help_text, "The status of the customer's account credit.")
        
# Create a TestCase for Customer Profile Required Fields
# crm_user.tests.models.test_CustomerProfileModel.ReqTests
class ReqTests(TestCase):
    """ Define a TestCase for Customer Profile Model Required Fields"""
    @classmethod 
    def setUpTestData(cls):
        """ Define setUpTestData method for Customer Profile Model Required Fields """
        Customer.objects.create_user(
            email="doe@example.com",
            first_name="Sara",
            middle_name="Lee",
            last_name="Doe",
            birth_date='1993-04-14',
            phone_number="+12125556789",
        )
        
    def setUp(self):
        """ Define setUp method for Customer Profile Model Required Fields """
        self.user = Customer.objects.get(email="doe@example.com")
        self.profile = CustomerProfile.objects.get(user=self.user)
        
    def test_id_required(self):
        """ Test that Customer Profile Model ID is not required """
        blank = self.profile._meta.get_field('id').blank 
        null = self.profile._meta.get_field('id').null  
        self.assertEqual(blank, True)
        self.assertEqual(null, False)
        
    def test_acct_no_required(self):
        """ Test that Customer Profile Model Account Number is required """
        blank = self.profile._meta.get_field('acct_no').blank 
        null = self.profile._meta.get_field('acct_no').null 
        self.assertEqual(blank, False)
        self.assertEqual(null, False)
        
    def test_status_required(self):
        """ Test that Customer Profile Model Status is required """
        blank = self.profile._meta.get_field('status').blank
        null = self.profile._meta.get_field('status').null
        self.assertEqual(blank, False)
        self.assertEqual(null, False)
        
    def test_user_required(self):
        """ Test that Customer Profile Model User is required """
        blank = self.profile._meta.get_field('user').blank 
        null = self.profile._meta.get_field('user').null 
        self.assertEqual(blank, False)
        self.assertEqual(null, False)

    def test_last_job_required(self):
        """ Test that Customer Profile Model Last Job is not required """
        blank = self.profile._meta.get_field('last_job').blank 
        null = self.profile._meta.get_field('last_job').null 
        self.assertEqual(blank, True)
        self.assertEqual(null, True)

    def test_language_required(self):
        """ Test that Customer Profile Model Language is required """
        blank = self.profile._meta.get_field('language').blank 
        null = self.profile._meta.get_field('language').null 
        self.assertEqual(blank, False)
        self.assertEqual(null, False)
        
    def test_theme_required(self):
        """ Test that Customer Profile Model Theme is required """
        blank = self.profile._meta.get_field('theme').blank
        null = self.profile._meta.get_field('theme').null
        self.assertEqual(blank, False)
        self.assertEqual(null, False)

    def test_balance_owed_required(self):
        """ Test that Customer Profile Model Balance Owed is required """
        blank = self.profile._meta.get_field('balance_owed').blank 
        null = self.profile._meta.get_field('balance_owed').null 
        self.assertEqual(blank, False)
        self.assertEqual(null, False)
        
    def test_credit_owed_required(self):
        """ Test that Customer Profile Model Credit Owed is not required """
        blank = self.profile._meta.get_field('credit_owed').blank
        null = self.profile._meta.get_field('credit_owed').null
        self.assertEqual(blank, False)
        self.assertEqual(null, False)
    
# Create a TestCase for Customer Profile Defaults
# crm_user.tests.models.test_CustomerProfileModel.DefaultTests
class DefaultTests(TestCase):
    """ Define a Testcase for Customer Profile Model Defaults """
    @classmethod 
    def setUpTestData(cls):
        """ Define setUpTestData method for Customer Profile Model Defaults """
        Customer.objects.create_user(
            email="doe@example.com",
            first_name="Sara",
            middle_name="Lee",
            last_name="Doe",
            birth_date='1993-04-14',
            phone_number="+12125556789",
        )
        
    def setUp(self):
        """ Define setUp method for Customer Profile Model Defaults """
        self.user = Customer.objects.get(email="doe@example.com")
        self.profile = CustomerProfile.objects.get(user=self.user)
        
    def test_id_default(self):
        """ Test that Customer Profile Model ID has no default values """
        default = self.profile._meta.get_field('id').default 
        self.assertEqual(default, NOT_PROVIDED)
        
    def test_acct_no_default(self):
        """ Test that Customer Profile Model Account Number has a default value """
        default = self.profile._meta.get_field('acct_no').default 
        self.assertEqual(default, CustomerProfile.account_number)
        
    def test_status_default(self):
        """ Test that Customer Profile Model Status has a default value """
        default = self.profile._meta.get_field('status').default
        self.assertEqual(default, self.profile.Status.NEW)
        
    def test_user_default(self):
        """ Test that Customer Profile Model User has no default value """
        default = self.profile._meta.get_field('user').default 
        self.assertEqual(default, NOT_PROVIDED)

    def test_last_job_default(self):
        """ Test that Customer Profile Model Last Job has no default value """
        default = self.profile._meta.get_field('last_job').default 
        self.assertEqual(default, NOT_PROVIDED)

    def test_language_default(self):
        """ Test that Customer Profile Model Language has a default value """
        default = self.profile._meta.get_field('language').default 
        self.assertEqual(default, self.profile.Language.ENGLISH)
        
    def test_theme_default(self):
        """ Test that Customer Profile Model Theme has a default value """
        default = self.profile._meta.get_field('theme').default
        self.assertEqual(default, self.profile.Colors.GREEN)
        
    def test_balance_owed_default(self):
        """ Test that Customer Profile Model Balance Owed has a default value """
        default = self.profile._meta.get_field('balance_owed').default
        self.assertEqual(default, False)
        
    def test_credit_owed_default(self):
        """ Test that Customer Profile Model Credit Owed has a default value """
        default = self.profile._meta.get_field('credit_owed').default
        self.assertEqual(default, False)
       
# Create a TestCase for Customer Profile Choices Fields
# crm_user.tests.models.test_CustomerProfileModel.ChoicesTests
class ChoicesTests(TestCase):
    """ Define a Testcase for Customer Profile Model Choices """
    @classmethod 
    def setUpTestData(cls):
        """ Define setUpTestData method for Customer Profile Model Choices """
        Customer.objects.create_user(
            email="doe@example.com",
            first_name="Sara",
            middle_name="Lee",
            last_name="Doe",
            birth_date='1993-04-14',
            phone_number="+12125556789",
        )
        
    def setUp(self):
        """ Define setUp method for Customer Profile Model Choices """
        self.user = Customer.objects.get(email="doe@example.com")
        self.profile = CustomerProfile.objects.get(user=self.user)
        
    def test_id_choices(self):
        """ Test that Customer Profile Model ID has no choices values """
        choices = self.profile._meta.get_field('id').choices 
        self.assertEqual(choices, None)
        
    def test_acct_no_choices(self):
        """ Test that Customer Profile Model Account Number has no choices value """
        choices = self.profile._meta.get_field('acct_no').choices 
        self.assertEqual(choices, None)
        
    def test_status_choices(self):
        """ Test that Customer Profile Model Status has a choices value """
        choices = self.profile._meta.get_field('status').choices
        self.assertEqual(choices, self.profile.Status.choices)
        
    def test_user_choices(self):
        """ Test that Customer Profile Model User has no choices value """
        choices = self.profile._meta.get_field('user').choices 
        self.assertEqual(choices, None)

    def test_last_job_choices(self):
        """ Test that Customer Profile Model Last Job has no choices value """
        choices = self.profile._meta.get_field('last_job').choices 
        self.assertEqual(choices, None)

    def test_language_choices(self):
        """ Test that Customer Profile Model Language has a choices value """
        choices = self.profile._meta.get_field('language').choices 
        self.assertEqual(choices, self.profile.Language.choices)
        
    def test_theme_choices(self):
        """ Test that Customer Profile Model Theme has a choices value """
        choices = self.profile._meta.get_field('theme').choices
        self.assertEqual(choices, self.profile.Colors.choices)

    def test_balance_owed_choices(self):
        """ Test that Customer Profile Model Balance Owed has a choices value """
        choices = self.profile._meta.get_field('balance_owed').choices 
        self.assertEqual(choices, None)
        
    def test_credit_owed_choices(self):
        """ Test that Customer Profile Model Credit Owed has a choices value """
        choices = self.profile._meta.get_field('credit_owed').choices
        self.assertEqual(choices, None)
       
# Create a TestCase for Customer Profile OneToOne Fields
# crm_user.tests.models.test_CustomerProfileModel.OneToOneTests
class OneToOneTests(TestCase):
    """ Define a TestCase for Customer Model OneToOne Fields """
    @classmethod 
    def setUpTestData(cls):
        """ Define setUpTestData method for Customer Profile Model OneToOne Fields """
        Customer.objects.create_user(
            email="doe@example.com",
            first_name="Sara",
            middle_name="Lee",
            last_name="Doe",
            birth_date='1993-04-14',
            phone_number="+12125556789",
        )
        
    def setUp(self):
        """ Define setUp method for Customer Profile Model OneToOne Fields """
        self.user = Customer.objects.get(email="doe@example.com")
        self.profile = CustomerProfile.objects.get(user=self.user)
        
    def test_user_one_to_one_related_name(self):
        """ Test that Customer Profile Model User has a related name value """
        self.assertEqual(self.profile, self.user.profile)
        
    def test_user_one_to_one_on_delete(self):
        """ Test that Customer Profile Model User has on_delete models.CASCADE """
        user = Customer.objects.get(id=1)
        profile = CustomerProfile.objects.get(id=1) 
        self.assertEqual(profile.user, user)
        user.delete()
        self.assertEqual(Customer.objects.filter(id=1).exists(), False)
        self.assertEqual(CustomerProfile.objects.filter(id=1).exists(), False)
 
# Create a TestCase for Customer Profile Methods
# crm_user.tests.models.test_CustomerProfileModel.MethodTests 
class MethodTests(TestCase):
    """ Define a TestCase for Customer Profile Model Methods """
    @classmethod 
    def setUpTestData(cls):
        """ Define setUpTestData method for Customer Profile Model Methods """
        Customer.objects.create_user(
            email="doe@example.com",
            first_name="Sara",
            middle_name="Lee",
            last_name="Doe",
            birth_date='1993-04-14',
            phone_number="+12125556789",
        )
        
    def setUp(self):
        """ Define setUp method for Customer Profile Model Methods """
        self.user = Customer.objects.get(email="doe@example.com")
        self.profile = CustomerProfile.objects.get(user=self.user)
        
    def test_string_method(self):
        """ Test for Customer Profile Model String Method """
        string = f'{self.profile.user.last_name}, {self.profile.user.first_name}'
        self.assertEqual(str(self.profile), string)
        
    def test_calc_acct_no_method(self):
        """ Test for Customer Model account_number Method """
        self.assertEqual(self.profile.acct_no, 'ACCT000001')
        self.assertEqual(CustomerProfile.account_number(), 'ACCT000002')
        
    def test_get_absolute_url_method(self):
        """ Test that Customer Model get_absolute_url method returns correct url """
        self.assertEqual(self.profile.get_absolute_url(), f'/user/user-details/{self.user.id}')
        
# Create a TestCase for Customer Profile Meta
# crm_user.tests.models.test_CustomerProfileModel.MetaTests 
class MetaTests(TestCase):
    """ Define a TestCase for Customer Profile Model Meta """
    @classmethod 
    def setUpTestData(cls):
        """ Define setUpTestData method for Customer Profile Model Meta """
        Customer.objects.create_user(
            email="doe@example.com",
            first_name="Sara",
            middle_name="Lee",
            last_name="Doe",
            birth_date='1993-04-14',
            phone_number="+12125556789",
        )
        
    def setUp(self):
        """ Define setUp method for Customer Profile Model Meta """
        self.user = Customer.objects.get(email="doe@example.com")
        self.profile = CustomerProfile.objects.get(user=self.user)
        
    def test_ordering(self):
        """ Test Customer Profile Model Ordering """
        self.assertEqual(self.profile._meta.ordering, ['user'])

    def test_verbose_name(self):
        """ Test Customer Profile Model Verbose Name """
        self.assertEqual(self.profile._meta.verbose_name, 'Customer Profile')
        
    def test_verbose_name_plural(self):
        """ Test Customer Profile Model Verbose Name Plural """
        self.assertEqual(self.profile._meta.verbose_name_plural, 'Customer Profiles')
        
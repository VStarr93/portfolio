#./crm_user/tests/models/test_EmployeeProfileModel.py
#-------------------------------------------------------------
#-------------------------------------------------------------
# IMPORTS

from django.test import TestCase
from crm_user.models import Employee, EmployeeProfile
from django.db.models.fields import NOT_PROVIDED

# For Testing Email Services
from django.core import mail 

#-------------------------------------------------------------
#-------------------------------------------------------------
# Create your Variables here.


#-------------------------------------------------------------
#-------------------------------------------------------------
# Create your EmployeeProfile Model tests here.

# Create a TestCase for Employee Profile Labels
# crm_user.tests.models.test_EmployeeProfileModel.LabelTests
class LabelTests(TestCase):
    """ Define a TestCase for Employee Profile Model Labels """
    @classmethod 
    def setUpTestData(cls):
        """ Define setUpTestData method for Employee Profile Model Labels """
        Employee.objects.create_user(
            email="doe@example.com",
            first_name="Sara",
            middle_name="Lee",
            last_name="Doe",
            birth_date='1993-04-14',
            phone_number="+12125556789",
        )
        
    def setUp(self):
        """ Define setUp method for Employee Profile Model Labels """
        self.user = EmployeeProfile.objects.get(id=1)
        
    def test_id_label(self):
        """ Test for Employee Profile Model ID Label """
        field_label = self.user._meta.get_field('id').verbose_name 
        self.assertEqual(field_label, 'ID')
        
    def test_work_id_label(self):
        """ Test for Employee Profile Model Work ID Label """
        field_label = self.user._meta.get_field('work_id').verbose_name 
        self.assertEqual(field_label, 'Work ID')
        
    def test_status_label(self):
        """ Test for Employee Profile Model Status Label """
        field_label = self.user._meta.get_field('status').verbose_name
        self.assertEqual(field_label, 'Status')
        
    def test_user_label(self):
        """ Test for Employee Profile Model User Label """
        field_label = self.user._meta.get_field('user').verbose_name 
        self.assertEqual(field_label, 'Employee')

    def test_is_manager_label(self):
        """ Test for Employee Profile Model Is Manager Label """
        field_label = self.user._meta.get_field('is_manager').verbose_name 
        self.assertEqual(field_label, 'Is Manager')

    def test_language_label(self):
        """ Test for Employee Profile Model Language Label """
        field_label = self.user._meta.get_field('language').verbose_name 
        self.assertEqual(field_label, 'Language')
        
    def test_theme_label(self):
        """ Test for Employee Profile Model Theme Label """
        field_label = self.user._meta.get_field('theme').verbose_name
        self.assertEqual(field_label, 'Theme')
        
# Create a TestCase for Employee Profile Max Lengths
# crm_user.tests.models.test_EmployeeProfileModel.MaxLengthTests
class MaxLengthTests(TestCase):
    """ Define a TestCase for Employee Profile Model Max Lengths """
    @classmethod 
    def setUpTestData(cls):
        """ Define setUpTestData method for Employee Profile Model Max Lengths """
        Employee.objects.create_user(
            email="doe@example.com",
            first_name="Sara",
            middle_name="Lee",
            last_name="Doe",
            birth_date='1993-04-14',
            phone_number="+12125556789",
        )
        
    def setUp(self):
        """ Define setUp method for Employee Profile Model Max Lengths """
        self.user = EmployeeProfile.objects.get(id=1)
        
    def test_id_max_length(self):
        """ Test for Employee Profile Model ID Max Length """
        max_length = self.user._meta.get_field('id').max_length 
        self.assertEqual(max_length, None)
        
    def test_work_id_max_length(self):
        """ Test for Employee Profile Model Work ID Max Length """
        max_length = self.user._meta.get_field('work_id').max_length 
        self.assertEqual(max_length, None)
        
    def test_status_max_length(self):
        """ Test for Employee Profile Model Status Max Length """
        max_length = self.user._meta.get_field('status').max_length
        self.assertEqual(max_length, 10)
        
    def test_user_max_length(self):
        """ Test for Employee Profile Model User Max Length """
        max_length = self.user._meta.get_field('user').max_length 
        self.assertEqual(max_length, None)

    def test_is_manager_max_length(self):
        """ Test for Employee Profile Model Is Manager Max Length """
        max_length = self.user._meta.get_field('is_manager').max_length 
        self.assertEqual(max_length, None)

    def test_language_max_length(self):
        """ Test for Employee Profile Model Language Max Length """
        max_length = self.user._meta.get_field('language').max_length 
        self.assertEqual(max_length, 10)
        
    def test_theme_max_length(self):
        """ Test for Employee Profile Model Theme Max Length """
        max_length = self.user._meta.get_field('theme').max_length
        self.assertEqual(max_length, 6)
        
# Create a TestCase for Employee Profile Help Text
# crm_user.tests.models.test_EmployeeProfileModel.HelpTextTests
class HelpTextTests(TestCase):
    """ Define a TestCase for Employee Profile Model Help Text """
    @classmethod 
    def setUpTestData(cls):
        """ Define setUpTestData method for Employee Profile Model Help Text """
        Employee.objects.create_user(
            email="doe@example.com",
            first_name="Sara",
            middle_name="Lee",
            last_name="Doe",
            birth_date='1993-04-14',
            phone_number="+12125556789",
        )
        
    def setUp(self):
        """ Define setUp method for Employee Profile Model Help Text """
        self.user = EmployeeProfile.objects.get(id=1)
        
    def test_id_help_text(self):
        """ Test for Employee Profile Model ID Help Text """
        help_text = self.user._meta.get_field('id').help_text 
        self.assertEqual(help_text, '')
        
    def test_work_id_help_text(self):
        """ Test for Employee Profile Model Work ID Help Text """
        help_text = self.user._meta.get_field('work_id').help_text 
        self.assertEqual(help_text, "Your employee work ID is auto-generated and cannot be changed.")
        
    def test_status_help_text(self):
        """ Test for Employee Profile Model Status Help Text """
        help_text = self.user._meta.get_field('status').help_text
        self.assertEqual(help_text, "Your employee status is adjusted based on employment status.")
        
    def test_user_help_text(self):
        """ Test for Employee Profile Model User Help Text """
        help_text = self.user._meta.get_field('user').help_text 
        self.assertEqual(help_text, "The Employee these details/model are associated with.")

    def test_is_manager_help_text(self):
        """ Test for Employee Profile Model Is Manager Help Text """
        help_text = self.user._meta.get_field('is_manager').help_text 
        self.assertEqual(help_text, "Is this employee a manager?")

    def test_language_help_text(self):
        """ Test for Employee Profile Model Language Help Text """
        help_text = self.user._meta.get_field('language').help_text 
        self.assertEqual(help_text, "What language do you speak?")
        
    def test_theme_help_text(self):
        """ Test for Employee Profile Model Theme Help Text """
        help_text = self.user._meta.get_field('theme').help_text
        self.assertEqual(help_text, "Choose a theme to use.")
        
# Create a TestCase for Employee Profile Required Fields
# crm_user.tests.models.test_EmployeeProfileModel.ReqTests
class ReqTests(TestCase):
    """ Define a TestCase for Employee Profile Model Required Fields"""
    @classmethod 
    def setUpTestData(cls):
        """ Define setUpTestData method for Employee Profile Model Required Fields """
        Employee.objects.create_user(
            email="doe@example.com",
            first_name="Sara",
            middle_name="Lee",
            last_name="Doe",
            birth_date='1993-04-14',
            phone_number="+12125556789",
        )
        
    def setUp(self):
        """ Define setUp method for Employee Profile Model Required Fields """
        self.user = EmployeeProfile.objects.get(id=1)
        
    def test_id_required(self):
        """ Test that Employee Profile Model ID is not required """
        blank = self.user._meta.get_field('id').blank 
        null = self.user._meta.get_field('id').null  
        self.assertEqual(blank, True)
        self.assertEqual(null, False)
        
    def test_work_id_required(self):
        """ Test that Employee Profile Model Work ID is required """
        blank = self.user._meta.get_field('work_id').blank 
        null = self.user._meta.get_field('work_id').null 
        self.assertEqual(blank, False)
        self.assertEqual(null, False)
        
    def test_status_required(self):
        """ Test that Employee Profile Model Status is required """
        blank = self.user._meta.get_field('status').blank
        null = self.user._meta.get_field('status').null
        self.assertEqual(blank, False)
        self.assertEqual(null, False)
        
    def test_user_required(self):
        """ Test that Employee Profile Model User is required """
        blank = self.user._meta.get_field('user').blank 
        null = self.user._meta.get_field('user').null 
        self.assertEqual(blank, False)
        self.assertEqual(null, False)

    def test_is_manager_required(self):
        """ Test that Employee Profile Model Is Manager is required """
        blank = self.user._meta.get_field('is_manager').blank 
        null = self.user._meta.get_field('is_manager').null 
        self.assertEqual(blank, False)
        self.assertEqual(null, False)

    def test_language_required(self):
        """ Test that Employee Profile Model Language is required """
        blank = self.user._meta.get_field('language').blank 
        null = self.user._meta.get_field('language').null 
        self.assertEqual(blank, False)
        self.assertEqual(null, False)
        
    def test_theme_required(self):
        """ Test that Employee Profile Model Theme is required """
        blank = self.user._meta.get_field('theme').blank
        null = self.user._meta.get_field('theme').null
        self.assertEqual(blank, False)
        self.assertEqual(null, False)
    
# Create a TestCase for Employee Profile Defaults
# crm_user.tests.models.test_EmployeeProfileModel.DefaultTests
class DefaultTests(TestCase):
    """ Define a Testcase for Employee Profile Model Defaults """
    @classmethod 
    def setUpTestData(cls):
        """ Define setUpTestData method for Employee Profile Model Defaults """
        Employee.objects.create_user(
            email="doe@example.com",
            first_name="Sara",
            middle_name="Lee",
            last_name="Doe",
            birth_date='1993-04-14',
            phone_number="+12125556789",
        )
        
    def setUp(self):
        """ Define setUp method for Employee Profile Model Defaults """
        self.user = EmployeeProfile.objects.get(id=1)
        
    def test_id_default(self):
        """ Test that Employee Profile Model ID has no default values """
        default = self.user._meta.get_field('id').default 
        self.assertEqual(default, NOT_PROVIDED)
        
    def test_work_id_default(self):
        """ Test that Employee Profile Model Work ID has a default value """
        default = self.user._meta.get_field('work_id').default 
        self.assertEqual(default, EmployeeProfile.calc_work_id)
        
    def test_status_default(self):
        """ Test that Employee Profile Model Status has a default value """
        default = self.user._meta.get_field('status').default
        self.assertEqual(default, self.user.Status.TRAINING)
        
    def test_user_default(self):
        """ Test that Employee Profile Model User has no default value """
        default = self.user._meta.get_field('user').default 
        self.assertEqual(default, NOT_PROVIDED)

    def test_is_manager_default(self):
        """ Test that Employee Profile Model Is Manager has a default value """
        default = self.user._meta.get_field('is_manager').default 
        self.assertEqual(default, False)

    def test_language_default(self):
        """ Test that Employee Profile Model Language has a default value """
        default = self.user._meta.get_field('language').default 
        self.assertEqual(default, self.user.Language.ENGLISH)
        
    def test_theme_default(self):
        """ Test that Employee Profile Model Theme has a default value """
        default = self.user._meta.get_field('theme').default
        self.assertEqual(default, self.user.Colors.GREEN)
       
# Create a TestCase for Employee Profile Choices Fields
# crm_user.tests.models.test_EmployeeProfileModel.ChoicesTests
class ChoicesTests(TestCase):
    """ Define a Testcase for Employee Profile Model Choices """
    @classmethod 
    def setUpTestData(cls):
        """ Define setUpTestData method for Employee Profile Model Choices """
        Employee.objects.create_user(
            email="doe@example.com",
            first_name="Sara",
            middle_name="Lee",
            last_name="Doe",
            birth_date='1993-04-14',
            phone_number="+12125556789",
        )
        
    def setUp(self):
        """ Define setUp method for Employee Profile Model Choices """
        self.user = EmployeeProfile.objects.get(id=1)
        
    def test_id_choices(self):
        """ Test that Employee Profile Model ID has no choices values """
        choices = self.user._meta.get_field('id').choices 
        self.assertEqual(choices, None)
        
    def test_work_id_choices(self):
        """ Test that Employee Profile Model Work ID has no choices value """
        choices = self.user._meta.get_field('work_id').choices 
        self.assertEqual(choices, None)
        
    def test_status_choices(self):
        """ Test that Employee Profile Model Status has a choices value """
        choices = self.user._meta.get_field('status').choices
        self.assertEqual(choices, self.user.Status.choices)
        
    def test_user_choices(self):
        """ Test that Employee Profile Model User has no choices value """
        choices = self.user._meta.get_field('user').choices 
        self.assertEqual(choices, None)

    def test_is_manager_choices(self):
        """ Test that Employee Profile Model Is Manager has no choices value """
        choices = self.user._meta.get_field('is_manager').choices 
        self.assertEqual(choices, None)

    def test_language_choices(self):
        """ Test that Employee Profile Model Language has a choices value """
        choices = self.user._meta.get_field('language').choices 
        self.assertEqual(choices, self.user.Language.choices)
        
    def test_theme_choices(self):
        """ Test that Employee Profile Model Theme has a choices value """
        choices = self.user._meta.get_field('theme').choices
        self.assertEqual(choices, self.user.Colors.choices)
       
# Create a TestCase for Employee Profile OneToOne Fields
# crm_user.tests.models.test_EmployeeProfileModel.OneToOneTests
class OneToOneTests(TestCase):
    """ Define a TestCase for Employee Model OneToOne Fields """
    @classmethod 
    def setUpTestData(cls):
        """ Define setUpTestData method for Employee Profile Model OneToOne Fields """
        Employee.objects.create_user(
            email="doe@example.com",
            first_name="Sara",
            middle_name="Lee",
            last_name="Doe",
            birth_date='1993-04-14',
            phone_number="+12125556789",
        )
        
    def setUp(self):
        """ Define setUp method for Employee Profile Model OneToOne Fields """
        self.profile = EmployeeProfile.objects.get(id=1)
        self.user = Employee.objects.get(id=1)
        
    def test_user_one_to_one_related_name(self):
        """ Test that Employee Profile Model User has a related name value """
        self.assertEqual(self.profile, self.user.emp_profile)
        
    def test_user_one_to_one_on_delete(self):
        """ Test that Employee Profile Model User has on_delete models.CASCADE """
        user = Employee.objects.get(id=1)
        profile = EmployeeProfile.objects.get(id=1) 
        self.assertEqual(profile.user, user)
        user.delete()
        self.assertEqual(Employee.objects.filter(id=1).exists(), False)
        self.assertEqual(EmployeeProfile.objects.filter(id=1).exists(), False)
 

#./crm_user/tests.py
#-------------------------------------------------------------
#-------------------------------------------------------------
# IMPORTS

from threading import _profile_hook
from django.test import TestCase, override_settings
from .models import User, Customer, Employee, Admin, CustomerProfile
from django.core.exceptions import ValidationError 
import datetime 
from django.core.files.uploadedfile import SimpleUploadedFile 
import shutil, tempfile 

# Management Commands
from io import StringIO 
from django.core.management import call_command 
from django.contrib.auth.models import Group, Permission 
from django.contrib.contenttypes.models import ContentType 


#-------------------------------------------------------------
#-------------------------------------------------------------
# Create your Variables here.

MEDIA_ROOT = tempfile.mkdtemp()


#-------------------------------------------------------------
#-------------------------------------------------------------
# Create your Management Commands tests here.

# Create a TestCase for creategroup command
# crm_user.tests.CreategroupTests
class CreategroupTests(TestCase):
    """
        Test creategroup command
    """
    def test_creategroup_output(self):
        """
            creategroup command runs successfully with 1 argument
        """
        out = StringIO()
        call_command("creategroup", 'new_group', stdout=out)
        self.assertIn("Successfully created", out.getvalue())

#Create a TestCase for createperm command
# crm_user.tests.CreatepermTests
class CreatepermTests(TestCase):
    """
        Test createperm command
    """
    def test_createperm_output(self):
        """
            createperm command runs successfully with 1 argument per option
        """
        out = StringIO()
        call_command("createperm", "add", "-m", "user", "-g", "admins", stdout=out)
        self.assertIn("Successfully added", out.getvalue())
        self.assertTrue(Group.objects.get(name='admins'))
        self.assertTrue(Permission.objects.get(name='Can add user'))
        self.assertTrue(Group.objects.get(name='admins').permissions.get(name='Can add user'))

    def test_createperm_two_models(self):
        """
            createperm command runs successfully with 2 arguments for model option
        """
        out = StringIO()
        call_command("createperm", "add", "-m", "user", 'customer', "-g", "admins", stdout=out)
        self.assertIn("Successfully added", out.getvalue())
        self.assertTrue(Group.objects.get(name='admins'))
        self.assertTrue(Permission.objects.get(name='Can add user'))
        self.assertTrue(Permission.objects.get(name='Can add customer'))
        self.assertTrue(Group.objects.get(name='admins').permissions.get(name='Can add user'))
        self.assertTrue(Group.objects.get(name='admins').permissions.get(name='Can add customer'))

    def test_createperm_two_groups(self):
        """
            createperm command runs successfully with 2 arguments for group option
        """
        out = StringIO()
        call_command("createperm", "add", "-m", "user", "-g", "admins", "customers", stdout=out)
        self.assertIn("Successfully added", out.getvalue())
        self.assertTrue(Group.objects.get(name='admins'))
        self.assertTrue(Group.objects.get(name='customers'))
        self.assertTrue(Permission.objects.get(name='Can add user'))
        self.assertTrue(Group.objects.get(name='admins').permissions.get(name='Can add user'))
        self.assertTrue(Group.objects.get(name='customers').permissions.get(name='Can add user'))

    def test_createperm_two_perms(self):
        """
            createperm command runs successfully with 2 arguments for perm_name positional argument
        """
        out = StringIO()
        call_command("createperm", "add", "view", "-m", "user", "-g", "admins", stdout=out)
        self.assertIn("Successfully added", out.getvalue())
        self.assertTrue(Group.objects.get(name='admins'))
        self.assertTrue(Permission.objects.get(name='Can add user'))
        self.assertTrue(Permission.objects.get(name='Can view user'))
        self.assertTrue(Group.objects.get(name='admins').permissions.get(name='Can add user'))
        self.assertTrue(Group.objects.get(name='admins').permissions.get(name='Can view user'))

#-------------------------------------------------------------
#-------------------------------------------------------------
# Create your User Model tests here.

# Create a TestCase for User Creation
# crm_user.tests.UserCreateTests
class UserCreateTests(TestCase):
    """
        Test user creation for regular user and superuser with and without passwords.
    """
    def test_create_user_with_password(self):
        """
            User is created successfully with email and password.
        """
        new_user = User.objects.create_user(email='test@example.com',password='test123')
        all_users = User.objects.all() 
        self.assertIn(new_user, all_users)
        self.assertIs(new_user.check_password('test123'), True)
    
    def test_create_user_without_password(self):
        """
            User is created successfully with email and no password.
            User does not have a usable password.
        """
        new_user = User.objects.create_user(email='test1@example.com')
        all_users = User.objects.all() 
        self.assertIn(new_user, all_users)
        self.assertIs(new_user.has_usable_password(), False)

    def test_create_superuser_with_password(self):
        """
            SuperUser is created successfully with email and password.
        """
        new_superuser = User.objects.create_superuser(email="test2@example.com", password="test123")
        all_users = User.objects.all() 
        self.assertIn(new_superuser, all_users)
        self.assertTrue(new_superuser.has_usable_password())
        
    def test_create_superuser_without_password(self):
        """
            SuperUser cannot be created without a password.
        """
        with self.assertRaises(TypeError):
            new_superuser = User.objects.create_superuser(email="test2@example.com")

# Create a TestCase for User Methods
# crm_user.tests.UserMethodTests
class UserMethodTests(TestCase):
    """
        Test User model method functionality
    """
    def setUp(self):
        """
            UserMethodTests setUp method to create test users
        """
        self.user1 = User.objects.create_user(email="test1@example.com")
        self.user2 = User.objects.create_user(email="test2@example.com")
    
    def test_method_age(self):
        """
            Test User.age calculates correctly from given birthdate
        """
        self.user1.birth_date = '1993-04-14'
        self.user1.save()
        self.assertEqual(self.user1.birth_date.year, 1993)
        self.assertEqual(self.user1.age(), 30)
        self.assertNotEqual(self.user1.age(), 29)

    def test_method_full_name(self):
        """
            Test full_name to display first and last name
        """
        self.user1.first_name = "Sue"
        self.user1.last_name = "Anne"
        self.user1.save()
        self.assertEqual(self.user1.full_name(), "Sue Anne")

# Create a TestCase for User Field Validations
# crm_user.tests.UserFieldTests
@override_settings(MEDIA_ROOT=MEDIA_ROOT)
class UserFieldTests(TestCase):
    """
        Test user fields for proper validation
    """
    @classmethod 
    def tearDownClass(cls):
        shutil.rmtree(MEDIA_ROOT, ignore_errors=True)
        super().tearDownClass()

    def test_field_type_default(self):
        """
            User Type defaults to CUSTOMER
        """
        user = User.objects.create_user(email="test@example.com")
        self.assertIs(user.type, User.Types.CUSTOMER)

    def test_field_email_syntax(self):
        """
            Email field must be in email format.
        """
        with self.assertRaises(ValidationError):
            User.objects.create_user(email="233345adada")

    def test_field_username_is_none(self):
        """
            Username field must be None.
        """
        user = User.objects.create_user(email="test@example.com")
        self.assertIsNone(user.username)

    def test_field_birth_date_is_date(self):
        """
            Birth Date field must be in the past and a date.
        """
        user = User.objects.create_user(email="test@example.com", birth_date="1993-04-14")
        self.assertLess(user.birth_date, datetime.date.today())
        self.assertEqual(user.birth_date.year, 1993)
        self.assertEqual(user.birth_date.month, 4)
        self.assertEqual(user.birth_date.day, 14)

    def test_field_profile_photo_upload(self):
        """
            Profile Photo is uploaded to /media/profile_images/
        """
        file = SimpleUploadedFile("test_image.jpg",b"test_content", "image/jpeg")
        user = User.objects.create_user(email="test@example.com", profile_photo=file)
        self.assertEqual(user.profile_photo.name, 'profile_images/test_image.jpg')

    def test_field_phone_number_syntax(self):
        """
            Phone Number should contain only numbers
        """
        user = User.objects.create_user(email="test@example.com", phone_number='+12818829480')
        with self.assertRaises(TypeError):
            User.objects.create_user(email="test1@example.com", phone_number=2818829480)
        with self.assertRaises(ValidationError):
            User.objects.create_user(email="test2@example.com", phone_number="2818829480")

# Create a TestCase for User Permissions


#-------------------------------------------------------------
#-------------------------------------------------------------
# Create your Customer - PROXY Model tests here.

# Create a TestCase for Customer Creation
# crm_user.tests.CustomerCreateTests
class CustomerCreateTests(TestCase):
    """
        Test Customer type creation
    """
    def setUp(self):
        """
            CustomerCreateTests setUp method to create test users.
        """
        self.user1 = Customer.objects.create_user(email="test1@example.com")
        self.user2 = Customer.objects.create_user(email="test2@example.com")

    def test_create_customer(self):
        """
            Test that customer was created successfully with type = CUSTOMER
        """
        self.assertEqual(self.user1.type, 'CUSTOMER')
        self.assertNotEqual(self.user1.type, 'EMPLOYEE')
        self.assertEqual(self.user1, User.objects.get(email=self.user1.email))

    def test_create_profile(self):
        """
            Test that customer profile is automatically created with the creation of new customer.
        """
        self.assertIsInstance(CustomerProfile.objects.get(user=self.user1), CustomerProfile)
        
# Create a TestCase for Customer Methods

# Create a TestCase for Customer Field Validations
# crm_user.tests.CustomerFieldTests
class CustomerFieldTests(TestCase):
    """
        Test Customer Profile fields for proper validation
    """
    def setUp(self):
        """
            CustomerFieldTests setUp method to create test users.
        """
        self.user1 = Customer.objects.create_user(email="test1@example.com")
        self.user2 = Customer.objects.create_user(email="test2@example.com")

    def test_fields_auto_generated(self):
        """
            Test that auto generated fields are correctly applied.
        """
        profile1 = CustomerProfile.objects.get(user=self.user1)
        profile2 = CustomerProfile.objects.get(user=self.user2)
        self.assertEqual(self.user1, profile.user )
        self.assertEqual(self.user1, profile.last_modified_by)
        self.assertIn("ACCT", profile.acct_no)
        self.assertEqual(profile.status, "NEW")
        self.assertIsNone(profile.last_job)
        self.assertEqual(profile.last_modified.date(), datetime.date.today())

# Create a TestCase for Customer Permissions


#-------------------------------------------------------------
#-------------------------------------------------------------
# Create your Employee Model tests here.

# Create a TestCase for Employee Creation

# Create a TestCase for Employee Methods

# Create a TestCase for Employee Field Validations

# Create a TestCase for Employee Permissions


#-------------------------------------------------------------
#-------------------------------------------------------------
# Create your Admin Model tests here.

# Create a TestCase for Admin Creation

# Create a TestCase for Admin Methods

# Create a TestCase for Admin Field Validations

# Create a TestCase for Admin Permissions



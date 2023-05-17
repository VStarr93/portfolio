#./crm_user/tests.py
#-------------------------------------------------------------
#-------------------------------------------------------------
# IMPORTS

from threading import _profile_hook
from django.test import TestCase, override_settings
from .models import *
from django.core.exceptions import ValidationError 
import datetime 
from django.core.files.uploadedfile import SimpleUploadedFile 
import shutil, tempfile 

# Management Commands
from io import StringIO 
from django.core.management import call_command 
from django.contrib.auth.models import Group, Permission 
from django.contrib.contenttypes.models import ContentType 

# For Testing Email Services
from django.core import mail 
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
# Create your base User Model tests here.

# Create a TestCase for User Creation
# crm_user.tests.BaseUserCreateTests
class BaseUserCreateTests(TestCase):
    """
        Test Base User creation for regular user and superuser with and without passwords.
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
        self.assertIs(new_user.has_usable_password(), True)

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
class BaseUserMethodTests(TestCase):
    """
        Test Base User model method functionality
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
class BaseUserFieldTests(TestCase):
    """
        Test Base User fields for proper validation
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
# crm_user.tests.CustomerMethodTests
class CustomerMethodTests(TestCase):
    """
        Test Customer model method functionality
    """
    def setUp(self):
        """
            CustomerMethodTests setUp method to create test users.
        """
        self.user1 = Customer.objects.create_user(email="test1@example.com")

    def test_method_welcome(self):
        """
            Welcome email should be sent upon new customer creation.
        """
        self.assertEqual(len(mail.outbox),2)
        self.user1.first_name = "Jessica"
        self.user1.save()
        self.assertEqual(len(mail.outbox),2)

    def test_method_account_number(self):
        """
            Account number should increment by 1 integer from last customer.
        """
        user2 = Customer.objects.create_user(email="test2@example.com")
        user3 = Customer.objects.create_user(email="test3@example.com")
        self.assertNotEqual(self.user1.profile.acct_no, user2.profile.acct_no)
        int1 = int(self.user1.profile.acct_no.split('ACCT')[-1])
        int2 = int(user2.profile.acct_no.split('ACCT')[-1])
        int3 = int(user3.profile.acct_no.split('ACCT')[-1])
        self.assertEqual(int2 - int1, 1)
        self.assertEqual(int3 - int1, 2)
        self.assertEqual(int3 - int2, 1)

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
        profile = CustomerProfile.objects.get(user=self.user1)
        self.assertEqual(self.user1, profile.user )
        self.assertEqual(self.user1, profile.last_modified_by)
        self.assertIn("ACCT", profile.acct_no)
        self.assertEqual(profile.status, "NEW")
        self.assertIsNone(profile.last_job)
        self.assertEqual(profile.last_modified.date(), datetime.date.today())

    def test_fields_boolean(self):
        """
            Test that boolean fields are correctly populating their defaults and change appropriately
        """
        self.assertFalse(self.user1.profile.balance_owed)
        self.assertFalse(self.user1.profile.credit_owed)
        self.user1.profile.balance_owed = True 
        self.user1.profile.credit_owed = True
        self.user1.save()
        self.assertTrue(self.user1.profile.balance_owed)
        self.assertTrue(self.user1.profile.credit_owed)

    def test_fields_optional(self):
        """
            Test that optional fields are correctly populating their defaults and change appropriately.
        """
        self.assertEqual(self.user1.profile.language, "ENGLISH")
        self.assertEqual(self.user1.profile.theme, "GREEN")

# Create a TestCase for Customer Permissions


#-------------------------------------------------------------
#-------------------------------------------------------------
# Create your Employee - PROXY Model tests here.

# Create a TestCase for Employee Creation
# crm_user.tests.EmployeeCreateTests
class EmployeeCreateTests(TestCase):
    """
        Test Employee type creation
    """
    def setUp(self):
        """
            EmployeeCreateTests setUp method to create test users.
        """
        self.user1 = Employee.objects.create_user(email="test1@example.com")
        self.user2 = Employee.objects.create_user(email="test2@example.com")

    def test_create_employee(self):
        """
            Test that employee was created successfully with type = EMPLOYEE
        """
        self.assertEqual(self.user1.type, 'EMPLOYEE')
        self.assertNotEqual(self.user1.type, 'CUSTOMER')
        self.assertEqual(self.user1, User.objects.get(email=self.user1.email))

    def test_create_profile(self):
        """
            Test that employee profile is automatically created with the creation of new employee.
        """
        self.assertIsInstance(EmployeeProfile.objects.get(user=self.user1), EmployeeProfile)
 
# Create a TestCase for Employee Methods
# crm_user.tests.EmployeeMethodTests
class EmployeeMethodTests(TestCase):
    """
        Test Employee model method functionality
    """
    def setUp(self):
        """
            EmployeeMethodTests setUp method to create test users.
        """
        self.user1 = Employee.objects.create_user(email="test1@example.com")

    def test_method_welcome(self):
        """
            Welcome email should be sent upon new employee creation.
        """
        self.assertEqual(len(mail.outbox),2)
        self.user1.first_name = "Jessica"
        self.user1.save()
        self.assertEqual(len(mail.outbox),2)

    def test_method_calc_work_id(self):
        """
            Work ID should increment by 1 integer from last employee.
        """
        user2 = Employee.objects.create_user(email="test2@example.com")
        user3 = Employee.objects.create_user(email="test3@example.com")
        self.assertNotEqual(self.user1.emp_profile.work_id, user2.emp_profile.work_id)
        int1 = int(self.user1.emp_profile.work_id)
        int2 = int(user2.emp_profile.work_id)
        int3 = int(user3.emp_profile.work_id)
        self.assertEqual(int2 - int1, 1)
        self.assertEqual(int3 - int1, 2)
        self.assertEqual(int3 - int2, 1)

# Create a TestCase for Employee Field Validations
# crm_user.tests.EmployeeFieldTests
class EmployeeFieldTests(TestCase):
    """
        Test Employee Profile fields for proper validation
    """
    def setUp(self):
        """
            EmployeeFieldTests setUp method to create test users.
        """
        self.user1 = Employee.objects.create_user(email="test1@example.com")
        self.user2 = Employee.objects.create_user(email="test2@example.com")

    def test_fields_auto_generated(self):
        """
            Test that auto generated fields are correctly applied.
        """
        profile = EmployeeProfile.objects.get(user=self.user1)
        self.assertEqual(self.user1, profile.user )
        self.assertEqual(self.user1, profile.last_modified_by)
        self.assertIsNotNone(profile.work_id)
        self.assertEqual(profile.status, "TRAINING")
        self.assertEqual(profile.last_modified.date(), datetime.date.today())

    def test_fields_boolean(self):
        """
            Test that boolean fields are correctly populating their defaults and change appropriately
        """
        self.assertFalse(self.user1.emp_profile.is_manager)
        self.user1.emp_profile.is_manager = True 
        self.user1.save()
        self.assertTrue(self.user1.emp_profile.is_manager)

    def test_fields_optional(self):
        """
            Test that optional fields are correctly populating their defaults and change appropriately.
        """
        self.assertEqual(self.user1.emp_profile.language, "ENGLISH")
        self.assertEqual(self.user1.emp_profile.theme, "GREEN")

# Create a TestCase for Employee Permissions


#-------------------------------------------------------------
#-------------------------------------------------------------
# Create your Admin - PROXY Model tests here.

# Create a TestCase for Admin Creation
# crm_user.tests.AdminCreateTests
class AdminCreateTests(TestCase):
    """
        Test Admin type creation
    """
    def setUp(self):
        """
            AdminCreateTests setUp method to create test users.
        """
        self.user1 = Admin.objects.create_user(email="test1@example.com")
        self.user2 = Admin.objects.create_user(email="test2@example.com")

    def test_create_admin(self):
        """
            Test that admin was created successfully with type = ADMIN
        """
        self.assertEqual(self.user1.type, 'ADMIN')
        self.assertNotEqual(self.user1.type, 'CUSTOMER')
        self.assertEqual(self.user1, User.objects.get(email=self.user1.email))

    def test_create_profile(self):
        """
            Test that admin profile is automatically created with the creation of new admin.
        """
        self.assertIsInstance(AdminProfile.objects.get(user=self.user1), AdminProfile)
 
# Create a TestCase for Admin Methods
# crm_user.tests.AdminMethodTests
class AdminMethodTests(TestCase):
    """
        Test Admin model method functionality
    """
    def setUp(self):
        """
            AdminMethodTests setUp method to create test users.
        """
        self.user1 = Admin.objects.create_user(email="test1@example.com")

    def test_method_welcome(self):
        """
            Welcome email should be sent upon new admin creation.
        """
        self.assertEqual(len(mail.outbox),2)
        self.user1.first_name = "Jessica"
        self.user1.save()
        self.assertEqual(len(mail.outbox),2)

    def test_method_calc_work_id(self):
        """
            Work ID should increment by 1 integer from last admin.
        """
        user2 = Admin.objects.create_user(email="test2@example.com")
        user3 = Admin.objects.create_user(email="test3@example.com")
        self.assertNotEqual(self.user1.admin_profile.work_id, user2.admin_profile.work_id)
        int1 = int(self.user1.admin_profile.work_id)
        int2 = int(user2.admin_profile.work_id)
        int3 = int(user3.admin_profile.work_id)
        self.assertEqual(int2 - int1, 1)
        self.assertEqual(int3 - int1, 2)
        self.assertEqual(int3 - int2, 1)

# Create a TestCase for Admin Field Validations
# crm_user.tests.AdminFieldTests
class AdminFieldTests(TestCase):
    """
        Test Admin Profile fields for proper validation
    """
    def setUp(self):
        """
            AdminFieldTests setUp method to create test users.
        """
        self.user1 = Admin.objects.create_user(email="test1@example.com")
        self.user2 = Admin.objects.create_user(email="test2@example.com")

    def test_fields_auto_generated(self):
        """
            Test that auto generated fields are correctly applied.
        """
        profile = AdminProfile.objects.get(user=self.user1)
        self.assertEqual(self.user1, profile.user )
        self.assertEqual(self.user1, profile.last_modified_by)
        self.assertIsNotNone(profile.work_id)
        self.assertEqual(profile.status, "TRAINING")
        self.assertEqual(profile.last_modified.date(), datetime.date.today())

    def test_fields_boolean(self):
        """
            Test that boolean fields are correctly populating their defaults and change appropriately
        """
        self.assertFalse(self.user1.admin_profile.is_manager)
        self.user1.admin_profile.is_manager = True 
        self.user1.save()
        self.assertTrue(self.user1.admin_profile.is_manager)

    def test_fields_optional(self):
        """
            Test that optional fields are correctly populating their defaults and change appropriately.
        """
        self.assertEqual(self.user1.admin_profile.language, "ENGLISH")
        self.assertEqual(self.user1.admin_profile.theme, "GREEN")

# Create a TestCase for Admin Permissions

#-------------------------------------------------------------
#-------------------------------------------------------------
# Create your User Model tests here.

# Create a TestCase for User Creation
# crm_user.tests.UserCreateTests
class UserCreateTests(TestCase):
    """
        Test User type creation
    """
    def setUp(self):
        """
            UserCreateTests setUp method to create test users.
        """
        self.user1 = User.objects.create_user(email="test1@example.com", type="CUSTOMER")
        self.user2 = User.objects.create_user(email="test2@example.com", type="EMPLOYEE")
        self.user3 = User.objects.create_user(email="test3@example.com", type="ADMIN")

    def test_create_profiles(self):
        """
            Test that user was created successfully with correct profile
        """
        self.assertIsInstance(CustomerProfile.objects.get(user=self.user1), CustomerProfile)
        self.assertIsInstance(EmployeeProfile.objects.get(user=self.user2), EmployeeProfile)
        self.assertIsInstance(AdminProfile.objects.get(user=self.user3), AdminProfile)

# Create a TestCase for User Methods
# crm_user.tests.UserMethodTests
class UserMethodTests(TestCase):
    """
        Test User model method functionality
    """
    def setUp(self):
        """
            UserMethodTests setUp method to create test users.
        """
        self.user1 = User.objects.create_user(email="test1@example.com", type="CUSTOMER")
        self.user2 = User.objects.create_user(email="test2@example.com", type="EMPLOYEE")
        self.user3 = User.objects.create_user(email="test3@example.com", type="ADMIN")

    def test_method_welcome(self):
        """
            Welcome email should be sent upon new user creation.
        """
        self.assertEqual(len(mail.outbox),3)
        self.user1.first_name = "Jessica"
        self.user1.save()
        self.assertEqual(len(mail.outbox),3)
        user2 = User.objects.create_user(email="test4@example.com", type="CUSTOMER")
        self.assertEqual(len(mail.outbox),4)

    def test_method_age(self):
        """
            Age should be calculated based on user birthday
        """
        self.user1.birth_date = '1993-04-14'
        self.user1.save()
        self.assertEqual(self.user1.age(), 30)
        self.assertNotEqual(self.user1.age(), 40)
        
    def test_method_full_name(self):
        """
            Full name should display first name and last name
        """
        self.user1.first_name = "John"
        self.user1.last_name = "Smith"
        self.user1.save()
        self.assertEqual(self.user1.full_name(), "John Smith")
        self.assertNotEqual(self.user1.full_name(), "JohnSmith")

# Create a TestCase for User Field Validations
# crm_user.tests.UserFieldTests
class UserFieldTests(TestCase):
    """
        Test User fields for proper validation
    """
    def setUp(self):
        """
            UserFieldTests setUp method to create test users.
        """
        self.user1 = User.objects.create_user(email="test1@example.com", type="CUSTOMER")
        self.user2 = User.objects.create_user(email="test2@example.com", type="EMPLOYEE")
        self.user3 = User.objects.create_user(email="test3@example.com", type="ADMIN")
        self.custProfile = CustomerProfile.objects.get(user=self.user1)
        self.empProfile = EmployeeProfile.objects.get(user=self.user2)
        self.adminProfile = AdminProfile.objects.get(user=self.user3)

    def test_fields_auto_generated(self):
        """
            Test that auto generated fields are correctly applied.
        """
        user4 = User.objects.create_user(email="temp@example.com")
        self.assertIsInstance(Customer.objects.get(email=user4.email), Customer)
        self.assertEqual(self.user1, self.custProfile.last_modified_by )
        self.assertEqual(self.user2, self.empProfile.last_modified_by )
        self.assertEqual(self.user3, self.adminProfile.last_modified_by )
        self.assertIsNotNone(self.custProfile.acct_no)
        self.assertIsNotNone(self.empProfile.work_id)
        self.assertIsNotNone(self.adminProfile.work_id)
        self.assertEqual(self.custProfile.status, "NEW")
        self.assertEqual(self.empProfile.status, "TRAINING")
        self.assertEqual(self.adminProfile.status, "TRAINING")
        self.assertEqual(self.custProfile.last_modified.date(), datetime.date.today())
        self.assertEqual(self.empProfile.last_modified.date(), datetime.date.today())
        self.assertEqual(self.adminProfile.last_modified.date(), datetime.date.today())

    def test_fields_boolean(self):
        """
            Test that boolean fields are correctly populating their defaults and change appropriately
        """
        self.assertFalse(self.adminProfile.is_manager)
        self.assertFalse(self.empProfile.is_manager)
        self.assertFalse(self.custProfile.balance_owed)
        self.assertFalse(self.custProfile.credit_owed)
        
    def test_fields_optional(self):
        """
            Test that optional fields are correctly populating their defaults and change appropriately.
        """
        # Defaults
        self.assertEqual(self.adminProfile.language, "ENGLISH")
        self.assertEqual(self.adminProfile.theme, "GREEN")
        self.assertEqual(self.custProfile.language, "ENGLISH")
        self.assertEqual(self.custProfile.theme, "GREEN")
        self.assertEqual(self.empProfile.language, "ENGLISH")
        self.assertEqual(self.empProfile.theme, "GREEN")
        # Provided
        self.user1.middle_name = "Jane"
        self.user1.save()
        self.assertEqual(self.user1.middle_name, "Jane")
        self.user1.birth_date = "1993-04-14"
        self.user1.save()
        self.assertEqual(self.user1.birth_date, datetime.date(1993,4,14))

# Create a TestCase for User Permissions



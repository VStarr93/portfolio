#./crm_user/tests/test_models.py
#-------------------------------------------------------------
#-------------------------------------------------------------
# IMPORTS

from django.test import TestCase, override_settings
from crm_user.models import *
from django.core.exceptions import ValidationError 
import datetime 
from django.core.files.uploadedfile import SimpleUploadedFile 
import shutil, tempfile 

# For Testing Email Services
from django.core import mail 
#-------------------------------------------------------------
#-------------------------------------------------------------
# Create your Variables here.

MEDIA_ROOT = tempfile.mkdtemp()


#-------------------------------------------------------------
#-------------------------------------------------------------
# Create your base User Model tests here.

# Create a TestCase for User Creation
# crm_user.tests.test_models.BaseUserCreateTests
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
# crm_user.tests.test_models.UserMethodTests
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
# crm_user.tests.test_models.UserFieldTests
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


#-------------------------------------------------------------
#-------------------------------------------------------------
# Create your Customer - PROXY Model tests here.

# Create a TestCase for Customer Creation
# crm_user.tests.test_models.CustomerCreateTests
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

# Create a TestCase for Customer Methods
# crm_user.tests.test_models.CustomerMethodTests
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
        self.user1.welcome()
        self.assertEqual(len(mail.outbox),3)
        subject1 = mail.outbox[0].subject
        subject2 = mail.outbox[1].subject
        self.assertIn("Welcome", subject1)
        self.assertIn("Password", subject2)


#-------------------------------------------------------------
#-------------------------------------------------------------
# Create your CustomerProfile Model tests here.

# Create a TestCase for Customer Profile Creation
# crm_user.tests.test_models.CustomerProfileCreateTests
class CustomerProfileCreateTests(TestCase):
    """
        Test Customer Profile creation
    """
    def setUp(self):
        """
            CustomerProfileCreateTests setUp method to create test users.
        """
        self.user1 = Customer.objects.create_user(email="test1@example.com")
        self.user2 = Customer.objects.create_user(email="test2@example.com")

    def test_create_profile(self):
        """
            Test that customer profile is automatically created with the creation of new customer.
        """
        self.assertIsInstance(CustomerProfile.objects.get(user=self.user1), CustomerProfile)
        
# Create a TestCase for Customer Profile Methods
# crm_user.tests.test_models.CustomerProfileMethodTests
class CustomerProfileMethodTests(TestCase):
    """
        Test Customer Profile model method functionality
    """
    def setUp(self):
        """
            CustomerProfileMethodTests setUp method to create test users.
        """
        self.user1 = Customer.objects.create_user(email="test1@example.com").profile
        self.user2 = Customer.objects.create_user(email="test2@example.com").profile
        self.user3 = Customer.objects.create_user(email="test3@example.com").profile

    def test_method_account_number(self):
        """
            Account number should increment by 1 integer from last customer.
        """
        self.assertNotEqual(self.user1.acct_no, self.user2.acct_no)
        int1 = int(self.user1.acct_no.split('ACCT')[-1])
        int2 = int(self.user2.acct_no.split('ACCT')[-1])
        int3 = int(self.user3.acct_no.split('ACCT')[-1])
        self.assertEqual(int2 - int1, 1)
        self.assertEqual(int3 - int1, 2)
        self.assertEqual(int3 - int2, 1)

# Create a TestCase for Customer Profile Field Validations
# crm_user.tests.test_models.CustomerProfileFieldTests
class CustomerProfileFieldTests(TestCase):
    """
        Test Customer Profile fields for proper validation
    """
    def setUp(self):
        """
            CustomerProfileFieldTests setUp method to create test users.
        """
        self.user1 = Customer.objects.create_user(email="test1@example.com").profile
        self.user2 = Customer.objects.create_user(email="test2@example.com").profile

    def test_fields_auto_generated(self):
        """
            Test that auto generated fields are correctly applied.
        """
        self.assertEqual(self.user1.user, self.user1.last_modified_by)
        self.assertIn("ACCT", self.user1.acct_no)
        self.assertEqual(self.user1.status, "NEW")
        self.assertIsNone(self.user1.last_job)
        self.assertEqual(self.user1.last_modified.date(), datetime.date.today())

    def test_fields_boolean(self):
        """
            Test that boolean fields are correctly populating their defaults and change appropriately
        """
        self.assertFalse(self.user1.balance_owed)
        self.assertFalse(self.user1.credit_owed)
        self.user1.balance_owed = True 
        self.user1.credit_owed = True
        self.user1.save()
        self.assertTrue(self.user1.balance_owed)
        self.assertTrue(self.user1.credit_owed)

    def test_fields_optional(self):
        """
            Test that optional fields are correctly populating their defaults and change appropriately.
        """
        self.assertEqual(self.user1.language, "ENGLISH")
        self.assertEqual(self.user1.theme, "GREEN")


#-------------------------------------------------------------
#-------------------------------------------------------------
# Create your Employee - PROXY Model tests here.

# Create a TestCase for Employee Creation
# crm_user.tests.test_models.EmployeeCreateTests
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

# Create a TestCase for Employee Methods
# crm_user.tests.test_models.EmployeeMethodTests
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
        self.user1.welcome()
        self.assertEqual(len(mail.outbox),3)
        subject1 = mail.outbox[0].subject 
        subject2 = mail.outbox[1].subject 
        self.assertIn("Welcome", subject1)
        self.assertIn("Password", subject2)


#-------------------------------------------------------------
#-------------------------------------------------------------
# Create your EmployeeProfile Model tests here.

# Create a TestCase for Employee Profile Creation
# crm_user.tests.test_models.EmployeeProfileCreateTests
class EmployeeProfileCreateTests(TestCase):
    """
        Test Employee Profile creation
    """
    def setUp(self):
        """
            EmployeeProfileCreateTests setUp method to create test users.
        """
        self.user1 = Employee.objects.create_user(email="test1@example.com")
        self.user2 = Employee.objects.create_user(email="test2@example.com")

    def test_create_profile(self):
        """
            Test that employee profile is automatically created with the creation of new employee.
        """
        self.assertIsInstance(EmployeeProfile.objects.get(user=self.user1), EmployeeProfile)
 
# Create a TestCase for Employee Profile Methods
# crm_user.tests.test_models.EmployeeProfileMethodTests
class EmployeeProfileMethodTests(TestCase):
    """
        Test Employee Profile method functionality
    """
    def setUp(self):
        """
            EmployeeProfileMethodTests setUp method to create test users.
        """
        self.user1 = Employee.objects.create_user(email="test1@example.com").emp_profile
        self.user2 = Employee.objects.create_user(email="test2@example.com").emp_profile 
        self.user3 = Employee.objects.create_user(email="test3@example.com").emp_profile 
        
    def test_method_calc_work_id(self):
        """
            Work ID should increment by 1 integer from last employee.
        """
        self.assertNotEqual(self.user1.work_id, self.user2.work_id)
        int1 = int(self.user1.work_id)
        int2 = int(self.user2.work_id)
        int3 = int(self.user3.work_id)
        self.assertEqual(int2 - int1, 1)
        self.assertEqual(int3 - int1, 2)
        self.assertEqual(int3 - int2, 1)

# Create a TestCase for Employee Profile Field Validations
# crm_user.tests.test_models.EmployeeProfileFieldTests
class EmployeeProfileFieldTests(TestCase):
    """
        Test Employee Profile fields for proper validation
    """
    def setUp(self):
        """
            EmployeeFieldTests setUp method to create test users.
        """
        self.user1 = Employee.objects.create_user(email="test1@example.com").emp_profile 
        self.user2 = Employee.objects.create_user(email="test2@example.com").emp_profile 

    def test_fields_auto_generated(self):
        """
            Test that auto generated fields are correctly applied.
        """
        self.assertEqual(self.user1.user, self.user1.last_modified_by)
        self.assertIsNotNone(self.user1.work_id)
        self.assertEqual(self.user1.status, "TRAINING")
        self.assertEqual(self.user1.last_modified.date(), datetime.date.today())

    def test_fields_boolean(self):
        """
            Test that boolean fields are correctly populating their defaults and change appropriately
        """
        self.assertFalse(self.user1.is_manager)
        self.user1.is_manager = True 
        self.user1.save()
        self.assertTrue(self.user1.is_manager)

    def test_fields_optional(self):
        """
            Test that optional fields are correctly populating their defaults and change appropriately.
        """
        self.assertEqual(self.user1.language, "ENGLISH")
        self.assertEqual(self.user1.theme, "GREEN")


#-------------------------------------------------------------
#-------------------------------------------------------------
# Create your Admin - PROXY Model tests here.

# Create a TestCase for Admin Creation
# crm_user.tests.test_models.AdminCreateTests
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

# Create a TestCase for Admin Methods
# crm_user.tests.test_models.AdminMethodTests
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
        self.user1.welcome()
        self.assertEqual(len(mail.outbox),3)
        subject1 = mail.outbox[0].subject 
        subject2 = mail.outbox[1].subject 
        self.assertIn("Welcome", subject1)
        self.assertIn("Password", subject2)


#-------------------------------------------------------------
#-------------------------------------------------------------
# Create your AdminProfile Model tests here.

# Create a TestCase for Admin Profile Creation
# crm_user.tests.test_models.AdminProfileCreateTests
class AdminProfileCreateTests(TestCase):
    """
        Test Admin Profile creation
    """
    def setUp(self):
        """
            AdminProfileCreateTests setUp method to create test users.
        """
        self.user1 = Admin.objects.create_user(email="test1@example.com")

    def test_create_profile(self):
        """
            Test that admin profile is automatically created with the creation of new admin.
        """
        self.assertIsInstance(AdminProfile.objects.get(user=self.user1), AdminProfile)
 
# Create a TestCase for Admin Profile Methods
# crm_user.tests.test_models.AdminProfileMethodTests
class AdminProfileMethodTests(TestCase):
    """
        Test Admin Profile method functionality
    """
    def setUp(self):
        """
            AdminProfileMethodTests setUp method to create test users.
        """
        self.user1 = Admin.objects.create_user(email="test1@example.com").admin_profile
        self.user2 = Admin.objects.create_user(email="test2@example.com").admin_profile 
        self.user3 = Admin.objects.create_user(email="test3@example.com").admin_profile 

    def test_method_calc_work_id(self):
        """
            Work ID should increment by 1 integer from last admin.
        """
        self.assertNotEqual(self.user1.work_id, self.user2.work_id)
        int1 = int(self.user1.work_id)
        int2 = int(self.user2.work_id)
        int3 = int(self.user3.work_id)
        self.assertEqual(int2 - int1, 1)
        self.assertEqual(int3 - int1, 2)
        self.assertEqual(int3 - int2, 1)

# Create a TestCase for Admin Profile Field Validations
# crm_user.tests.test_models.AdminProfileFieldTests
class AdminProfileFieldTests(TestCase):
    """
        Test Admin Profile fields for proper validation
    """
    def setUp(self):
        """
            AdminProfileFieldTests setUp method to create test users.
        """
        self.user1 = Admin.objects.create_user(email="test1@example.com").admin_profile 
        self.user2 = Admin.objects.create_user(email="test2@example.com").admin_profile 

    def test_fields_auto_generated(self):
        """
            Test that auto generated fields are correctly applied.
        """
        self.assertEqual(self.user1.user, self.user1.last_modified_by)
        self.assertIsNotNone(self.user1.work_id)
        self.assertEqual(self.user1.status, "TRAINING")
        self.assertEqual(self.user1.last_modified.date(), datetime.date.today())

    def test_fields_boolean(self):
        """
            Test that boolean fields are correctly populating their defaults and change appropriately
        """
        self.assertFalse(self.user1.is_manager)
        self.user1.is_manager = True 
        self.user1.save()
        self.assertTrue(self.user1.is_manager)

    def test_fields_optional(self):
        """
            Test that optional fields are correctly populating their defaults and change appropriately.
        """
        self.assertEqual(self.user1.language, "ENGLISH")
        self.assertEqual(self.user1.theme, "GREEN")


#-------------------------------------------------------------
#-------------------------------------------------------------
# Create your custom User Model tests here.

# Create a TestCase for Custom User Creation
# crm_user.tests.test_models.CustomUserCreateTests
class CustomUserCreateTests(TestCase):
    """
        Test Custom User type creation
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

# Create a TestCase for Custom User Methods
# crm_user.tests.test_models.CustomUserMethodTests
class CustomUserMethodTests(TestCase):
    """
        Test Custom User model method functionality
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
        self.assertEqual(len(mail.outbox),6)
        self.user1.first_name = "Jessica"
        self.user1.save()
        self.assertEqual(len(mail.outbox),6)
        Customer.objects.get(email=self.user1.email).welcome()
        self.assertEqual(len(mail.outbox),7)
        subject1 = mail.outbox[0].subject 
        subject2 = mail.outbox[1].subject 
        self.assertIn("Welcome", subject1)
        self.assertIn("Password", subject2)

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

# Create a TestCase for Custom User Field Validations
# crm_user.tests.test_models.CustomUserFieldTests
class CustomUserFieldTests(TestCase):
    """
        Test Custom User fields for proper validation
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


#-------------------------------------------------------------
#-------------------------------------------------------------
# Create your Address Model tests here.

# Create a TestCase for Address Creation
# crm_user.tests.test_models.AddressCreateTests
class AddressCreateTests(TestCase):
    """
        Test Address creation
    """
    def setUp(self):
        """
            AddressCreateTests setUp method to create test users.
        """
        self.user1 = User.objects.create_user(email="test1@example.com", type="CUSTOMER")
        
    def test_create_address(self):
        """
            Test that address was created successfully with correct user
        """
        address = Address.objects.create(user=self.user1, address_line1="123 Sara lane", city="Houston", state="TX", zip="77309", name="home")
        address2 = Address.objects.create(user=self.user1, address_line1="456 Sara lane", city="Houston", state="TX", zip="77309", name="work", type="COMMERCIAL")
        self.assertIn(address, self.user1.addresses.all())
        self.assertIn(address2, self.user1.addresses.all())

# Create a TestCase for Address Field Validations
# crm_user.tests.test_models.AddressFieldTests
class AddressFieldTests(TestCase):
    """
        Test Address fields for proper validation
    """
    def setUp(self):
        """
            UserFieldTests setUp method to create test users.
        """
        self.user1 = User.objects.create_user(email="test1@example.com", type="CUSTOMER")
        self.address1 = Address.objects.create(user=self.user1, address_line1="123 Sara lane", city="Houston", state="TX", zip="77309", name="home")

    def test_fields_auto_generated(self):
        """
            Test that auto generated fields are correctly applied.
        """
        self.assertEqual(self.user1, self.address1.last_modified_by )
        self.assertEqual(self.address1.last_modified.date(), datetime.date.today())
        self.assertIsNotNone(self.address1.id)
        self.assertEqual(self.address1.type, "RESIDENTIAL")
        
    def test_fields_optional(self):
        """
            Test that optional fields are correctly populating their defaults and change appropriately.
        """
        # Defaults
        self.assertIsNone(self.address1.address_line2)
        # Provided
        self.address1.address_line2 = "apt 32"
        self.user1.save()
        self.assertEqual(self.address1.address_line2, "apt 32")
        


#./crm_user/tests.py
#-------------------------------------------------------------
#-------------------------------------------------------------
# IMPORTS

from django.test import TestCase
from .models import User, Customer, Employee, Admin
from django.core.exceptions import ValidationError 
import datetime 

#-------------------------------------------------------------
#-------------------------------------------------------------
# Create your User Model tests here.

# Create a TestCase for User Creation
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

# Create a TestCase for User Field Validations
class UserFieldTests(TestCase):
    """
        Test user fields for proper validation
    """
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

# Create a TestCase for User Permissions


#-------------------------------------------------------------
#-------------------------------------------------------------
# Create your Customer Model tests here.

# Create a TestCase for Customer Creation

# Create a TestCase for Customer Methods

# Create a TestCase for Customer Field Validations

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



#./crm_user/tests.py
#-------------------------------------------------------------
#-------------------------------------------------------------
# IMPORTS

from django.test import TestCase
from .models import User, Customer, Employee, Admin


#-------------------------------------------------------------
#-------------------------------------------------------------
# Create your User Model tests here.

# Create a TestCase for User Creation
class UserCreateTests(TestCase):
    def test_create_user_with_password(self):
        new_user = User.objects.create_user(email='test@example.com',password='test123')
        all_users = User.objects.all() 
        self.assertIn(new_user, all_users)
        self.assertIs(new_user.check_password('test123'), True)
    
    def test_create_user_without_password(self):
        new_user = User.objects.create_user(email='test1@example.com')
        all_users = User.objects.all() 
        self.assertIn(new_user, all_users)
        self.assertIs(new_user.has_usable_password(), False)

    def test_create_superuser_with_password(self):
        new_superuser = User.objects.create_superuser(email="test2@example.com", password="test123")
        all_users = User.objects.all() 
        self.assertIn(new_superuser, all_users)
        self.assertTrue(new_superuser.has_usable_password())
        
    def test_create_superuser_without_password(self):
        with self.assertRaises(TypeError):
            new_superuser = User.objects.create_superuser(email="test2@example.com")

# Create a TestCase for User Methods

# Create a TestCase for User Field Validations

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



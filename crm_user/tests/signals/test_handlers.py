#./crm_user/tests/signals/test_handlers.py
#-------------------------------------------------------------
#-------------------------------------------------------------
# IMPORTS

from django.test import TestCase
from crm_user.models import Address, User, AdminProfile, EmployeeProfile, CustomerProfile
from crm_user.signals import handlers 

# For Testing Permissions
from guardian.shortcuts import assign_perm
# For Testing Email Services
from django.core import mail 

#-------------------------------------------------------------
#-------------------------------------------------------------
# Create your Variables here.


#-------------------------------------------------------------
#-------------------------------------------------------------
# Create your Signal tests here.

# Create a TestCase for Handler Tests
# crm_user.tests.signals.test_handlers.HandlerTests
class HandlerTests(TestCase):
    """ Define a TestCase for Signal Handlers """
    def test_user_type_customer_creates_customer(self):
        """ Test that creating a user type customer creates a Customer Profile object """
        User.objects.create_user(email='test@example.com', type='CUSTOMER')
        self.assertEqual(CustomerProfile.objects.filter(id=1).exists(), True)
        self.assertEqual(len(mail.outbox), 2)
        
    def test_user_type_employee_creates_employee(self):
        """ Test that creating a user type employee creates an Employee Profile object """
        User.objects.create_user(email='test@example.com', type='EMPLOYEE')
        self.assertEqual(EmployeeProfile.objects.filter(id=1).exists(), True)
        self.assertEqual(len(mail.outbox), 2)
        
    def test_user_type_admin_creates_admin(self):
        """ Test that creating a user type admin creates an Admin Profile object """
        User.objects.create_user(email='test@example.com', type='ADMIN')
        self.assertEqual(AdminProfile.objects.filter(id=1).exists(), True)
        self.assertEqual(len(mail.outbox), 2)

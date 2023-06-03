#./crm_user/tests/signals/test_handlers.py
#-------------------------------------------------------------
#-------------------------------------------------------------
# IMPORTS

from django.test import TestCase
from crm_user.models import Address, User, AdminProfile, EmployeeProfile, CustomerProfile
from crm_user.signals import handlers 

# For Testing Permissions
from guardian.shortcuts import assign_perm
from django.contrib.auth.models import Group, Permission

# For Testing Email Services
from django.core import mail 

# For Testing Database
from freezegun import freeze_time
from django.utils import timezone 

#-------------------------------------------------------------
#-------------------------------------------------------------
# Create your Variables here.


#-------------------------------------------------------------
#-------------------------------------------------------------
# Create your Signal tests here.

# Create a TestCase for Handler Tests
# crm_user.tests.signals.test_handlers.HandlerTests
class UserCreateProfileTests(TestCase):
    """ Define a TestCase for New User creates Profile Tests """
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

# Create a TestCase for Customer Set Permissions Reciever 
# crm_user.tests.signals.test_handlers.CustomerSetPermsTests
class CustomerSetPermsTests(TestCase):
    """ Define a TestCase for Customer Set Permissions Reciever """
    def setUp(self):
        """ Define a setUp method for CustomerSetPermsTests to create test users and groups """
        # Create customer 
        self.customer = Customer.objects.create_user(email="test@example.com")
        self.user = User.objects.create_user(email="test1@example.com")
        # Get Admin Group
        self.admin_group = Group.objects.get(name='Admins')
        self.employee_manager_group = Group.objects.get(name='Employee - Manager')
        self.employee_standard_group = Group.objects.get(name='Employee - Standard')
        self.customer_group = Group.objects.get(name='Customer')
        
    def test_customer_created_customer_view_permission(self):
        """ Test that when a customer is created, they receive view permission for that object (their user) """

        self.assertEqual(self.customer.has_perm('view_user', self.customer), True)
        
    def test_customer_created_customer_change_permission(self):
        """ Test that when a customer is created, they receive change permission for that object (their user) """

        self.assertEqual(self.customer.has_perm('change_user', self.customer), True)
        
    def test_customer_created_admin_group_view_permission(self):
        """ Test that when a customer is created, Admin group has view permission for this customer """
        # add user to Admin Group
        self.user.groups.add(self.admin_group)
        
        # Check that user in Admin Group has view permissions for this customer 
        self.assertEqual(self.user.has_perm('view_user', self.customer), True)
        
        # remove user from Admin Group
        self.user.groups.remove(self.admin_group)
        
        # Check that user does not have view permissions for this customer
        self.assertEqual(self.user.has_perm('view_user', self.customer), False)
        
    def test_customer_created_admin_group_change_permission(self):
        """ Test that when a customer is created, Admin group has change permission for this customer """
        # add user to Admin Group
        self.user.groups.add(self.admin_group)
        
        # Check that user in Admin Group has change permissions for this customer
        self.assertEqual(self.user.has_perm('change_user', self.customer), True)
        
        # remove user from Admin Group
        self.user.groups.remove(self.admin_group)
        
        # Check that user does not have change permissions for this customer
        self.assertEqual(self.user.has_perm('change_user', self.customer), False)
        
    def test_customer_created_admin_group_delete_permission(self):
        """ Test that when a customer is created, Admin group has delete permission for this customer"""
        # add user to Admin Group
        self.user.groups.add(self.admin_group)
        
        # Check that user in Admin Group has delete permission for this customer
        self.assertEqual(self.user.has_perm('delete_user', self.customer), True)
        
        # remove user from Admin Group
        self.user.groups.remove(self.admin_group)
        
        # Check that user does not have delete permission for this customer
        self.assertEqual(self.user.has_perm('delete_user', self.customer), False)
        
    def test_customer_created_employee_manager_group_view_permission(self):
        """ Test that when a customer is created, Employee Manager Group has view permission for this customer """
        # add user to Employee Manager Group
        self.user.groups.add(self.employee_manager_group)
        
        # Check that user in Employee Manager Group has view permission for this customer
        self.assertEqual(self.user.has_perm('view_user', self.customer), True)
        
        # remove user from Employee Manager Group
        self.user.groups.remove(self.employee_manager_group)
        
        # Check that user does not have view permission for this customer
        self.assertEqual(self.user.has_perm('view_user', self.customer), False)
        
    def test_customer_created_employee_manager_group_change_permission(self):
        """ Test that when a customer is created, Employee Manager Group has change permission for this customer """
        # add user to Employee Manager Group
        self.user.groups.add(self.employee_manager_group)
        
        # Check that user in Employee Manager Group has change permission for this customer
        self.assertEqual(self.user.has_perm('change_user', self.customer), True)
        
        # remove user from Employee Manager Group
        self.user.groups.remove(self.employee_manager_group)
        
        # Check that user does not have change permission for this customer
        self.assertEqual(self.user.has_perm('change_user', self.customer), False)
        
    def test_customer_created_employee_manager_group_delete_permission(self):
        """ Test that when a customer is created, Employee Manager Group has delete permission for this customer """
        # add user to Employee Manager Group
        self.user.groups.add(self.employee_manager_group)
        
        # Check that user in Employee Manager Group has delete permission for this customer
        self.assertEqual(self.user.has_perm('delete_user', self.customer), True)
        
        # remove user from Employee Manager Group
        self.user.groups.remove(self.employee_manager_group)
        
        # Check that user does not have delete permission for this customer
        self.assertEqual(self.user.has_perm('delete_user', self.customer), False)
        
    def test_customer_created_employee_standard_group_view_permission(self):
        """ Test that when a customer is created, Employee Standard Group has view permission for this customer """
        # add user to Employee Standard Group
        self.user.groups.add(self.employee_standard_group)
        
        # Check that user in Employee Standard Group has view permission for this customer
        self.assertEqual(self.user.has_perm('view_user', self.customer), True)
        
        # remove user from Employee Standard Group
        self.user.groups.remove(self.employee_standard_group)
        
        # Check that user does not have view permission for this customer
        self.assertEqual(self.user.has_perm('view_user', self.customer), False)
        
    def test_customer_created_added_to_customer_group(self):
        """ Test that when a customer is created, they are added to Customer group """
        
        self.assertEqual(self.customer.groups.filter(name='Customer').exists(), True)
        
        # check that customer is not in Admin group
        self.assertEqual(self.user.groups.filter(name='Admins').exists(), False)
        
        # check that customer is not in Employee Manager group
        self.assertEqual(self.user.groups.filter(name='Employee - Manager').exists(), False)
        
        # check that customer is not in Employee Standard group
        self.assertEqual(self.user.groups.filter(name='Employee - Standard').exists(), False)


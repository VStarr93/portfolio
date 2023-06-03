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

# Create a TestCase for Customer Profile Set Permissions Reciever 
# crm_user.tests.signals.test_handlers.CustomerProfileSetPermsTests
class CustomerProfileSetPermsTests(TestCase):
    """ Define a TestCase for Customer Profile Set Permissions Reciever """
    def setUp(self):
        """ Define a setUp method for CustomerProfileSetPermsTests to create test users and groups """
        # Create customer 
        self.customer = Customer.objects.create_user(email="test@example.com")
        self.profile = CustomerProfile.objects.get(user=self.customer)
        self.user = User.objects.create_user(email="test1@example.com")
        # Get Admin Group
        self.admin_group = Group.objects.get(name='Admins')
        self.employee_manager_group = Group.objects.get(name='Employee - Manager')
        self.employee_standard_group = Group.objects.get(name='Employee - Standard')
        
    def test_customer_profile_created_customer_view_permission(self):
        """ Test that when a customer profile is created, the customer receives view permission for that object (their profile) """

        self.assertEqual(self.customer.has_perm('view_customerprofile', self.profile), True)
        
    def test_customer_profile_created_customer_change_permission(self):
        """ Test that when a customer profile is created, the customer receives change permission for that object (their profile) """

        self.assertEqual(self.customer.has_perm('change_customerprofile', self.profile), True)
        
    def test_customer_profile_created_admin_group_view_permission(self):
        """ Test that when a customer profile is created, Admin group has view permission for this profile """
        # add user to Admin Group
        self.user.groups.add(self.admin_group)
        
        # Check that user in Admin Group has view permissions for this profile 
        self.assertEqual(self.user.has_perm('view_customerprofile', self.profile), True)
        
        # remove user from Admin Group
        self.user.groups.remove(self.admin_group)
        
        # Check that user does not have view permissions for this profile
        self.assertEqual(self.user.has_perm('view_customerprofile', self.profile), False)
        
    def test_customer_profile_created_admin_group_delete_permission(self):
        """ Test that when a customer profile is created, Admin group has delete permission for this profile"""
        # add user to Admin Group
        self.user.groups.add(self.admin_group)
        
        # Check that user in Admin Group has delete permission for this profile
        self.assertEqual(self.user.has_perm('delete_customerprofile', self.profile), True)
        
        # remove user from Admin Group
        self.user.groups.remove(self.admin_group)
        
        # Check that user does not have delete permission for this profile
        self.assertEqual(self.user.has_perm('delete_customerprofile', self.profile), False)
        
    def test_customer_profile_created_employee_manager_group_view_permission(self):
        """ Test that when a customer profile is created, Employee Manager Group has view permission for this profile """
        # add user to Employee Manager Group
        self.user.groups.add(self.employee_manager_group)
        
        # Check that user in Employee Manager Group has view permission for this profile
        self.assertEqual(self.user.has_perm('view_customerprofile', self.profile), True)
        
        # remove user from Employee Manager Group
        self.user.groups.remove(self.employee_manager_group)
        
        # Check that user does not have view permission for this profile
        self.assertEqual(self.user.has_perm('view_customerprofile', self.profile), False)
        
    def test_customer_profile_created_employee_manager_group_delete_permission(self):
        """ Test that when a customer profile is created, Employee Manager Group has delete permission for this profile """
        # add user to Employee Manager Group
        self.user.groups.add(self.employee_manager_group)
        
        # Check that user in Employee Manager Group has delete permission for this profile
        self.assertEqual(self.user.has_perm('delete_customerprofile', self.profile), True)
        
        # remove user from Employee Manager Group
        self.user.groups.remove(self.employee_manager_group)
        
        # Check that user does not have delete permission for this profile
        self.assertEqual(self.user.has_perm('delete_customerprofile', self.profile), False)
        
    def test_customer_profile_created_employee_standard_group_view_permission(self):
        """ Test that when a customer profile is created, Employee Standard Group has view permission for this profile """
        # add user to Employee Standard Group
        self.user.groups.add(self.employee_standard_group)
        
        # Check that user in Employee Standard Group has view permission for this profile
        self.assertEqual(self.user.has_perm('view_customerprofile', self.profile), True)
        
        # remove user from Employee Standard Group
        self.user.groups.remove(self.employee_standard_group)
        
        # Check that user does not have view permission for this profile
        self.assertEqual(self.user.has_perm('view_customerprofile', self.profile), False)
        
# Create a TestCase for Employee Set Permissions Reciever 
# crm_user.tests.signals.test_handlers.EmployeeSetPermsTests
class EmployeeSetPermsTests(TestCase):
    """ Define a TestCase for Employee Set Permissions Reciever """
    def setUp(self):
        """ Define a setUp method for EmployeeSetPermsTests to create test users and groups """
        # Create employee 
        self.employee = Employee.objects.create_user(email="test@example.com")
        self.user = User.objects.create_user(email="test1@example.com")
        # Get Admin Group
        self.admin_group = Group.objects.get(name='Admins')
        self.employee_manager_group = Group.objects.get(name='Employee - Manager')
        self.employee_standard_group = Group.objects.get(name='Employee - Standard')
          
    def test_employee_created_employee_view_permission(self):
        """ Test that when an employee is created, they receive view permission for that object (their user) """

        self.assertEqual(self.employee.has_perm('view_user', self.employee), True)
        
    def test_employee_created_employee_change_permission(self):
        """ Test that when an employee is created, they receive change permission for that object (their user) """

        self.assertEqual(self.employee.has_perm('change_user', self.employee), True)
        
    def test_employee_created_admin_group_view_permission(self):
        """ Test that when an employee is created, Admin group has view permission for this employee """
        # add user to Admin Group
        self.user.groups.add(self.admin_group)
        
        # Check that user in Admin Group has view permissions for this employee 
        self.assertEqual(self.user.has_perm('view_user', self.employee), True)
        
        # remove user from Admin Group
        self.user.groups.remove(self.admin_group)
        
        # Check that user does not have view permissions for this employee
        self.assertEqual(self.user.has_perm('view_user', self.employee), False)
        
    def test_employee_created_admin_group_change_permission(self):
        """ Test that when an employee is created, Admin group has change permission for this employee """
        # add user to Admin Group
        self.user.groups.add(self.admin_group)
        
        # Check that user in Admin Group has change permissions for this employee
        self.assertEqual(self.user.has_perm('change_user', self.employee), True)
        
        # remove user from Admin Group
        self.user.groups.remove(self.admin_group)
        
        # Check that user does not have change permissions for this employee
        self.assertEqual(self.user.has_perm('change_user', self.employee), False)
        
    def test_employee_created_admin_group_delete_permission(self):
        """ Test that when an employee is created, Admin group has delete permission for this employee"""
        # add user to Admin Group
        self.user.groups.add(self.admin_group)
        
        # Check that user in Admin Group has delete permission for this employee
        self.assertEqual(self.user.has_perm('delete_user', self.employee), True)
        
        # remove user from Admin Group
        self.user.groups.remove(self.admin_group)
        
        # Check that user does not have delete permission for this employee
        self.assertEqual(self.user.has_perm('delete_user', self.employee), False)
        
    def test_employee_created_employee_manager_group_view_permission(self):
        """ Test that when an employee is created, Employee Manager Group has view permission for this employee """
        # add user to Employee Manager Group
        self.user.groups.add(self.employee_manager_group)
        
        # Check that user in Employee Manager Group has view permission for this employee
        self.assertEqual(self.user.has_perm('view_user', self.employee), True)
        
        # remove user from Employee Manager Group
        self.user.groups.remove(self.employee_manager_group)
        
        # Check that user does not have view permission for this employee
        self.assertEqual(self.user.has_perm('view_user', self.employee), False)
        
    def test_employee_created_employee_manager_group_change_permission(self):
        """ Test that when an employee is created, Employee Manager Group has change permission for this employee """
        # add user to Employee Manager Group
        self.user.groups.add(self.employee_manager_group)
        
        # Check that user in Employee Manager Group has change permission for this employee
        self.assertEqual(self.user.has_perm('change_user', self.employee), True)
        
        # remove user from Employee Manager Group
        self.user.groups.remove(self.employee_manager_group)
        
        # Check that user does not have change permission for this employee
        self.assertEqual(self.user.has_perm('change_user', self.employee), False)
        
    def test_employee_created_employee_manager_group_delete_permission(self):
        """ Test that when an employee is created, Employee Manager Group has delete permission for this employee """
        # add user to Employee Manager Group
        self.user.groups.add(self.employee_manager_group)
        
        # Check that user in Employee Manager Group has delete permission for this employee
        self.assertEqual(self.user.has_perm('delete_user', self.employee), True)
        
        # remove user from Employee Manager Group
        self.user.groups.remove(self.employee_manager_group)
        
        # Check that user does not have delete permission for this employee
        self.assertEqual(self.user.has_perm('delete_user', self.employee), False)
        
    def test_employee_created_added_to_employee_standard_group(self):
        """ Test that when an employee is created, they are added to Employee group """
        
        self.assertEqual(self.employee.groups.filter(name='Employee - Standard').exists(), True)
        
        # check that employee is not in Admin group
        self.assertEqual(self.employee.groups.filter(name='Admins').exists(), False)
        
        # check that employee is not in Employee Manager group
        self.assertEqual(self.employee.groups.filter(name='Employee - Manager').exists(), False)
        
        # check that employee is not in Customer group
        self.assertEqual(self.employee.groups.filter(name='Customer').exists(), False)
   
# Create a TestCase for Employee Profile Set Permissions Reciever 
# crm_user.tests.signals.test_handlers.EmployeeProfileSetPermsTests
class EmployeeProfileSetPermsTests(TestCase):
    """ Define a TestCase for Employee Profile Set Permissions Reciever """
    def setUp(self):
        """ Define a setUp method for EmployeeProfileSetPermsTests to create test users and groups """
        # Create Employee 
        self.employee = Employee.objects.create_user(email="test@example.com")
        self.profile = EmployeeProfile.objects.get(user=self.employee)
        self.user = User.objects.create_user(email="test1@example.com")
        # Get Admin Group
        self.admin_group = Group.objects.get(name='Admins')
        self.employee_manager_group = Group.objects.get(name='Employee - Manager')
        self.employee_standard_group = Group.objects.get(name='Employee - Standard')
        
    def test_employee_profile_created_employee_view_permission(self):
        """ Test that when an employee profile is created, the employee receives view permission for that object (their profile) """

        self.assertEqual(self.employee.has_perm('view_employeeprofile', self.profile), True)
        
    def test_employee_profile_created_employee_change_permission(self):
        """ Test that when an employee profile is created, the employee receives change permission for that object (their profile) """

        self.assertEqual(self.employee.has_perm('change_employeeprofile', self.profile), True)
        
    def test_employee_profile_created_admin_group_view_permission(self):
        """ Test that when an employee profile is created, Admin group has view permission for this profile """
        # add user to Admin Group
        self.user.groups.add(self.admin_group)
        
        # Check that user in Admin Group has view permissions for this profile 
        self.assertEqual(self.user.has_perm('view_employeeprofile', self.profile), True)
        
        # remove user from Admin Group
        self.user.groups.remove(self.admin_group)
        
        # Check that user does not have view permissions for this profile
        self.assertEqual(self.user.has_perm('view_employeeprofile', self.profile), False)
        
    def test_employee_profile_created_admin_group_delete_permission(self):
        """ Test that when an employee profile is created, Admin group has delete permission for this profile"""
        # add user to Admin Group
        self.user.groups.add(self.admin_group)
        
        # Check that user in Admin Group has delete permission for this profile
        self.assertEqual(self.user.has_perm('delete_employeeprofile', self.profile), True)
        
        # remove user from Admin Group
        self.user.groups.remove(self.admin_group)
        
        # Check that user does not have delete permission for this profile
        self.assertEqual(self.user.has_perm('delete_employeeprofile', self.profile), False)
        
    def test_employee_profile_created_admin_group_change_hire_date_permission(self):
        """ Test that when an employee profile is created, Admin group has change hire date permission for this profile"""
        # add user to Admin Group
        self.user.groups.add(self.admin_group)
        
        # Check that user in Admin Group has change hire date permission for this profile
        self.assertEqual(self.user.has_perm('change_employee_hire_date', self.profile), True)
        
        # remove user from Admin Group
        self.user.groups.remove(self.admin_group)
        
        # Check that user does not have change hire date permission for this profile
        self.assertEqual(self.user.has_perm('change_employee_hire_date', self.profile), False)
        
    def test_employee_profile_created_admin_group_change_status_permission(self):
        """ Test that when an employee profile is created, Admin group has change status permission for this profile """
        # add user to Admin Group
        self.user.groups.add(self.admin_group)
        
        # Check that user in Admin Group has change status permissions for this profile 
        self.assertEqual(self.user.has_perm('change_employee_status', self.profile), True)
        
        # remove user from Admin Group
        self.user.groups.remove(self.admin_group)
        
        # Check that user does not have change status permissions for this profile
        self.assertEqual(self.user.has_perm('change_employee_status', self.profile), False)
        
    def test_employee_profile_created_admin_group_make_manager_permission(self):
        """ Test that when an employee profile is created, Admin group has make manager permission for this profile"""
        # add user to Admin Group
        self.user.groups.add(self.admin_group)
        
        # Check that user in Admin Group has make manager permission for this profile
        self.assertEqual(self.user.has_perm('make_employee_manager', self.profile), True)
        
        # remove user from Admin Group
        self.user.groups.remove(self.admin_group)
        
        # Check that user does not have make manager permission for this profile
        self.assertEqual(self.user.has_perm('make_employee_manager', self.profile), False)
        
    def test_employee_profile_created_employee_manager_group_view_permission(self):
        """ Test that when an employee profile is created, Employee Manager Group has view permission for this profile """
        # add user to Employee Manager Group
        self.user.groups.add(self.employee_manager_group)
        
        # Check that user in Employee Manager Group has view permission for this profile
        self.assertEqual(self.user.has_perm('view_employeeprofile', self.profile), True)
        
        # remove user from Employee Manager Group
        self.user.groups.remove(self.employee_manager_group)
        
        # Check that user does not have view permission for this profile
        self.assertEqual(self.user.has_perm('view_employeeprofile', self.profile), False)
        
    def test_employee_profile_created_employee_manager_group_delete_permission(self):
        """ Test that when an employee profile is created, Employee Manager Group has delete permission for this profile """
        # add user to Employee Manager Group
        self.user.groups.add(self.employee_manager_group)
        
        # Check that user in Employee Manager Group has delete permission for this profile
        self.assertEqual(self.user.has_perm('delete_employeeprofile', self.profile), True)
        
        # remove user from Employee Manager Group
        self.user.groups.remove(self.employee_manager_group)
        
        # Check that user does not have delete permission for this profile
        self.assertEqual(self.user.has_perm('delete_employeeprofile', self.profile), False)
        
    def test_employee_profile_created_employee_manager_group_change_hire_date_permission(self):
        """ Test that when an employee profile is created, Employee Manager Group has change hire date permission for this profile """
        # add user to Employee Manager Group
        self.user.groups.add(self.employee_manager_group)
        
        # Check that user in Employee Manager Group has change hire date permission for this profile
        self.assertEqual(self.user.has_perm('change_employee_hire_date', self.profile), True)
        
        # remove user from Employee Manager Group
        self.user.groups.remove(self.employee_manager_group)
        
        # Check that user does not have change hire date permission for this profile
        self.assertEqual(self.user.has_perm('change_employee_hire_date', self.profile), False)
        
    def test_employee_profile_created_employee_manager_group_change_status_permission(self):
        """ Test that when an employee profile is created, Employee Manager Group has change status permission for this profile """
        # add user to Employee Manager Group
        self.user.groups.add(self.employee_manager_group)
        
        # Check that user in Employee Manager Group has change status permission for this profile
        self.assertEqual(self.user.has_perm('change_employee_status', self.profile), True)
        
        # remove user from Employee Manager Group
        self.user.groups.remove(self.employee_manager_group)
        
        # Check that user does not have change status permission for this profile
        self.assertEqual(self.user.has_perm('change_employee_status', self.profile), False)
        
    def test_employee_profile_created_employee_manager_group_make_manager_permission(self):
        """ Test that when an employee profile is created, Employee Manager Group has make manager permission for this profile """
        # add user to Employee Manager Group
        self.user.groups.add(self.employee_manager_group)
        
        # Check that user in Employee Manager Group has make manager permission for this profile
        self.assertEqual(self.user.has_perm('make_employee_manager', self.profile), True)
        
        # remove user from Employee Manager Group
        self.user.groups.remove(self.employee_manager_group)
        
        # Check that user does not have make manager permission for this profile
        self.assertEqual(self.user.has_perm('make_employee_manager', self.profile), False)
        
    def test_employee_profile_update_nonmanager_to_manager_permission(self):
        """ Test that if a nonmanager gets changed to manager, that permissions are correctly updated """
        # Check that employee profile is set as nonmanager
        self.assertEqual(self.profile.is_manager, False)
        
        # Check that employee has permissions for nonmanager
        self.assertIn(self.employee_standard_group, self.employee.groups.all())
        self.assertNotIn(self.employee_manager_group, self.employee.groups.all())
        
        # Change employee profile to manager
        self.profile.is_manager = True
        self.profile.save()
        
        # Check that employee has permissions for manager
        self.assertIn(self.employee_manager_group, self.employee.groups.all())
        self.assertNotIn(self.employee_standard_group, self.employee.groups.all())
        
    def test_employee_profile_update_manager_to_nonmanager_permission(self):
        """" Test that if a manager gets changed to nonmanager, that permissions are correctly updated """
        # Check that employee profile is set as nonmanager
        self.assertEqual(self.profile.is_manager, False)
        
        # Check that employee has permissions for nonmanager
        self.assertIn(self.employee_standard_group, self.employee.groups.all())
        self.assertNotIn(self.employee_manager_group, self.employee.groups.all())
        
        # Change employee profile to manager
        self.profile.is_manager = True
        self.profile.save()
        
        # Check that employee has permissions for manager
        self.assertIn(self.employee_manager_group, self.employee.groups.all())
        self.assertNotIn(self.employee_standard_group, self.employee.groups.all())
        
        # Change employee profile to nonmanager
        self.profile.is_manager = False
        self.profile.save()
        
        # Check that employee has permissions for nonmanager
        self.assertIn(self.employee_standard_group, self.employee.groups.all())
        self.assertNotIn(self.employee_manager_group, self.employee.groups.all())
        
# Create a TestCase for Admin Set Permissions Reciever 
# crm_user.tests.signals.test_handlers.AdminSetPermsTests
class AdminSetPermsTests(TestCase):
    """ Define a TestCase for Admin Set Permissions Reciever """
    def setUp(self):
        """ Define a setUp method for AdminSetPermsTests to create test users and groups """
        # Create admin 
        self.admin = Admin.objects.create_user(email="test@example.com")
        self.user = User.objects.create_user(email="test1@example.com")
        # Get Admin Group
        self.admin_group = Group.objects.get(name='Admins')
        self.employee_manager_group = Group.objects.get(name='Employee - Manager')
          
    def test_admin_created_admin_view_permission(self):
        """ Test that when an admin is created, they receive view permission for that object (their user) """

        self.assertEqual(self.admin.has_perm('view_user', self.admin), True)
        
    def test_admin_created_admin_change_permission(self):
        """ Test that when an admin is created, they receive change permission for that object (their user) """

        self.assertEqual(self.admin.has_perm('change_user', self.admin), True)
        
    def test_admin_created_admin_delete_permission(self):
        """ Test that when an admin is created, they receive delete permission for that object (their user) """

        self.assertEqual(self.admin.has_perm('delete_user', self.admin), True)
        
    def test_admin_created_admin_group_view_permission(self):
        """ Test that when an admin is created, Admin group has view permission for this admin """
        # add user to Admin Group
        self.user.groups.add(self.admin_group)
        
        # Check that user in Admin Group has view permissions for this admin 
        self.assertEqual(self.user.has_perm('view_user', self.admin), True)
        
        # remove user from Admin Group
        self.user.groups.remove(self.admin_group)
        
        # Check that user does not have view permissions for this admin
        self.assertEqual(self.user.has_perm('view_user', self.admin), False)
        
    def test_admin_created_admin_group_change_permission(self):
        """ Test that when an admin is created, Admin group has change permission for this admin """
        # add user to Admin Group
        self.user.groups.add(self.admin_group)
        
        # Check that user in Admin Group has change permissions for this admin
        self.assertEqual(self.user.has_perm('change_user', self.admin), True)
        
        # remove user from Admin Group
        self.user.groups.remove(self.admin_group)
        
        # Check that user does not have change permissions for this admin
        self.assertEqual(self.user.has_perm('change_user', self.admin), False)
        
    def test_admin_created_admin_group_delete_permission(self):
        """ Test that when an admin is created, Admin group has delete permission for this admin"""
        # add user to Admin Group
        self.user.groups.add(self.admin_group)
        
        # Check that user in Admin Group has delete permission for this admin
        self.assertEqual(self.user.has_perm('delete_user', self.admin), True)
        
        # remove user from Admin Group
        self.user.groups.remove(self.admin_group)
        
        # Check that user does not have delete permission for this admin
        self.assertEqual(self.user.has_perm('delete_user', self.admin), False)
        
    def test_admin_created_employee_manager_group_view_permission(self):
        """ Test that when an admin is created, Employee Manager Group has view permission for this admin """
        # add user to Employee Manager Group
        self.user.groups.add(self.employee_manager_group)
        
        # Check that user in Employee Manager Group has view permission for this admin
        self.assertEqual(self.user.has_perm('view_user', self.admin), True)
        
        # remove user from Employee Manager Group
        self.user.groups.remove(self.employee_manager_group)
        
        # Check that user does not have view permission for this admin
        self.assertEqual(self.user.has_perm('view_user', self.admin), False)
        
    def test_admin_created_added_to_admin_group(self):
        """ Test that when an admin is created, they are added to Admin group """
        
        self.assertEqual(self.admin.groups.filter(name='Admins').exists(), True)
        
        # check that employee is not in Employee Manager group
        self.assertEqual(self.admin.groups.filter(name='Employee - Manager').exists(), False)
        
        # check that employee is not in Employee Standard group
        self.assertEqual(self.admin.groups.filter(name='Employee - Standard').exists(), False)
        
        # check that employee is not in Customer group
        self.assertEqual(self.admin.groups.filter(name='Customers').exists(), False)
  
# Create a TestCase for Admin Profile Set Permissions Reciever 
# crm_user.tests.signals.test_handlers.AdminProfileSetPermsTests
class AdminProfileSetPermsTests(TestCase):
    """ Define a TestCase for Admin Profile Set Permissions Reciever """
    def setUp(self):
        """ Define a setUp method for AdminProfileSetPermsTests to create test users and groups """
        # Create Admin 
        self.admin = Admin.objects.create_user(email="test@example.com")
        self.profile = AdminProfile.objects.get(user=self.admin)
        self.user = User.objects.create_user(email="test1@example.com")
        # Get Admin Group
        self.admin_group = Group.objects.get(name='Admins')
        self.employee_manager_group = Group.objects.get(name='Employee - Manager')
        self.employee_standard_group = Group.objects.get(name='Employee - Standard')
        
    def test_admin_profile_created_admin_view_permission(self):
        """ Test that when an admin profile is created, the admin receives view permission for that object (their profile) """

        self.assertEqual(self.admin.has_perm('view_adminprofile', self.profile), True)
        
    def test_admin_profile_created_admin_change_permission(self):
        """ Test that when an admin profile is created, the admin receives change permission for that object (their profile) """

        self.assertEqual(self.admin.has_perm('change_adminprofile', self.profile), True)
         
    def test_admin_profile_created_admin_delete_permission(self):
        """ Test that when an admin profile is created, the admin receives change permission for that object (their profile) """

        self.assertEqual(self.admin.has_perm('change_adminprofile', self.profile), True)
        
    def test_admin_profile_created_admin_group_view_permission(self):
        """ Test that when an admin profile is created, Admin group has view permission for this profile """
        # add user to Admin Group
        self.user.groups.add(self.admin_group)
        
        # Check that user in Admin Group has view permissions for this profile 
        self.assertEqual(self.user.has_perm('view_adminprofile', self.profile), True)
        
        # remove user from Admin Group
        self.user.groups.remove(self.admin_group)
        
        # Check that user does not have view permissions for this profile
        self.assertEqual(self.user.has_perm('view_adminprofile', self.profile), False)
        
    def test_admin_profile_created_admin_group_delete_permission(self):
        """ Test that when an admin profile is created, Admin group has delete permission for this profile"""
        # add user to Admin Group
        self.user.groups.add(self.admin_group)
        
        # Check that user in Admin Group has delete permission for this profile
        self.assertEqual(self.user.has_perm('delete_adminprofile', self.profile), True)
        
        # remove user from Admin Group
        self.user.groups.remove(self.admin_group)
        
        # Check that user does not have delete permission for this profile
        self.assertEqual(self.user.has_perm('delete_adminprofile', self.profile), False)
        
    def test_admin_profile_created_admin_group_change_status_permission(self):
        """ Test that when an admin profile is created, Admin group has change status permission for this profile """
        # add user to Admin Group
        self.user.groups.add(self.admin_group)
        
        # Check that user in Admin Group has change status permissions for this profile 
        self.assertEqual(self.user.has_perm('change_admin_status', self.profile), True)
        
        # remove user from Admin Group
        self.user.groups.remove(self.admin_group)
        
        # Check that user does not have change status permissions for this profile
        self.assertEqual(self.user.has_perm('change_admin_status', self.profile), False)
        
    def test_admin_profile_created_admin_group_make_manager_permission(self):
        """ Test that when an admin profile is created, Admin group has make manager permission for this profile"""
        # add user to Admin Group
        self.user.groups.add(self.admin_group)
        
        # Check that user in Admin Group has make manager permission for this profile
        self.assertEqual(self.user.has_perm('make_admin_manager', self.profile), True)
        
        # remove user from Admin Group
        self.user.groups.remove(self.admin_group)
        
        # Check that user does not have make manager permission for this profile
        self.assertEqual(self.user.has_perm('make_admin_manager', self.profile), False)
           
# Create a TestCase for Employee Profile Change Permissions Receiver
# crm_user.tests.signals.test_handlers.EmployeeProfileChangePermsTests
class EmployeeProfileChangePermsTests(TestCase):
    """ Define a TestCase for Employee Profile Change Permissions Receiver """
    def setUp(self):
        """ Define a setUp method for Employee Profile Change Permissions Receiver to create test users and groups """
        self.employee = Employee.objects.create_user(email='employee@example.com')
        self.profile = EmployeeProfile.objects.get(user=self.employee)
        self.user = User.objects.create_user(email='user@example.com')
        # Set Group Variables
        self.employee_group = Group.objects.get(name='Employee - Standard')
        self.employee_manager_group = Group.objects.get(name='Employee - Manager')
        
    def test_employee_profile_is_manager_employee_manager_group(self):
        """ Test that if an employee profile is manager is True, then employee user moves to Employee Manager Group """
        # Check that employee is in employee standard group
        self.assertEqual(self.employee.groups.filter(name='Employee - Standard').exists(), True)
        
        # Update employee profile to is manager is true
        self.profile.is_manager = True
        self.profile.save()
        
        # Check that employee is in employee manager group
        self.assertEqual(self.employee.groups.filter(name='Employee - Manager').exists(), True)
        
        # Check that employee is not in employee standard group
        self.assertEqual(self.employee.groups.filter(name='Employee - Standard').exists(), False)
        
    def test_employee_profile_is_not_manager_employee_standard_group(self):
        """ Test that if an employee profile is manager is False, then employee user moves to Employee Standard Group """
        # Update employee profile to is manager is False
        self.profile.is_manager = False
        self.profile.save()
        
        # Check that employee is in employee standard group
        self.assertEqual(self.employee.groups.filter(name='Employee - Standard').exists(), True)
        
        # Check that employee is not in employee manager group
        self.assertEqual(self.employee.groups.filter(name='Employee - Manager').exists(), False)
        
# create a TestCase for Address Set Permissions Receiver 
# crm_user.tests.signals.test_handlers.AddressSetPermsTests 
class AddressSetPermsTests(TestCase):
    """ Define a TestCase for Address Set Permissions Receiver """
    def setUp(self):
        """ Define a setUp method for Address Set Permissions Receiver to create test users and addresses """
        self.user1 = User.objects.create_user(email='user1@example.com')
        self.user = User.objects.create_user(email='user@example.com')
        self.address = Address.objects.create(
            name = 'home',
            type = 'RESIDENTIAL',
            address_line1 = '123 Sara lane',
            city = 'Houston', 
            state = 'TX',
            zip = 77301,
            user = self.user,
        )
        # Get Groups
        self.admin_group = Group.objects.get(name='Admins')
        self.employee_manager_group = Group.objects.get(name='Employee - Manager')
        self.employee_standard_group = Group.objects.get(name='Employee - Standard')
        
    def test_new_address_user_view_permission(self):
        """ Test that when a new address is created, the user has view permission for that address """
        self.assertEqual(self.user.has_perm('view_address', self.address), True)
        
    def test_new_address_user_change_permission(self):
        """ Test that when a new address is created, the user has change permission for that address """
        self.assertEqual(self.user.has_perm('change_address', self.address), True)
        
    def test_new_address_user_disable_permission(self):
        """ Test that when a new address is created, the user has disable permission for that address """
        self.assertEqual(self.user.has_perm('disable_address', self.address), True)
        
    def test_new_address_admin_group_view_permission(self):
        """ Test that when a new address is created, Admin Group has view permission for that address """
        # add user to admin group
        self.user1.groups.add(self.admin_group)
        
        # Check that user in admin group has view permission
        self.assertEqual(self.user1.has_perm('view_address', self.address), True)
        
        # remove user from admin group
        self.user1.groups.remove(self.admin_group)
        
        # Check that user does not have view permission
        self.assertEqual(self.user1.has_perm('view_address', self.address), False)
        
    def test_new_address_admin_group_change_permission(self):
        """ Test that when a new address is created, Admin Group has change permission for that address """
        # add user to admin group
        self.user1.groups.add(self.admin_group)
        
        # Check that user in admin group has change permission
        self.assertEqual(self.user1.has_perm('change_address', self.address), True) 
        
        # remove user from admin group
        self.user1.groups.remove(self.admin_group)
        
        # Check that user does not have change permission
        self.assertEqual(self.user1.has_perm('change_address', self.address), False)
        
    def test_new_address_admin_group_delete_permission(self):
        """ Test that when a new address is created, Admin Group has delete permission for that address """
        # add user to admin group
        self.user1.groups.add(self.admin_group)
        
        # Check that user in admin group has delete permission for that address
        self.assertEqual(self.user1.has_perm('delete_address', self.address), True) 
        
        # remove user from admin group
        self.user1.groups.remove(self.admin_group)
        
        # Check that user does not have delete permission 
        self.assertEqual(self.user1.has_perm('delete_address', self.address), False)
        
    def test_new_address_admin_group_disable_permission(self):
        """ Test that when a new address is created, Admin Group has disable permission for that address """
        # add user to admin group
        self.user1.groups.add(self.admin_group)
        
        # Check that user in admin group has disable permission for that address
        self.assertEqual(self.user1.has_perm('disable_address', self.address), True) 
        
        # remove user from admin group
        self.user1.groups.remove(self.admin_group)
        
        # Check that user does not have disable permission for that address
        self.assertEqual(self.user1.has_perm('disable_address', self.address), False)
        
    def test_new_address_employee_manager_group_view_permission(self):
        """ Test that when a new addres is created, Employee Manager Group has view permission for that address """
        # add user to employee manager group
        self.user1.groups.add(self.employee_manager_group)
        
        # Check that user in employee manager group has view permission for that address
        self.assertEqual(self.user1.has_perm('view_address', self.address), True)
        
        # remove user from employee manager group
        self.user1.groups.remove(self.employee_manager_group)
        
        # check that user does not have view permission for that address
        self.assertEqual(self.user1.has_perm('view_address', self.address), False)
        
    def test_new_address_employee_manager_group_change_permission(self):
        """ Test that when a new address is created, Employee Manager Group has change permission for that address """
        # add user to employee manager group
        self.user1.groups.add(self.employee_manager_group)
        
        # Check that user in Employee Manager Group has change permission for that address
        self.assertEqual(self.user1.has_perm('change_address', self.address), True)
        
        # remove user from employee manager group
        self.user1.groups.remove(self.employee_manager_group)
        
        # Check that user does not have change permission for that address
        self.assertEqual(self.user1.has_perm('change_address', self.address), False)
        
    def test_new_address_employee_manager_group_disable_permission(self):
        """" Test that when a new address is created, Employee Manager Group has disable permission for that address """
        # add user to employee manager group
        self.user1.groups.add(self.employee_manager_group)
        
        # Check that user in employee manager group has disable permission for that address
        self.assertEqual(self.user1.has_perm('disable_address', self.address), True) 
        
        # remove user from employee manager group
        self.user1.groups.remove(self.employee_manager_group)
        
        # Check that user does not have disable permission for that address
        self.assertEqual(self.user1.has_perm('disable_address', self.address), False)
        
    def test_new_address_employee_standard_group_view_permission(self):
        """ Test that when a new address is created, Employee Standard Group has view permission for that address """
        # add user to employee standard group
        self.user1.groups.add(self.employee_standard_group)
        
        # Check that user in employee standard group has view permission for that address
        self.assertEqual(self.user1.has_perm('view_address', self.address), True)
        
        # remove user from employee standard group
        self.user1.groups.remove(self.employee_standard_group)
        
        # Check that user does not have view permission for that address
        self.assertEqual(self.user1.has_perm('view_address', self.address), False)
        
# create a TestCase for Address Change Update Last Modfied Receiver 
class AddressChangeUpdateLastModifiedTests(TestCase):
    """ Define a TestCase for Address Change Update Last Modfied Receiver """
    def setUp(self):
        """ Define a setUp method for Address Change Update Last Modfied Receiver """
        self.user = User.objects.create_user(email='user@example.com')
        self.address = Address.objects.create(
            name = 'home',
            type = 'RESIDENTIAL',
            address_line1 = '123 Sara lane',
            city = 'Houston', 
            state = 'TX',
            zip = 77301,
            user = self.user,
        )
        
    @freeze_time(timezone.now())
    def test_user_updated_on_address_change(self):
        """ Test that User last_modified field is updated on Address Change """
        # Check that user last modified does not equal current timestamp
        self.assertNotEqual(self.user.last_modified, timezone.now())
        
        # Update address
        self.address.name = 'work'
        self.address.save()
        
        # Check that user last modified was updated with current timestamp
        self.assertEqual(self.user.last_modified, timezone.now())
        
#./crm_user/tests/forms/test_AddressForm.py
#-------------------------------------------------------------
#-------------------------------------------------------------
# IMPORTS

from django.test import TestCase
from crm_user.forms import AddressForm
from crm_user.models import User, Customer, Admin, Employee
from django.core.exceptions import ValidationError 
import datetime 

# For Testing Email Services
from django.core import mail 


#-------------------------------------------------------------
#-------------------------------------------------------------
# Create your Variables here.


#-------------------------------------------------------------
#-------------------------------------------------------------
# Create your Address Form tests here.

# Create a TestCase for Required Form Fields
# crm_user.tests.forms.test_AddressForm.FormReqTests 
class FormReqTests(TestCase):
    """ Define a TestCase for AddressForm Required Fields """
    @classmethod
    def setUpTestData(cls):
        """ FormReq setUp method to create test users """
        User.objects.create_user(email="test1@example.com", type="CUSTOMER", password="t3st13x@mpl3")
    
    def setUp(self):
        """ FormReq setUp method to create test user variables """
        self.user = User.objects.get(id=1)
    
    def test_valid_data(self):
        """ Define a test for valid data """
        form_data = {
            'user': self.user,
            'name': 'home',
            'type': 'RESIDENTIAL',
            'address_line1': '123 Sara Lane',
            'city': 'Houston',
            'state': 'TX',
            'zip': '77891',
        }
        form = AddressForm(form_data)
        self.assertTrue(form.is_valid())
    
    def test_no_user(self):
        """ Define a test for no user """
        form_data = {
            'name': 'home',
            'type': 'RESIDENTIAL',
            'address_line1': '123 Sara Lane',
            'city': 'Houston',
            'state': 'TX',
            'zip': '77891',
        }
        form = AddressForm(form_data)
        self.assertTrue(form.is_valid())
    
    def test_no_name(self):
        """ Define a test for no name """
        form_data = {
            'user': self.user,
            'type': 'RESIDENTIAL',
            'address_line1': '123 Sara Lane',
            'city': 'Houston',
            'state': 'TX',
            'zip': '77891',
        }
        form = AddressForm(form_data)
        self.assertFalse(form.is_valid())
    
    def test_no_type(self):
        """ Define a test for no type """
        form_data = {
            'user': self.user,
            'name': 'Home',
            'address_line1': '123 Sara Lane',
            'city': 'Houston',
            'state': 'TX',
            'zip': '77891',
        }
        form = AddressForm(form_data)
        self.assertFalse(form.is_valid())
    
    def test_no_address_line1(self):
        """ Define a test for no address_line1 """
        form_data = {
            'user': self.user,
            'name': 'Home',
            'type': 'RESIDENTIAL',
            'city': 'Houston',
            'state': 'TX',
            'zip': '77891',
        }
        form = AddressForm(form_data)
        self.assertFalse(form.is_valid())
    
    def test_no_address_line2(self):
        """ Define a test for no address_line2 """
        form_data = {
            'user': self.user,
            'name': 'Home',
            'type': 'RESIDENTIAL',
            'address_line1': '123 Sara Lane',
            'city': 'Houston',
            'state': 'TX',
            'zip': '77891',
        }
        form = AddressForm(form_data)
        self.assertTrue(form.is_valid())
    
    def test_no_city(self):
        """ Define a test for no city """
        form_data = {
            'user': self.user,
            'name': 'Home',
            'type': 'RESIDENTIAL',
            'address_line1': '123 Sara Lane',
            'state': 'TX',
            'zip': '77891',
        }
        form = AddressForm(form_data)
        self.assertFalse(form.is_valid())
    
    def test_no_state(self):
        """ Define a test for no state """
        form_data = {
            'user': self.user,
            'name': 'Home',
            'type': 'RESIDENTIAL',
            'address_line1': '123 Sara Lane',
            'city': 'Houston',
            'zip': '77891',
        }
        form = AddressForm(form_data)
        self.assertFalse(form.is_valid())
    
    def test_no_zip(self):
        """ Define a test for no zip """
        form_data = {
            'user': self.user,
            'name': 'Home',
            'type': 'RESIDENTIAL',
            'address_line1': '123 Sara Lane',
            'city': 'Houston',
            'state': 'TX',
        }
        form = AddressForm(form_data)
        self.assertFalse(form.is_valid())
    
# Create a TestCase for different user types submitting AddressForm
# crm_user.tests.forms.test_AddressForm.FormUserTests 
class FormUserTests(TestCase):
    """ Define a TestCase for different user types submitting AddressForm """
    @classmethod
    def setUpTestData(cls):
        """ FormUser setUp method to create test users """
        Customer.objects.create_user(email="customer@example.com", password="t3st13x@mpl3")
        Admin.objects.create_user(email="admin@example.com", password="t3st13x@mpl3")
        Employee.objects.create_user(email="employee@example.com", password="t3st13x@mpl3")
    
    def setUp(self):
        """ FormUser setUp method to create test user variables """
        self.customer = Customer.objects.get(id=1)
        self.admin = Admin.objects.get(id=2)
        self.employee = Employee.objects.get(id=3)
        self.formdata = {
            'name': 'home',
            'type': 'RESIDENTIAL',
            'address_line1': '123 Sara Lane',
            'city': 'Houston',
            'state': 'TX',
            'zip': '77891',
        }
    
    def test_user_customer(self):
        """ Define a test for user type Customer"""
        self.formdata['user'] = self.customer 
        form = AddressForm(self.formdata)
        self.assertTrue(form.is_valid())
    
    def test_user_admin(self):
        """ Define a test for user type Admin"""
        self.formdata['user'] = self.admin 
        form = AddressForm(self.formdata)
        self.assertTrue(form.is_valid())
    
    def test_user_employee(self):
        """ Define a test for user type Employee"""
        self.formdata['user'] = self.employee 
        form = AddressForm(self.formdata)
        self.assertTrue(form.is_valid())
    

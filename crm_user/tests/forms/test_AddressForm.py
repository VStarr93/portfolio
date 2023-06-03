#./crm_user/tests/forms/test_AddressForm.py
#-------------------------------------------------------------
#-------------------------------------------------------------
# IMPORTS

from django.test import TestCase
from crm_user.forms import AddressForm
from crm_user.models import User, Customer, Admin, Employee

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
        self.customer = Customer.objects.get(email='customer@example.com')
        self.admin = Admin.objects.get(email='admin@example.com')
        self.employee = Employee.objects.get(email='employee@example.com')
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
    
# Create a TestCase for AddressForm Labels 
# crm_user.tests.forms.test_AddressForm.FormLabelTests 
class FormLabelTests(TestCase):
    """ Define a TestCase for AddressForm Labels """
    @classmethod
    def setUpTestData(cls):
        """ FormLabel setUp method to create test users """
        User.objects.create_user(email="test1@example.com", type="CUSTOMER", password="t3st13x@mpl3")
    
    def setUp(self):
        """ FormHelp setUp method to create test user variables """
        self.user = User.objects.get(id=1)
        self.formdata = {
            'user': self.user,
            'name': 'home',
            'type': 'RESIDENTIAL',
            'address_line1': '123 Sara Lane',
            'city': 'Houston',
            'state': 'TX',
            'zip': '77891',
        }
    
    def test_address_field_address_line1_label(self):
        """ Define a test for address_line1 field label """
        form = AddressForm(self.formdata)
        self.assertTrue(form.fields['address_line1'].label == 'Address Line 1')
        
    def test_address_field_address_line2_label(self):
        """ Define a test for address_line2 field label """
        form = AddressForm(self.formdata)
        self.assertTrue(form.fields['address_line2'].label == 'Address Line 2')
        
    def test_address_field_city_label(self):
        """ Define a test for city field label """
        form = AddressForm(self.formdata)
        self.assertTrue(form.fields['city'].label == 'City')
        
    def test_address_field_state_label(self):
        """ Define a test for state field label """
        form = AddressForm(self.formdata)
        self.assertTrue(form.fields['state'].label == 'State')
        
    def test_address_field_zip_label(self):
        """ Define a test for zip field label """
        form = AddressForm(self.formdata)
        self.assertTrue(form.fields['zip'].label == 'Zip')
        
    def test_address_field_name_label(self):
        """ Define a test for name field label """
        form = AddressForm(self.formdata)
        self.assertTrue(form.fields['name'].label == 'Name')
        
    def test_address_field_type_label(self):
        """ Define a test for type field label """
        form = AddressForm(self.formdata)
        self.assertTrue(form.fields['type'].label == 'Type')
        
        
# Create a TestCase for AddressForm Help Test 
# crm_user.tests.forms.test_AddressForm.FormHelpTests 
class FormHelpTests(TestCase):
    """ Define a TestCase for AddressForm Help Text """
    @classmethod
    def setUpTestData(cls):
        """ FormHelp setUp method to create test users """
        User.objects.create_user(email="test1@example.com", type="CUSTOMER", password="t3st13x@mpl3")
    
    def setUp(self):
        """ FormHelp setUp method to create test user variables """
        self.user = User.objects.get(id=1)
        self.formdata = {
            'user': self.user,
            'name': 'home',
            'type': 'RESIDENTIAL',
            'address_line1': '123 Sara Lane',
            'city': 'Houston',
            'state': 'TX',
            'zip': '77891',
        }
    
    def test_address_field_address_line1_help_text(self):
        """ Define a test for address_line1 field help text """
        form = AddressForm(self.formdata)
        self.assertTrue(form.fields['address_line1'].help_text == 'Enter the street number and street name')
        
    def test_address_field_address_line2_help_text(self):
        """ Define a test for address_line2 field help text """
        form = AddressForm(self.formdata)
        self.assertTrue(form.fields['address_line2'].help_text == 'Enter the apartment or suite number')
        
    def test_address_field_city_help_text(self):
        """ Define a test for city field help text """
        form = AddressForm(self.formdata)
        self.assertTrue(form.fields['city'].help_text == 'Enter the city')
        
    def test_address_field_state_help_text(self):
        """ Define a test for state field help text """
        form = AddressForm(self.formdata)
        self.assertTrue(form.fields['state'].help_text == 'Enter the state as a 2 letter initial')
        
    def test_address_field_zip_help_text(self):
        """ Define a test for zip field help text """
        form = AddressForm(self.formdata)
        self.assertTrue(form.fields['zip'].help_text == 'Enter the zip code')
        
    def test_address_field_name_help_text(self):
        """ Define a test for name field help text """
        form = AddressForm(self.formdata)
        self.assertTrue(form.fields['name'].help_text == 'Enter a nickname for this address')
        
    def test_address_field_type_help_text(self):
        """ Define a test for type field help text """
        form = AddressForm(self.formdata)
        self.assertTrue(form.fields['type'].help_text == 'Select the correct address type')
        
        
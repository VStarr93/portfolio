#./crm_user/tests/test_forms.py
#-------------------------------------------------------------
#-------------------------------------------------------------
# IMPORTS

from django.test import TestCase, override_settings
from crm_user.forms import *
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
# Create your Custom User Creation Form tests here.
# crm_user.tests.test_forms.CustomUserCreationFormTests 
class CustomUserCreationFormTests(TestCase):
    """ Define a TestCase for CustomUserCreationForm """
    def test_form_creation(self):
        """ Define a test for form creation"""
        form_data = {
            'first_name': 'John',
            'last_name': 'Smith',
            'type': 'EMPLOYEE',
            'email': 'jsmith@example.com',
            'password1': 'JSm1th3x@mpl3',
            'password2': 'JSm1th3x@mpl3'
        }
        form = CustomUserCreationForm(form_data)
        self.assertTrue(form.is_valid())

    def test_form_creation_no_pwd(self):
        """ Define a test for form creation"""
        form_data = {
            'first_name': 'John',
            'last_name': 'Smith',
            'type': 'EMPLOYEE',
            'email': 'jsmith@example.com',
        }
        form = CustomUserCreationForm(form_data)
        self.assertFalse(form.is_valid())

    def test_save_form_to_db(self):
        """ Define a test for saving form to database """
        form_data = {
            'first_name': 'John',
            'middle_name': 'Jacob',
            'last_name': 'Smith',
            'type': 'EMPLOYEE',
            'email': 'jsmith@example.com',
            'password1': 'JSm1th3x@mpl3',
            'password2': 'JSm1th3x@mpl3'
        }
        form = CustomUserCreationForm(form_data)
        form.save()
        self.assertIsInstance(Employee.objects.get(email='jsmith@example.com'), Employee)


#-------------------------------------------------------------
#-------------------------------------------------------------
# Create your Customer Creation Form tests here.
# crm_user.tests.test_forms.CustomerCreationFormTests 
class CustomerCreationFormTests(TestCase):
    """ Define a TestCase for CustomerCreationForm """
    def test_form_creation(self):
        """ Define a test for form creation"""
        form_data = {
            'first_name': 'John',
            'middle_name': 'Jacob',
            'last_name': 'Smith',
            'email': 'jsmith@example.com',
            'password1': 'JSm1th3x@mpl3',
            'password2': 'JSm1th3x@mpl3'
        }
        form = CustomerCreationForm(form_data)
        self.assertTrue(form.is_valid())
        self.assertEqual(form.type, 'CUSTOMER')

    def test_form_creation_no_pwd(self):
        """ Define a test for form creation"""
        form_data = {
            'first_name': 'John',
            'last_name': 'Smith',
            'email': 'jsmith@example.com',
        }
        form = CustomerCreationForm(form_data)
        self.assertFalse(form.is_valid())

    def test_save_form_to_db(self):
        """ Define a test for saving form to database """
        form_data = {
            'first_name': 'John',
            'middle_name': 'Jacob',
            'last_name': 'Smith',
            'email': 'jsmith@example.com',
            'password1': 'JSm1th3x@mpl3',
            'password2': 'JSm1th3x@mpl3'
        }
        form = CustomerCreationForm(form_data)
        form.save()
        self.assertIsInstance(Customer.objects.get(email='jsmith@example.com'), Customer)


#-------------------------------------------------------------
#-------------------------------------------------------------
# Create your Employee Creation Form tests here.
# crm_user.tests.test_forms.EmployeeCreationFormTests 
class EmployeeCreationFormTests(TestCase):
    """ Define a TestCase for EmployeeCreationForm """
    def test_form_creation(self):
        """ Define a test for form creation"""
        form_data = {
            'first_name': 'John',
            'middle_name': 'Jacob',
            'last_name': 'Smith',
            'email': 'jsmith@example.com',
            'password1': 'JSm1th3x@mpl3',
            'password2': 'JSm1th3x@mpl3'
        }
        form = EmployeeCreationForm(form_data)
        self.assertTrue(form.is_valid())
        self.assertEqual(form.type, 'EMPLOYEE')

    def test_form_creation_no_pwd(self):
        """ Define a test for form creation"""
        form_data = {
            'first_name': 'John',
            'last_name': 'Smith',
            'email': 'jsmith@example.com',
        }
        form = EmployeeCreationForm(form_data)
        self.assertFalse(form.is_valid())

    def test_save_form_to_db(self):
        """ Define a test for saving form to database """
        form_data = {
            'first_name': 'John',
            'middle_name': 'Jacob',
            'last_name': 'Smith',
            'email': 'jsmith@example.com',
            'password1': 'JSm1th3x@mpl3',
            'password2': 'JSm1th3x@mpl3'
        }
        form = EmployeeCreationForm(form_data)
        form.save()
        self.assertIsInstance(Employee.objects.get(email='jsmith@example.com'), Employee)


#-------------------------------------------------------------
#-------------------------------------------------------------
# Create your Admin Creation Form tests here.
# crm_user.tests.test_forms.AdminCreationFormTests 
class AdminCreationFormTests(TestCase):
    """ Define a TestCase for AdminCreationForm """
    def test_form_creation(self):
        """ Define a test for form creation"""
        form_data = {
            'first_name': 'John',
            'middle_name': 'Jacob',
            'last_name': 'Smith',
            'email': 'jsmith@example.com',
            'password1': 'JSm1th3x@mpl3',
            'password2': 'JSm1th3x@mpl3'
        }
        form = AdminCreationForm(form_data)
        self.assertTrue(form.is_valid())
        self.assertEqual(form.type, 'ADMIN')

    def test_form_creation_no_pwd(self):
        """ Define a test for form creation"""
        form_data = {
            'first_name': 'John',
            'last_name': 'Smith',
            'email': 'jsmith@example.com',
        }
        form = AdminCreationForm(form_data)
        self.assertFalse(form.is_valid())

    def test_save_form_to_db(self):
        """ Define a test for saving form to database """
        form_data = {
            'first_name': 'John',
            'middle_name': 'Jacob',
            'last_name': 'Smith',
            'email': 'jsmith@example.com',
            'password1': 'JSm1th3x@mpl3',
            'password2': 'JSm1th3x@mpl3'
        }
        form = AdminCreationForm(form_data)
        form.save()
        self.assertIsInstance(Admin.objects.get(email='jsmith@example.com'), Admin)


#-------------------------------------------------------------
#-------------------------------------------------------------
# Create your Simple Customer Creation Form tests here.
# crm_user.tests.test_forms.SimpleCustomerCreationFormTests 
class SimpleCustomerCreationFormTests(TestCase):
    """ Define a TestCase for SimpleCustomerCreationForm """
    def test_form_creation(self):
        """ Define a test for form creation"""
        form_data = {
            'first_name': 'John',
            'middle_name': 'Jacob',
            'last_name': 'Smith',
            'email': 'jsmith@example.com',
            'password1': 'JSm1th3x@mpl3',
            'password2': 'JSm1th3x@mpl3'
        }
        form = SimpleCustomerCreationForm(form_data)
        self.assertTrue(form.is_valid())

    def test_form_creation_no_pwd(self):
        """ Define a test for form creation"""
        form_data = {
            'first_name': 'John',
            'last_name': 'Smith',
            'email': 'jsmith@example.com',
        }
        form = SimpleCustomerCreationForm(form_data)
        self.assertTrue(form.is_valid())

    def test_save_form_to_db(self):
        """ Define a test for saving form to database """
        form_data = {
            'first_name': 'John',
            'last_name': 'Smith',
            'email': 'jsmith@example.com',
        }
        form = SimpleCustomerCreationForm(form_data)
        form.save()
        self.assertIsInstance(Customer.objects.get(email='jsmith@example.com'), Customer)


#-------------------------------------------------------------
#-------------------------------------------------------------
# Create your Simple Employee Creation Form tests here.
# crm_user.tests.test_forms.SimpleEmployeeCreationFormTests 
class SimpleEmployeeCreationFormTests(TestCase):
    """ Define a TestCase for SimpleEmployeeCreationForm """
    def test_form_creation(self):
        """ Define a test for form creation"""
        form_data = {
            'first_name': 'John',
            'middle_name': 'Jacob',
            'last_name': 'Smith',
            'email': 'jsmith@example.com',
            'password1': 'JSm1th3x@mpl3',
            'password2': 'JSm1th3x@mpl3'
        }
        form = SimpleEmployeeCreationForm(form_data)
        self.assertTrue(form.is_valid())

    def test_form_creation_no_pwd(self):
        """ Define a test for form creation"""
        form_data = {
            'first_name': 'John',
            'last_name': 'Smith',
            'email': 'jsmith@example.com',
        }
        form = SimpleEmployeeCreationForm(form_data)
        self.assertTrue(form.is_valid())

    def test_save_form_to_db(self):
        """ Define a test for saving form to database """
        form_data = {
            'first_name': 'John',
            'last_name': 'Smith',
            'email': 'jsmith@example.com',
        }
        form = SimpleEmployeeCreationForm(form_data)
        form.save()
        self.assertIsInstance(Employee.objects.get(email='jsmith@example.com'), Employee)


#-------------------------------------------------------------
#-------------------------------------------------------------
# Create your Simple Admin Creation Form tests here.
# crm_user.tests.test_forms.SimpleAdminCreationFormTests 
class SimpleAdminCreationFormTests(TestCase):
    """ Define a TestCase for SimpleAdminCreationForm """
    def test_form_creation(self):
        """ Define a test for form creation"""
        form_data = {
            'first_name': 'John',
            'middle_name': 'Jacob',
            'last_name': 'Smith',
            'email': 'jsmith@example.com',
            'password1': 'JSm1th3x@mpl3',
            'password2': 'JSm1th3x@mpl3'
        }
        form = SimpleAdminCreationForm(form_data)
        self.assertTrue(form.is_valid())

    def test_form_creation_no_pwd(self):
        """ Define a test for form creation"""
        form_data = {
            'first_name': 'John',
            'last_name': 'Smith',
            'email': 'jsmith@example.com',
        }
        form = SimpleAdminCreationForm(form_data)
        self.assertTrue(form.is_valid())

    def test_save_form_to_db(self):
        """ Define a test for saving form to database """
        form_data = {
            'first_name': 'John',
            'last_name': 'Smith',
            'email': 'jsmith@example.com',
        }
        form = SimpleAdminCreationForm(form_data)
        form.save()
        self.assertIsInstance(Admin.objects.get(email='jsmith@example.com'), Admin)


#-------------------------------------------------------------
#-------------------------------------------------------------
# Create your Custom User Change Form tests here.
# crm_user.tests.test_forms.CustomUserChangeFormTests 
class CustomUserChangeFormTests(TestCase):
    """ Define a TestCase for CustomUserChangeForm """
    def setUp(self):
        """ CustomUserChangeForm setUp method to create test users"""
        self.user1 = Customer.objects.create_user(email='user1@example.com', first_name="John", last_name="Smith")
    
    def test_form_creation(self):
        """ Define a test for form creation"""
        form_data = {
            'middle_name': 'Jacob',
            'email': 'jsmith@example.com',
        }
        form = CustomUserChangeForm(form_data, instance=self.user1)
        self.assertTrue(form.is_valid())
        
    def test_save_form_to_db(self):
        """ Define a test for saving form to database """
        form_data = {
            'middle_name': 'Jason',
            'email': 'jsmith@example.com',
        }
        form = CustomUserChangeForm(form_data, instance=self.user1)
        form.save()
        self.assertEqual(self.user1.email, 'jsmith@example.com')
        self.assertEqual(self.user1.middle_name, 'Jason')


#-------------------------------------------------------------
#-------------------------------------------------------------
# Create your Address Form tests here.
# crm_user.tests.test_forms.AddressFormTests 
class AddressFormTests(TestCase):
    """ Define a TestCase for AddressForm """
    def setUp(self):
        """ AddressForm setUp method to create test users"""
        self.user1 = User.objects.create_user(email="test1@example.com", type="CUSTOMER")
    
    def test_form_creation(self):
        """ Define a test for form creation"""
        form_data = {
            'user': self.user1,
            'name': 'home',
            'type': 'RESIDENTIAL',
            'address_line1': '123 Sara Lane',
            'city': 'Houston',
            'state': 'TX',
            'zip': '77891',
        }
        form = AddressForm(form_data)
        self.assertTrue(form.is_valid())
        
    def test_save_form_to_db(self):
        """ Define a test for saving form to database """
        form_data = {
            'name': 'home',
            'type': 'RESIDENTIAL',
            'address_line1': '123 Sara Lane',
            'city': 'Houston',
            'state': 'TX',
            'zip': '77891',
        }
        form = AddressForm(form_data)
        address = form.save(commit=False)
        self.assertIsInstance(self.user1, User)
        address.user = self.user1
        address.save()
        self.assertIsInstance(Address.objects.get(user=address.user, name=address.name), Address)
        self.assertIn(address, self.user1.addresses.all())


#-------------------------------------------------------------
#-------------------------------------------------------------
# Create your Customer Customize Form tests here.
# crm_user.tests.test_forms.CustomerCustomizeFormTests 
class CustomerCustomizeFormTests(TestCase):
    """ Define a TestCase for CustomerCustomizeForm """
    def setUp(self):
        """ CustomerCustomizeForm setUp method to create test users"""
        self.user1 = Customer.objects.create_user(email="test1@example.com").profile
    
    def test_form_creation(self):
        """ Define a test for form creation"""
        form_data = {
            'language': 'SPANISH',
            'theme': 'PURPLE',
        }
        form = CustomerCustomizeForm(form_data, instance=self.user1)
        self.assertTrue(form.is_valid())
        
    def test_save_form_to_db(self):
        """ Define a test for saving form to database """
        form_data = {
            'language': 'SPANISH',
            'theme': 'PURPLE',
        }
        form = CustomerCustomizeForm(form_data, instance=self.user1)
        form.save()
        self.assertEqual(self.user1.theme, form.cleaned_data['theme'])
        self.assertEqual(self.user1.language, 'SPANISH')


#-------------------------------------------------------------
#-------------------------------------------------------------
# Create your Employee Customize Form tests here.
# crm_user.tests.test_forms.EmployeeCustomizeFormTests 
class EmployeeCustomizeFormTests(TestCase):
    """ Define a TestCase for EmployeeCustomizeForm """
    def setUp(self):
        """ EmployeeCustomizeForm setUp method to create test users"""
        self.user1 = Employee.objects.create_user(email="test1@example.com").emp_profile
    
    def test_form_creation(self):
        """ Define a test for form creation"""
        form_data = {
            'language': 'SPANISH',
            'theme': 'PURPLE',
        }
        form = EmployeeCustomizeForm(form_data, instance=self.user1)
        self.assertTrue(form.is_valid())
        
    def test_save_form_to_db(self):
        """ Define a test for saving form to database """
        form_data = {
            'language': 'SPANISH',
            'theme': 'PURPLE',
        }
        form = EmployeeCustomizeForm(form_data, instance=self.user1)
        form.save()
        self.assertEqual(self.user1.theme, form.cleaned_data['theme'])
        self.assertEqual(self.user1.language, 'SPANISH')


#-------------------------------------------------------------
#-------------------------------------------------------------
# Create your Admin Customize Form tests here.
# crm_user.tests.test_forms.AdminCustomizeFormTests 
class AdminCustomizeFormTests(TestCase):
    """ Define a TestCase for AdminCustomizeForm """
    def setUp(self):
        """ AdminCustomizeForm setUp method to create test users"""
        self.user1 = Admin.objects.create_user(email="test1@example.com").admin_profile
    
    def test_form_creation(self):
        """ Define a test for form creation"""
        form_data = {
            'language': 'SPANISH',
            'theme': 'PURPLE',
        }
        form = AdminCustomizeForm(form_data, instance=self.user1)
        self.assertTrue(form.is_valid())
        
    def test_save_form_to_db(self):
        """ Define a test for saving form to database """
        form_data = {
            'language': 'SPANISH',
            'theme': 'PURPLE',
        }
        form = AdminCustomizeForm(form_data, instance=self.user1)
        form.save()
        self.assertEqual(self.user1.theme, form.cleaned_data['theme'])
        self.assertEqual(self.user1.language, 'SPANISH')


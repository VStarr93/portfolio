#./crm_user/tests/views/test_UserDetailsView.py
#-------------------------------------------------------------
#-------------------------------------------------------------
# IMPORTS

from django.test import TestCase, override_settings, Client 
from crm_user.forms import *
from crm_user.models import *
from django.core.exceptions import ValidationError, PermissionDenied
import datetime 
from django.core.files.uploadedfile import SimpleUploadedFile 
import shutil, tempfile 

# For Testing Email Services
from django.core import mail 

# For HTTP 
from http import HTTPStatus

#-------------------------------------------------------------
#-------------------------------------------------------------
# Create your Variables here.

MEDIA_ROOT = tempfile.mkdtemp()


#-------------------------------------------------------------
#-------------------------------------------------------------
# Create your User Registration View tests here.


# Create a TestCase for User Details View Get Request
# crm_user.tests.views.test_UserRegistrationView.GetATests 
class GetTests(TestCase):
    """ Define a TestCase for User Details View Get Request """
    @classmethod 
    def setUpTestData(cls):
        """ Define a setUpTestData method for User Details View Get Request """
        # Create users 
        cls.password = 'P@ssw0rd'
        cls.admin1 = Admin.objects.create_user(first_name="Admin1", email='admin1@example.com', password=cls.password)
        cls.admin2 = Admin.objects.create_user(first_name="Admin2", email='admin2@example.com', password=cls.password)
        cls.employee1 = Employee.objects.create_user(first_name="Employee1", email='employee1@example.com', password=cls.password)
        cls.employee2 = Employee.objects.create_user(first_name="Employee2", email='employee2@example.com', password=cls.password)
        cls.manager1 = Employee.objects.create_user(first_name="Manager1", email='manager1@example.com', password=cls.password)
        cls.manager2 = Employee.objects.create_user(first_name="Manager2", email='manager2@example.com', password=cls.password)
        cls.manager1.emp_profile.is_manager = True 
        cls.manager1.emp_profile.save()
        cls.manager2.emp_profile.is_manager = True 
        cls.manager2.emp_profile.save()
        cls.customer1 = Customer.objects.create_user(first_name="Customer1", email='customer1@example.com', password=cls.password)
        cls.customer2 = Customer.objects.create_user(first_name="Customer2", email='customer2@example.com', password=cls.password)
    
        # Create Clients
        cls.aclient = Client()
        cls.eclient = Client()
        cls.mclient = Client()
        cls.cclient = Client()
        
        # Log in users to correct client
        cls.aclient.login(email=cls.admin1.email, password=cls.password)
        cls.eclient.login(email=cls.employee1.email, password=cls.password)
        cls.mclient.login(email=cls.manager1.email, password=cls.password)
        cls.cclient.login(email=cls.customer1.email, password=cls.password)
        
    def test_url_location(self):
        """ Test that User Details URL is at correct location """
        # Create Get Request
        response = self.aclient.get(f'/user/user-details/{self.admin1.id}')
        
        # Check that status code is 200
        self.assertEqual(response.status_code, 200)
        
    def test_url_name(self):
        """ Test that User Registration URL name is correct """
        # Create Get Request
        response = self.aclient.get(reverse('crm_user:user-details', args=[int(self.admin1.id)]))
        
        # Check that status code is 200
        self.assertEqual(response.status_code, 200)
       
    def test_raise_403_employee_get_admin(self):
        """ Test that a 403 error will be raised when an employee views an admin """
        # Create a Response 
        response = self.eclient.get(reverse('crm_user:user-details', args=[int(self.admin1.id)]))
        
        # Check that the status code is 403
        self.assertEqual(response.status_code, 403)
        
    def test_raise_403_employee_get_manager(self):
        """ Test that a 403 error will be raised when an employee views a manager """
        # Create a Response
        response = self.eclient.get(reverse('crm_user:user-details', args=[int(self.manager1.id)]))
        
        # Check that the status code is 403
        self.assertEqual(response.status_code, 403)
        
    def test_raise_403_employee_get_employee(self):
        """ Test that a 403 error will be raised when an employee views an employee """
        # Create a response 
        response = self.eclient.get(reverse('crm_user:user-details', args=[int(self.employee2.id)]))
        
        # Check that the status code is 403
        self.assertEqual(response.status_code, 403)
        
    def test_raise_403_customer_get_admin(self):
        """ Test that a 403 error will be raised when a customer views an admin """
        # Create a response 
        response = self.cclient.get(reverse('crm_user:user-details', args=[int(self.admin1.id)]))
        
        # Check that status code is 403
        self.assertEqual(response.status_code, 403)
        
    def test_raise_403_customer_get_manager(self):
        """ Test that a 403 error will be raised when a customer views a manager """
        # Create a response
        response = self.cclient.get(reverse('crm_user:user-details', args=[int(self.manager1.id)]))
        
        # Check that status code is 403
        self.assertEqual(response.status_code, 403)
        
    def test_raise_403_customer_get_employee(self):
        """ Test that a 403 error will be raised when a customer views an employee """
        # Create a response 
        response = self.cclient.get(reverse('crm_user:user-details', args=[int(self.employee1.id)]))
        
        # Check that status code is 403
        self.assertEqual(response.status_code, 403)
        
    def test_raise_403_customer_get_customer(self):
        """ Test that a 403 error will be raised when a customer views a customer """
        # Create a response 
        response = self.cclient.get(reverse('crm_user:user-details', args=[int(self.customer2.id)]))
        
        # Check that status code is 403
        self.assertEqual(response.status_code, 403)
        
    def test_template_admin_get_admin(self):
        """ Test that the correct template is rendered when an admin views an admin """
        # Create a response 
        response = self.aclient.get(reverse('crm_user:user-details', args=[int(self.admin2.id)]))
        
        # Check that the status code is 200
        self.assertEqual(response.status_code, 200)
        
        # Check that the correct template is rendered 
        self.assertTemplateUsed(response, 'crm_user/user_details.html')
        
    def test_template_admin_get_manager(self):
        """" Test that the correct template is rendered when an admin views a manager """
        # Create a response 
        response = self.aclient.get(reverse('crm_user:user-details', args=[int(self.manager1.id)]))
        
        # Check that the status code is 200
        self.assertEqual(response.status_code, 200)
        
        # Check that the correct template is rendered 
        self.assertTemplateUsed(response, 'crm_user/user_details.html')
        
    def test_template_admin_get_employee(self):
        """ Test that the correct template is rendered when an admin views an employee """
        # Create a response 
        response = self.aclient.get(reverse('crm_user:user-details', args=[int(self.employee1.id)]))
        
        # Check that the status code is 200
        self.assertEqual(response.status_code, 200)
        
        # Check that the correct template is rendered 
        self.assertTemplateUsed(response, 'crm_user/user_details.html')
        
    def test_template_admin_get_customer(self):
        """ Test that the correct template is rendered when an admin views a customer """
        # Create a response 
        response = self.aclient.get(reverse('crm_user:user-details', args=[int(self.customer1.id)]))
        
        # Check that the status code is 200
        self.assertEqual(response.status_code, 200)
        
        # Check that the correct template is rendered 
        self.assertTemplateUsed(response, 'crm_user/user_details.html')
        
    def test_template_manager_get_admin(self):
        """ Test that the correct template is rendered when a manager views an admin """    
        # Create a response 
        response = self.mclient.get(reverse('crm_user:user-details', args=[int(self.admin1.id)]))
        
        # Check that the status code is 200
        self.assertEqual(response.status_code, 200)
        
        # Check that the correct template is rendered 
        self.assertTemplateUsed(response, 'crm_user/user_details.html')
        
    def test_template_manager_get_manager(self):
        """ Test that the correct template is rendered when a manager views a manager """
        # Create a response 
        response = self.mclient.get(reverse('crm_user:user-details', args=[int(self.manager2.id)]))
        
        # Check that the status code is 200
        self.assertEqual(response.status_code, 200)
        
        # Check that the correct template is rendered 
        self.assertTemplateUsed(response, 'crm_user/user_details.html')
        
    def test_template_manager_get_employee(self):
        """ Test that the correct template is rendered when a manager views an employee """
        # Create a response 
        response = self.mclient.get(reverse('crm_user:user-details', args=[int(self.employee1.id)]))
        
        # Check that the status code is 200
        self.assertEqual(response.status_code, 200)
        
        # Check that the correct template is rendered 
        self.assertTemplateUsed(response, 'crm_user/user_details.html')
        
    def test_template_manager_get_customer(self):
        """" Test that the correct template is rendered when a manager views a customer """
        # Create a response 
        response = self.mclient.get(reverse('crm_user:user-details', args=[int(self.customer1.id)]))
        
        # Check that the status code is 200
        self.assertEqual(response.status_code, 200)
        
        # Check that the correct template is rendered 
        self.assertTemplateUsed(response, 'crm_user/user_details.html')
        
    def test_template_employee_get_customer(self):
        """ Test that the correct template is rendered when an employee views a customer """
        # Create a response 
        response = self.eclient.get(reverse('crm_user:user-details', args=[int(self.customer1.id)]))
        
        # Check that the status code is 200
        self.assertEqual(response.status_code, 200)
        
        # Check that the correct template is rendered 
        self.assertTemplateUsed(response, 'crm_user/user_details.html')
        
    
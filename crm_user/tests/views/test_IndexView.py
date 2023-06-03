#./crm_user/tests/views/test_IndexView.py
#-------------------------------------------------------------
#-------------------------------------------------------------
# IMPORTS

from django.test import TestCase
from crm_user.models import Admin, Employee, Customer
from django.core.exceptions import ValidationError 
import datetime 
from django.core.files.uploadedfile import SimpleUploadedFile 

# For HTTP 
from http import HTTPStatus
from django.urls import reverse 

#-------------------------------------------------------------
#-------------------------------------------------------------
# Create your Variables here.


#-------------------------------------------------------------
#-------------------------------------------------------------
# Create your Index View tests here.


# Create a TestCase for Index View Get Request
# crm_user.tests.views.test_IndexView.GetRequestTests 
class GetRequestTests(TestCase):
    """ Define a TestCase for Index View Get Request """
    @classmethod 
    def setUpTestData(cls):
        """ Define setUpTestData for Index View Get Request """
        Admin.objects.create_user(email="admin@example.com", password="@dm1n3x@mpl3")
        Employee.objects.create_user(email="employee@example.com", password="3mpl0y333x@mpl3")
        Customer.objects.create_user(email="customer@example.com", password="Cust0m3r3x@mpl3")
        
    def setUp(self):
        """ Define setUp for Index View Get Request """
        self.admin = Admin.objects.get(email="admin@example.com")
        self.employee = Employee.objects.get(email="employee@example.com")
        self.customer = Customer.objects.get(email='customer@example.com')
    
    def test_index_view_url_exists(self):
        """ That that Index View URL exists """
        response = self.client.get('/user/')
        self.assertEqual(response.status_code, 302)
        
    def test_index_view_url_name(self):
        """ Test that Index View URL name exists """
        response = self.client.get(reverse('crm_user:home'))
        self.assertEqual(response.status_code, 302)
        
    def test_index_view_anonymous_redirect(self):
        """ Test that Index View redirects anonymous users to Login """
        response = self.client.get(reverse('crm_user:home'))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('login'))
        
    def test_index_view_admin(self):
        """ Test that Index View renders admin templates when logged in """
        # login user
        self.client.login(email=self.admin.email, password='@dm1n3x@mpl3')
        # Get Response
        response = self.client.get(reverse('crm_user:home'))
        # Test status code
        # Status code should be 200
        self.assertEqual(response.status_code, 200)
        # Test Templates used
        # Admin user should use admin_menu.html and admin_dashboard.html
        self.assertTemplateUsed(response, 'crm_user/snippets/dashboard/admin_menu.html')
        self.assertTemplateUsed(response, 'crm_user/snippets/dashboard/admin_dashboard.html')
        
    def test_index_view_employee(self):
        """ Test that Index View renders employee templates when logged in """
        # login user
        self.client.login(email=self.employee.email, password='3mpl0y333x@mpl3')
        # Get Response
        response = self.client.get(reverse('crm_user:home'))
        # Test status code
        # Status code should be 200
        self.assertEqual(response.status_code, 200)
        # Test Templates used
        # Employee user should use employee_menu.html and employee_dashboard.html
        self.assertTemplateUsed(response, 'crm_user/snippets/dashboard/emp_menu.html')
        self.assertTemplateUsed(response, 'crm_user/snippets/dashboard/emp_dashboard.html')
        
    def test_index_view_customer(self):
        """ Test that Index View renders customer templates when logged in """
        # login user
        self.client.login(email=self.customer.email, password='Cust0m3r3x@mpl3')
        # Get Response
        response = self.client.get(reverse('crm_user:home'))
        # Test status code
        # Status code should be 200
        self.assertEqual(response.status_code, 200)
        # Test Templates used
        # Customer user should use customer_menu.html and customer_dashboard.html
        self.assertTemplateUsed(response, 'crm_user/snippets/dashboard/cust_menu.html')
        self.assertTemplateUsed(response, 'crm_user/snippets/dashboard/cust_dashboard.html')
        
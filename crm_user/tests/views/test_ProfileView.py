#./crm_user/tests/test_views.py
#-------------------------------------------------------------
#-------------------------------------------------------------
# IMPORTS

from django.test import TestCase, override_settings, Client 
from crm_user.forms import *
from crm_user.models import *
from django.core.exceptions import ValidationError 
import datetime 
from django.core.files.uploadedfile import SimpleUploadedFile 
import shutil, tempfile 
from django.forms.models import modelformset_factory 
from django.conf import settings  

# For Testing Email Services
from django.core import mail 

# For HTTP 
from http import HTTPStatus

# For DB Freeze 
from freezegun import freeze_time 
from django.utils import timezone

#-------------------------------------------------------------
#-------------------------------------------------------------
# Create your Variables here.

MEDIA_ROOT = tempfile.mkdtemp()


#-------------------------------------------------------------
#-------------------------------------------------------------
# Create your Profile View tests here.


# Create a TestCase for Profile View Get Request
# crm_user.tests.views.test_ProfileView.GetTests
class GetTests(TestCase):
    """ Define a TestCase for Profile View Get Request """
    @classmethod
    def setUpTestData(cls):
        cls.password = 'P@ssw0rd3x@mpl3'
        cls.employee = Employee.objects.create_user(email='employee@example.com', password=cls.password)
        cls.admin = Admin.objects.create_user(email='admin@example.com', password=cls.password)
        cls.customer = Customer.objects.create_user(email='customer@example.com', password=cls.password)
        cls.anonclient = Client()
        cls.adminclient = Client()
        cls.employeeclient = Client()
        cls.customerclient = Client()
        cls.adminclient.login(email=cls.admin.email, password=cls.password)
        cls.employeeclient.login(email=cls.employee.email, password=cls.password)
        cls.customerclient.login(email=cls.customer.email, password=cls.password)
        cls.anonresponse = cls.anonclient.get(reverse('crm_user:profile'))
        cls.adminresponse = cls.adminclient.get(reverse('crm_user:profile'))
        cls.employeeresponse = cls.employeeclient.get(reverse('crm_user:profile'))
        cls.customerresponse = cls.customerclient.get(reverse('crm_user:profile'))
        
    def setUp(self):
        """ Define a setUp for Profile View Get Request """
        
    def test_url_location(self):
        """ Test that Profile View URL is at correct location """
        # Create Response variable
        response = self.__class__.anonresponse 
        
        self.assertEqual(response.status_code, 302)
        
    def test_url_name(self):
        """ Test that Profile View URL name is correct """
        # Create Response variable
        response = self.__class__.anonresponse 
        
        self.assertEqual(response.status_code, 302)
        
    def test_redirect_not_logged_in(self):
        """ Test that Profile View will redirect anonymous users to the login page """
        # Create Response variable
        response = self.__class__.anonresponse 
        
        # Status Code should be 302
        self.assertEqual(response.status_code, 302)
        # Redirects to the login page
        self.assertRedirects(response, '/accounts/login/?next=/user/profile/')

    def test_template_admin(self):
        """ Test that Profile View will render the correct template for admin users """
        # Create Response variable
        response = self.__class__.adminresponse 
        
        # Check user is logged in
        self.assertEqual(response.context['user'], self.admin)

        # Check that status code is "success"
        self.assertEqual(response.status_code, 200)

        # Check that the correct template is rendered for admin users
        self.assertTemplateUsed(response, 'crm_user/snippets/profile/admin_acct.html')
        self.assertTemplateUsed(response, 'crm_user/profile.html')
    
    def test_template_employee(self):
        """ Test that Profile View will render the correct template for employee users """
        # Create Response variable
        response = self.__class__.employeeresponse 
        
        # Check user is logged in
        self.assertEqual(response.context['user'], self.employee)

        # Check that status code is "success"
        self.assertEqual(response.status_code, 200)

        # Check that the correct template is rendered for employee users
        self.assertTemplateUsed(response, 'crm_user/snippets/profile/emp_acct.html')
        self.assertTemplateUsed(response, 'crm_user/profile.html')
    
    def test_template_customer(self):
        """ Test that Profile View will render the correct template for customer users """
        # Create Response variable
        response = self.__class__.customerresponse 
        
        # Check user is logged in
        self.assertEqual(response.context['user'], self.customer)

        # Check that status code is "success"
        self.assertEqual(response.status_code, 200)

        # Check that the correct template is rendered for customer users
        self.assertTemplateUsed(response, 'crm_user/snippets/profile/cust_acct.html')
        self.assertTemplateUsed(response, 'crm_user/profile.html')
    
    def test_template_context_admin(self):
        """ Test that Profile View will render the correct template context for admin users """
        # Create Response variable
        response = self.__class__.adminresponse 
        
        # Check user is logged in
        self.assertEqual(response.context['user'], self.admin)

        # Check that status code is "success"
        self.assertEqual(response.status_code, 200)

        # Check that the correct template context is rendered for admin users
        self.assertIsInstance(response.context['changeForm'], CustomUserChangeForm)
        self.assertEqual(response.context['changeForm'].instance, self.admin)
        self.assertIsInstance(response.context['customizeForm'], AdminCustomizeForm)
        self.assertEqual(response.context['customizeForm'].instance, self.admin.admin_profile)
        self.assertQuerysetEqual(response.context['addressFormSet'].queryset, Address.objects.filter(user=self.admin))
        self.assertEqual(response.context['addressFormSet'].extra, 1)
        self.assertEqual(response.context['addressFormSet'].can_delete, True)
        self.assertEqual(response.context['addressFormSet'].model, Address)
        self.assertIsInstance(response.context['addressFormSet'].forms[0], AddressForm)
        self.assertIsInstance(response.context['addressFormHelper'], AddressFormHelper)

    def test_template_context_employee(self):
        """ Test that Profile View will render the correct template context for employee users """
        # Create Response variable
        response = self.__class__.employeeresponse 
        
        # Check user is logged in
        self.assertEqual(response.context['user'], self.employee)

        # Check that status code is "success"
        self.assertEqual(response.status_code, 200)

        # Check that the correct template context is rendered for employee users
        self.assertIsInstance(response.context['changeForm'], CustomUserChangeForm)
        self.assertEqual(response.context['changeForm'].instance, self.employee)
        self.assertIsInstance(response.context['customizeForm'], EmployeeCustomizeForm)
        self.assertEqual(response.context['customizeForm'].instance, self.employee.emp_profile)
        self.assertQuerysetEqual(response.context['addressFormSet'].queryset, Address.objects.filter(user=self.employee))
        self.assertEqual(response.context['addressFormSet'].extra, 1)
        self.assertEqual(response.context['addressFormSet'].can_delete, True)
        self.assertEqual(response.context['addressFormSet'].model, Address)
        self.assertIsInstance(response.context['addressFormSet'].forms[0], AddressForm)
        self.assertIsInstance(response.context['addressFormHelper'], AddressFormHelper)

    def test_template_context_customer(self):
        """ Test that Profile View will render the correct template context for customer users """
        # Create Response variable
        response = self.__class__.customerresponse 
        
        # Check user is logged in
        self.assertEqual(response.context['user'], self.customer)

        # Check that status code is "success"
        self.assertEqual(response.status_code, 200)

        # Check that the correct template context is rendered for customer users
        self.assertIsInstance(response.context['changeForm'], CustomUserChangeForm)
        self.assertEqual(response.context['changeForm'].instance, self.customer)
        self.assertIsInstance(response.context['customizeForm'], CustomerCustomizeForm)
        self.assertEqual(response.context['customizeForm'].instance, self.customer.profile)
        self.assertQuerysetEqual(response.context['addressFormSet'].queryset, Address.objects.filter(user=self.customer))
        self.assertEqual(response.context['addressFormSet'].extra, 1)
        self.assertEqual(response.context['addressFormSet'].can_delete, True)
        self.assertEqual(response.context['addressFormSet'].model, Address)
        self.assertIsInstance(response.context['addressFormSet'].forms[0], AddressForm)
        self.assertIsInstance(response.context['addressFormHelper'], AddressFormHelper)


#./crm_user/tests/views/test_UserRegistrationView.py
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


# Create a TestCase for User Registration View Get Request with anonymous user
# crm_user.tests.views.test_UserRegistrationView.GetAnonUserTests 
class GetAnonUserTests(TestCase):
    """ Define a TestCase for User Registration View Get Request with anonymous user """
    def test_url_location(self):
        """ Test that User Registration URL is at correct location """
        # Create Get Request
        response = self.client.get('/user/register/')
        
        # Check that status code is 200
        self.assertEqual(response.status_code, 200)
        
    def test_url_name(self):
        """ Test that User Registration URL name is correct """
        # Create Get Request
        response = self.client.get(reverse('crm_user:register'))
        
        # Check that status code is 200
        self.assertEqual(response.status_code, 200)
       
    def test_redirect_not_logged_in_create_employee(self):
        """ Test that User Registration View will redirect anonymous users who click on employee to home page """
        # Create a Get Request with empBtn 
        response = self.client.get(reverse('crm_user:register'), {'empBtn': True})
        
        # Check that status code is 302
        self.assertEqual(response.status_code, 302)
        
    def test_redirect_not_logged_in_create_admin(self):
        """ Test that User Registration View will redirect anonymous users who click on admin to home page """
        # Create a Get Request with adminBtn
        response = self.client.get(reverse('crm_user:register'), {'adminBtn': True})
        
        # Check that status code is 302
        self.assertEqual(response.status_code, 302)
    
    def test_template_not_logged_in_create_customer(self):
        """ Test that User Registration View will render correct template and context for anonymous users who click on customer """
        # Create a Get Request with customerBtn
        response = self.client.get(reverse('crm_user:register'), {'customerBtn': True})
        
        # Check that status code is 200
        self.assertEqual(response.status_code, 200)
        
        # Check that correct template is rendered
        self.assertTemplateUsed(response, 'crm_user/registration.html')
        
        # check that correct template context is rendered
        self.assertEqual(response.context['form'], CustomerCreationForm)

    def test_template_user_registration_not_logged_in(self):
        """ Test that User Registration View will render correct template for anonymous users """
        # Create a Get Request
        response = self.client.get(reverse('crm_user:register'))
        
        # Check that status code is 200
        self.assertEqual(response.status_code, 200)
        
        # Check that correct template is rendered
        self.assertTemplateUsed(response, 'crm_user/user_registration.html')
    

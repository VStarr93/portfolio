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

# Create a TestCase for Profile View Post Request
# crm_user.tests.views.test_ProfileView.PostTests
@freeze_time(timezone.now())
@override_settings(MEDIA_ROOT=MEDIA_ROOT)
class PostTests(TestCase):
    """ Define a TestCase for Profile View Post Request """
    @classmethod 
    def setUpTestData(cls):
        # Create password 
        cls.password = 'P@ssw0rd3x@mpl3'
        
        # Create users 
        cls.admin = Admin.objects.create_user(email='admin@example.com', password=cls.password)
        cls.employee = Employee.objects.create_user(email='employee@example.com', password=cls.password)
        cls.customer = Customer.objects.create_user(email='customer@example.com', password=cls.password)
        
        # Create Form Data
        cls.photo = SimpleUploadedFile("test_content", b"test_content", "image/jpg")
        cls.files = {
            'profile_photo': cls.photo,
        }
        cls.changedata = {
            'first_name': 'John',
            'middle_name': 'Jacob',
            'last_name': 'Smith',
            'email': 'jsmith@example.com',
            'birth_date': '1993-04-14',
            'phone_number': '+12124448769',
            #'profile_photo': SimpleUploadedFile('test_content', b'test_content', 'image/jpg'),
            'submitChange': True,
        }
        cls.customizedata = {
            'theme': 'PURPLE',
            'language': 'SPANISH',
            'submitCustomize': True,
        }
        cls.addressdata1 = {
            'form-0-name': 'home',
            'form-0-type': 'RESIDENTIAL',
            'form-0-address_line1': '123 Sara Lane',
            'form-0-city': 'Houston',
            'form-0-state': 'TX',
            'form-0-zip': '77891',
            'form-TOTAL_FORMS': 1,
            'form-INITIAL_FORMS': 0,
            'form-MAX-NUM_FORMS': 1000,            
            'form-MIN-NUM_FORMS': 0,
            'submitAddress': True,
        }
        cls.addressdatadelete = {
            'form-0-name': 'home',
            'form-0-type': 'RESIDENTIAL',
            'form-0-address_line1': '123 Sara Lane',
            'form-0-city': 'Houston',
            'form-0-state': 'TX',
            'form-0-zip': '77891',
            'form-0-DELETE': True,
            'form-0-id': 1,
            'form-TOTAL_FORMS': 1,
            'form-INITIAL_FORMS': 1,
            'form-MAX-NUM_FORMS': 1000,            
            'form-MIN-NUM_FORMS': 0,
            'submitAddress': True,
        }
        cls.addressdata2 = {
            'form-0-name': 'home',
            'form-0-type': 'RESIDENTIAL',
            'form-0-address_line1': '123 Sara Lane',
            'form-0-city': 'Houston',
            'form-0-state': 'TX',
            'form-0-zip': '77891',
            'form-1-name': 'work',
            'form-1-type': 'COMMERCIAL',
            'form-1-address_line1': '567 Business Lane',
            'form-1-city': 'Spring',
            'form-1-state': 'TX',
            'form-1-zip': '77801',
            'form-TOTAL_FORMS': 2,
            'form-INITIAL_FORMS': 0,
            'form-MAX-NUM_FORMS': 1000,            
            'form-MIN-NUM_FORMS': 0,
            'submitAddress': True,
        }

        # Create User Clients
        cls.aclient = Client()
        cls.eclient = Client()
        cls.cclient = Client()
        
        # Log in User for each client
        cls.aclient.login(email=cls.admin.email, password=cls.password)
        cls.eclient.login(email=cls.employee.email, password=cls.password)
        cls.cclient.login(email=cls.customer.email, password=cls.password)
        
        # Create Post Request for Customize Form 
        cls.aCustomizeResponse = cls.aclient.post(reverse('crm_user:profile'), cls.customizedata)
        cls.eCustomizeResponse = cls.eclient.post(reverse('crm_user:profile'), cls.customizedata)
        cls.cCustomizeResponse = cls.cclient.post(reverse('crm_user:profile'), cls.customizedata)
        
        # Create Post Request for Address Form
        cls.aAddressResponse = cls.aclient.post(reverse('crm_user:profile'), cls.addressdata1)
        cls.eAddressResponse = cls.eclient.post(reverse('crm_user:profile'), cls.addressdata1)
        cls.cAddressResponse = cls.cclient.post(reverse('crm_user:profile'), cls.addressdata1)
        
        # Create Post Request for Change Form 
        cls.aChangeResponse = cls.aclient.post(reverse('crm_user:profile'), cls.changedata)
        cls.eChangeResponse = cls.eclient.post(reverse('crm_user:profile'), cls.changedata)
        cls.cChangeResponse = cls.cclient.post(reverse('crm_user:profile'), cls.changedata)
        
    @classmethod 
    def tearDownClass(cls):
        shutil.rmtree(MEDIA_ROOT, ignore_errors=True)
        super().tearDownClass()

    def test_redirect_on_success_change_form(self):
        """ Test that Profile View redirects user to profile after successful CustomUserChangeForm post """
        # Create Response variable
        response = self.__class__.aChangeResponse
        
        # Check that response status is 302
        self.assertEqual(response.status_code, 302)
        
        # Check that view redirects successful post to profile view
        self.assertRedirects(response, reverse('crm_user:profile'))
        
    def test_redirect_on_success_admin_customize_form(self):
        """ Test that Profile View redirects user to profile after successful AdminCustomizeForm post """
        # Create Response variable
        response = self.__class__.aCustomizeResponse
        
        # Check that response status is 302
        self.assertEqual(response.status_code, 302)
        
        # Check that view redirects successful post to profile view
        self.assertRedirects(response, reverse('crm_user:profile'))
        
    def test_redirect_on_success_employee_customize_form(self):
        """ Test that Profile View redirects user to profile after successful EmployeeCustomizeForm post """
        # Create Response variable
        response = self.__class__.eCustomizeResponse
        
        # Check that response status is 302
        self.assertEqual(response.status_code, 302)
        
        # Check that view redirects successful post to profile view
        self.assertRedirects(response, reverse('crm_user:profile'))
        
    def test_redirect_on_success_customer_customize_form(self):
        """ Test that Profile View redirects user to profile after successful CustomerCustomizeForm post """
        # Create Response variable
        response = self.__class__.cCustomizeResponse
        
        # Check that response status is 302
        self.assertEqual(response.status_code, 302)
        
        # Check that view redirects successful post to profile view
        self.assertRedirects(response, reverse('crm_user:profile'))
        
    def test_redirect_on_success_address_form(self):
        """ Test that Profile View redirects user to profile after successful AddressForm post """
        # Create Response variable
        response = self.__class__.cAddressResponse
        
        # Check that response status is 302
        self.assertEqual(response.status_code, 302)
        
        # Check that view redirects successful post to profile view
        self.assertRedirects(response, reverse('crm_user:profile'))
        
    def test_db_change_form(self):
        """ Test that a valid CustomUserChangeForm submitted by user updates database correctly. """
        # Create Response variable
        response = self.__class__.aChangeResponse

        # Check that response status is 302
        self.assertEqual(response.status_code, 302)
        
        # Check that database was updated correctly
        admin = Admin.objects.get(id=self.admin.id)
        self.assertEqual(admin.first_name, 'John')
        self.assertEqual(admin.middle_name, 'Jacob')
        self.assertEqual(admin.last_name, 'Smith')
        self.assertEqual(admin.email, 'jsmith@example.com')
        self.assertEqual(admin.birth_date, datetime.date(1993, 4, 14))
        self.assertEqual(admin.phone_number, '+12124448769')
        self.assertEqual(admin.last_modified_by, admin)
        self.assertEqual(admin.last_modified, timezone.now())
        #self.assertEqual(admin.profile_photo, self.photo )
    
    def test_db_address_form(self):
        """ Test that a valid AddressForm submitted by user updates database correctly. """
        # Create Response variable
        response = self.__class__.aAddressResponse

        # Check that response status is 302
        self.assertEqual(response.status_code, 302)
        
        # Check that database was updated correctly
        user = User.objects.get(id=self.admin.id)
        address = Address.objects.filter(user=user).first()
        self.assertIn(address, user.addresses.all())
        self.assertEqual(user.last_modified_by, user)
        self.assertEqual(user.last_modified, timezone.now())
        
    def test_db_admin_customize_form(self):
        """ Test that a valid AdminCustomizeForm submitted by user updates database correctly. """
        # Create Response variable
        response = self.__class__.aCustomizeResponse

        # Check that response status is 302
        self.assertEqual(response.status_code, 302)
        
        # Check that database was updated correctly
        user = Admin.objects.get(id=self.admin.id)
        self.assertEqual(user.last_modified_by, user)
        self.assertEqual(user.last_modified, timezone.now())
        self.assertEqual(user.admin_profile.theme, 'PURPLE')
        self.assertEqual(user.admin_profile.language, 'SPANISH')
        
    def test_db_employee_customize_form(self):
        """ Test that a valid EmployeeCustomizeForm submitted by user updates database correctly. """
        # Create Response variable
        response = self.__class__.eCustomizeResponse

        # Check that response status is 302
        self.assertEqual(response.status_code, 302)
        
        # Check that database was updated correctly
        user = Employee.objects.get(id=self.employee.id)
        self.assertEqual(user.last_modified_by, user)
        self.assertEqual(user.last_modified, timezone.now())
        self.assertEqual(user.emp_profile.theme, 'PURPLE')
        self.assertEqual(user.emp_profile.language, 'SPANISH')
        
    def test_db_customer_customize_form(self):
        """ Test that a valid CustomerCustomizeForm submitted by user updates database correctly. """
        # Create Response variable
        response = self.__class__.cCustomizeResponse

        # Check that response status is 302
        self.assertEqual(response.status_code, 302)
        
        # Check that database was updated correctly
        user = Customer.objects.get(id=self.customer.id)
        self.assertEqual(user.last_modified_by, user)
        self.assertEqual(user.last_modified, timezone.now())
        self.assertEqual(user.profile.theme, 'PURPLE')
        self.assertEqual(user.profile.language, 'SPANISH')
        
    def test_address_delete(self):
        """ Test that address is deleted successfully when checked """
        # Create Response variable
        response = self.__class__.aAddressResponse

        # Check that status is 302
        self.assertEqual(response.status_code, 302)
        
        # Check that address was created
        self.assertEqual(Address.objects.filter(id=1).exists(), True)
        
        # Create a Post request to delete Address in AddressForm
        response = self.aclient.post(reverse('crm_user:profile'), self.addressdatadelete)

        # Check that status is 302
        self.assertEqual(response.status_code, 302)
        
        # Check that address was deleted
        self.assertEqual(Address.objects.filter(id=1).exists(), False)
        
# Create a TestCase for Profile View Post Errors Request
# crm_user.tests.views.test_ProfileView.PostErrorsTests
@override_settings(MEDIA_ROOT=MEDIA_ROOT)
class PostErrorsTests(TestCase):
    """ Define a TestCase for Profile View Post Request """
    @classmethod 
    def setUpTestData(cls):
        # Create password 
        cls.password = 'P@ssw0rd3x@mpl3'
        
        # Create users 
        cls.admin = Admin.objects.create_user(email='admin@example.com', password=cls.password)
        cls.employee = Employee.objects.create_user(email='employee@example.com', password=cls.password)
        cls.customer = Customer.objects.create_user(email='customer@example.com', password=cls.password)
        
        # Create Form Data
        cls.photo = SimpleUploadedFile("test_image.jpg", b"test_content", "image/jpeg")
        cls.files = {
            'profile_photo': cls.photo,
        }
        long_name = 'hello' * 11
        cls.changedataerror = {
            'first_name': long_name,
            'middle_name': long_name,
            'last_name': long_name,
            'email': 'jsmith',
            'birth_date': '04-14-1993',
            'phone_number': '2125556890',
            'profile_photo': SimpleUploadedFile('photo.mp4', b'test_content', 'video'),
            'submitChange': True,
        }
        cls.customizedataerror = {
            'theme': 'INDIGO',
            'language': 'EN',
            'submitCustomize': True,
        }
        long_address = long_name * 6
        cls.addressdataerror = {
            'form-0-name': '',
            'form-0-type': '',
            'form-0-address_line1': '',
            'form-0-address_line2': long_address,
            'form-0-city': '',
            'form-0-state': 'Texas',
            'form-0-zip': '77891-123',
            'form-TOTAL_FORMS': 1,
            'form-INITIAL_FORMS': 0,
            'form-MAX-NUM_FORMS': 1000,            
            'form-MIN-NUM_FORMS': 0,            
            'submitAddress': True,
        }
        
        # Create User Clients
        cls.aclient = Client()
        cls.eclient = Client()
        cls.cclient = Client()
        
        # Log in User for each client
        cls.aclient.login(email=cls.admin.email, password=cls.password)
        cls.eclient.login(email=cls.employee.email, password=cls.password)
        cls.cclient.login(email=cls.customer.email, password=cls.password)
        
        # Create Post Request for Customize Form 
        cls.aCustomizeErrorResponse = cls.aclient.post(reverse('crm_user:profile'), cls.customizedataerror)
        cls.eCustomizeErrorResponse = cls.eclient.post(reverse('crm_user:profile'), cls.customizedataerror)
        cls.cCustomizeErrorResponse = cls.cclient.post(reverse('crm_user:profile'), cls.customizedataerror)
        
        # Create Post Request for Address Form
        cls.aAddressErrorResponse = cls.aclient.post(reverse('crm_user:profile'), cls.addressdataerror)
        cls.eAddressErrorResponse = cls.eclient.post(reverse('crm_user:profile'), cls.addressdataerror)
        cls.cAddressErrorResponse = cls.cclient.post(reverse('crm_user:profile'), cls.addressdataerror)
        
        # Create Post Request for Change Form 
        cls.aChangeErrorResponse = cls.aclient.post(reverse('crm_user:profile'), cls.changedataerror)
        cls.eChangeErrorResponse = cls.eclient.post(reverse('crm_user:profile'), cls.changedataerror)
        cls.cChangeErrorResponse = cls.cclient.post(reverse('crm_user:profile'), cls.changedataerror)
        
    @classmethod 
    def tearDownClass(cls):
        shutil.rmtree(MEDIA_ROOT, ignore_errors=True)
        super().tearDownClass()

    def test_template_on_errors_admin(self):
        """ Test that Profile View will render the correct template for admin users submitting an invalid form """
        # Create Response variable
        response = self.__class__.aAddressErrorResponse
        
        # Check that status code is "success"
        self.assertEqual(response.status_code, 200)

        # Check that the correct template is rendered for admin users
        self.assertTemplateUsed(response, 'crm_user/snippets/profile/admin_acct.html')
        self.assertTemplateUsed(response, 'crm_user/profile.html')
    
    def test_template_on_errors_employee(self):
        """ Test that Profile View will render the correct template for employee users submitting an invalid form """
        # Create Response variable
        response = self.__class__.eAddressErrorResponse
        
        # Check that status code is "success"
        self.assertEqual(response.status_code, 200)

        # Check that the correct template is rendered for employee users
        self.assertTemplateUsed(response, 'crm_user/snippets/profile/emp_acct.html')
        self.assertTemplateUsed(response, 'crm_user/profile.html')
    
    def test_template_on_errors_customer(self):
        """ Test that Profile View will render the correct template for customer users submitting an invalid form """
        # Create Response variable
        response = self.__class__.cAddressErrorResponse
        
        # Check that status code is "success"
        self.assertEqual(response.status_code, 200)

        # Check that the correct template is rendered for customer users
        self.assertTemplateUsed(response, 'crm_user/snippets/profile/cust_acct.html')
        self.assertTemplateUsed(response, 'crm_user/profile.html')
    
    def test_template_context_on_errors_address_form(self):
        """ Test that Profile View will render the correct template context for submitting an invalid AddressForm """
        # Create Response variable
        response = self.__class__.aAddressErrorResponse
        
        # Check that status code is "success"
        self.assertEqual(response.status_code, 200)

        # Check that the correct template context is rendered for admin users
        self.assertIsInstance(response.context['changeForm'], CustomUserChangeForm)
        self.assertEqual(response.context['changeForm'].instance, self.admin)
        self.assertIsInstance(response.context['customizeForm'], AdminCustomizeForm)
        self.assertEqual(response.context['customizeForm'].instance, self.admin.admin_profile)
        self.assertEqual(response.context['addressFormSet'][0]['name'].value(), self.addressdataerror['form-0-name'])
        self.assertEqual(response.context['addressFormSet'].queryset, None)
        self.assertEqual(response.context['addressFormSet'].extra, 1)
        self.assertEqual(response.context['addressFormSet'].can_delete, True)
        self.assertEqual(response.context['addressFormSet'].model, Address)
        self.assertIsInstance(response.context['addressFormSet'].forms[0], AddressForm)
        self.assertIsInstance(response.context['addressFormHelper'], AddressFormHelper)

    def test_template_context_on_errors_change_form(self):
        """ Test that Profile View will render the correct template context for submitting an invalid CustomUserChangeForm """
        # Create Response variable
        response = self.__class__.eChangeErrorResponse
        
        # Check that status code is "success"
        self.assertEqual(response.status_code, 200)

        # Check that the correct template context is rendered for employee users
        self.assertIsInstance(response.context['changeForm'], CustomUserChangeForm)
        self.assertEqual(response.context['changeForm'].instance, self.employee)
        self.assertEqual(response.context['changeForm']['first_name'].value(), self.changedataerror['first_name'])
        self.assertIsInstance(response.context['customizeForm'], EmployeeCustomizeForm)
        self.assertEqual(response.context['customizeForm'].instance, self.employee.emp_profile)
        self.assertQuerysetEqual(response.context['addressFormSet'].queryset, Address.objects.filter(user=self.employee))
        self.assertEqual(response.context['addressFormSet'].extra, 1)
        self.assertEqual(response.context['addressFormSet'].can_delete, True)
        self.assertEqual(response.context['addressFormSet'].model, Address)
        self.assertIsInstance(response.context['addressFormSet'].forms[0], AddressForm)
        self.assertIsInstance(response.context['addressFormHelper'], AddressFormHelper)

    def test_template_context_on_errors_admin_customize_form(self):
        """ Test that Profile View will render the correct template context for admin users submitting an invalid AdminCustomizeForm """
        # Create Response variable
        response = self.__class__.aCustomizeErrorResponse
        
        # Check that status code is "success"
        self.assertEqual(response.status_code, 200)

        # Check that the correct template context is rendered for customer users
        self.assertIsInstance(response.context['changeForm'], CustomUserChangeForm)
        self.assertEqual(response.context['changeForm'].instance, self.admin)
        self.assertIsInstance(response.context['customizeForm'], AdminCustomizeForm)
        self.assertEqual(response.context['customizeForm'].instance, self.admin.admin_profile)
        self.assertEqual(response.context['customizeForm']['language'].value(), self.customizedataerror['language'])
        self.assertEqual(response.context['customizeForm']['theme'].value(), self.customizedataerror['theme'])
        self.assertQuerysetEqual(response.context['addressFormSet'].queryset, Address.objects.filter(user=self.admin))
        self.assertEqual(response.context['addressFormSet'].extra, 1)
        self.assertEqual(response.context['addressFormSet'].can_delete, True)
        self.assertEqual(response.context['addressFormSet'].model, Address)
        self.assertIsInstance(response.context['addressFormSet'].forms[0], AddressForm)
        self.assertIsInstance(response.context['addressFormHelper'], AddressFormHelper)
    
    def test_template_context_on_errors_employee_customize_form(self):
        """ Test that Profile View will render the correct template context for employee users submitting an invalid EmployeeCustomizeForm """
        # Create Response variable
        response = self.__class__.eCustomizeErrorResponse
        
        # Check that status code is "success"
        self.assertEqual(response.status_code, 200)

        # Check that the correct template context is rendered for customer users
        self.assertIsInstance(response.context['changeForm'], CustomUserChangeForm)
        self.assertEqual(response.context['changeForm'].instance, self.employee)
        self.assertIsInstance(response.context['customizeForm'], EmployeeCustomizeForm)
        self.assertEqual(response.context['customizeForm'].instance, self.employee.emp_profile)
        self.assertEqual(response.context['customizeForm']['language'].value(), self.customizedataerror['language'])
        self.assertEqual(response.context['customizeForm']['theme'].value(), self.customizedataerror['theme'])
        self.assertQuerysetEqual(response.context['addressFormSet'].queryset, Address.objects.filter(user=self.employee))
        self.assertEqual(response.context['addressFormSet'].extra, 1)
        self.assertEqual(response.context['addressFormSet'].can_delete, True)
        self.assertEqual(response.context['addressFormSet'].model, Address)
        self.assertIsInstance(response.context['addressFormSet'].forms[0], AddressForm)
        self.assertIsInstance(response.context['addressFormHelper'], AddressFormHelper)
    
    def test_template_context_on_errors_customer_customize_form(self):
        """ Test that Profile View will render the correct template context for customer users submitting an invalid CustomerCustomizeForm """
        # Create Response variable
        response = self.__class__.cCustomizeErrorResponse
        
        # Check that status code is "success"
        self.assertEqual(response.status_code, 200)

        # Check that the correct template context is rendered for customer users
        self.assertIsInstance(response.context['changeForm'], CustomUserChangeForm)
        self.assertEqual(response.context['changeForm'].instance, self.customer)
        self.assertIsInstance(response.context['customizeForm'], CustomerCustomizeForm)
        self.assertEqual(response.context['customizeForm'].instance, self.customer.profile)
        self.assertEqual(response.context['customizeForm']['language'].value(), self.customizedataerror['language'])
        self.assertEqual(response.context['customizeForm']['theme'].value(), self.customizedataerror['theme'])
        self.assertQuerysetEqual(response.context['addressFormSet'].queryset, Address.objects.filter(user=self.customer))
        self.assertEqual(response.context['addressFormSet'].extra, 1)
        self.assertEqual(response.context['addressFormSet'].can_delete, True)
        self.assertEqual(response.context['addressFormSet'].model, Address)
        self.assertIsInstance(response.context['addressFormSet'].forms[0], AddressForm)
        self.assertIsInstance(response.context['addressFormHelper'], AddressFormHelper)

    def test_form_errors_change_form(self):
        """ Test that an invalid CustomUserChangeForm submitted by user displays correct form errors """
        # Create Response variable
        response = self.__class__.aChangeErrorResponse
        
        # Check that response status is 200
        self.assertEqual(response.status_code, 200)
        
        # Check that response displays correct form errors
        self.assertFormError(response, form='changeForm', field='email', errors='Enter a valid email address.',)
        self.assertFormError(response, form='changeForm', field='birth_date', errors='Enter a date in the format yyyy-mm-dd.')
        self.assertFormError(response, form='changeForm', field='phone_number', errors='Enter a valid phone number (e.g. +12125552368).')
        self.assertFormError(response, form='changeForm', field='profile_photo', errors='Upload a valid image. The file you uploaded was either not an image or a corrupted image.')
        self.assertFormError(response, form='changeForm', field='first_name', errors='Ensure this value has at most 50 characters (it has 55).')
        self.assertFormError(response, form='changeForm', field='middle_name', errors='Ensure this value has at most 50 characters (it has 55).')
        self.assertFormError(response, form='changeForm', field='last_name', errors='Ensure this value has at most 50 characters (it has 55).')
    
    def test_form_errors_admin_customize_form(self):
        """ Test that an invalid AdminCustomizeForm submitted by admin user displays correct form errors """
        # Create Response variable
        response = self.__class__.aCustomizeErrorResponse
        
        # Check that response status is 200
        self.assertEqual(response.status_code, 200)
        
        # Check that response displays correct form errors
        self.assertFormError(response, form='customizeForm', field='language', errors='Select a valid choice. EN is not one of the available choices.',)
        self.assertFormError(response, form='customizeForm', field='theme', errors='Select a valid choice. INDIGO is not one of the available choices.')
        
    def test_form_errors_customer_customize_form(self):
        """ Test that an invalid CustomerCustomizeForm submitted by customer user displays correct form errors """
        # Create Response variable
        response = self.__class__.cCustomizeErrorResponse
        
        # Check that response status is 200
        self.assertEqual(response.status_code, 200)
        
        # Check that response displays correct form errors
        self.assertFormError(response, form='customizeForm', field='language', errors='Select a valid choice. EN is not one of the available choices.',)
        self.assertFormError(response, form='customizeForm', field='theme', errors='Select a valid choice. INDIGO is not one of the available choices.')
        
    def test_form_errors_employee_customize_form(self):
        """ Test that an invalid EmployeeCustomizeForm submitted by employee user displays correct form errors """
        # Create Response variable
        response = self.__class__.eCustomizeErrorResponse
        
        # Check that response status is 200
        self.assertEqual(response.status_code, 200)
        
        # Check that response displays correct form errors
        self.assertFormError(response, form='customizeForm', field='language', errors='Select a valid choice. EN is not one of the available choices.',)
        self.assertFormError(response, form='customizeForm', field='theme', errors='Select a valid choice. INDIGO is not one of the available choices.')
        
    def test_form_errors_address_form(self):
        """ Test that an invalid AddressForm submitted by user displays correct form errors """
        # Create Response variable
        response = self.__class__.aAddressErrorResponse
        
        # Check that response status is 200
        self.assertEqual(response.status_code, 200)
        
        # Check that response displays correct form errors
        self.assertFormsetError(response, formset='addressFormSet', form_index=0, field='name', errors='This field is required.',)
        self.assertFormsetError(response, formset='addressFormSet', form_index=0, field='type', errors='This field is required.',)
        self.assertFormsetError(response, formset='addressFormSet', form_index=0, field='address_line1', errors='This field is required.',)
        self.assertFormsetError(response, formset='addressFormSet', form_index=0, field='address_line2', errors='Ensure this value has at most 254 characters (it has 330).',)
        self.assertFormsetError(response, formset='addressFormSet', form_index=0, field='city', errors='This field is required.')
        self.assertFormsetError(response, formset='addressFormSet', form_index=0, field='state', errors='Ensure this value has at most 2 characters (it has 5).')
        self.assertFormsetError(response, formset='addressFormSet', form_index=0, field='zip', errors='Enter a whole number.')
        
    
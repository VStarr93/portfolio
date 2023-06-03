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
    
# Create a TestCase for User Registration View Get Request with Customer login
# crm_user.tests.views.test_UserRegistrationView.GetCustomerLoginTests 
class GetCustomerLoginTests(TestCase):
    """ Define a TestCase for User Registration View Get Request with Customer login """
    def setUp(self):
        """ Define setUp for User Registration View Get Request with Customer login """
        self.password = 'P@ssw0rd3x@mpl3'
        self.customer = Customer.objects.create_user(email='customer@example.com', password=self.password)

    def test_redirect_user_registration_customer_logged_in(self):
        """ Test that User Registration View will redirect logged in customers to home page """
        # Log in customer 
        self.client.login(email=self.customer.email, password=self.password)
        
        # Create Get Request 
        response = self.client.get(reverse('crm_user:register'))
        
        # Check that status code is 302
        self.assertEqual(response.status_code, 302)
        
    def test_redirect_customer_logged_in_create_customer(self):
        """ Test that User Registration View will redirect logged in customers who click on customer to home page """
        # Log in customer 
        self.client.login(email=self.customer.email, password=self.password)
        
        # Create Get Request with customerBtn
        response = self.client.get(reverse('crm_user:register'), {'customerBtn': True})
        
        # Check that status code is 302
        self.assertEqual(response.status_code, 302)
        
    def test_redirect_customer_logged_in_create_admin(self):
        """ Test that User Registration View will redirect logged in customers who click on admin to home page """
        # Log in customer 
        self.client.login(email=self.customer.email, password=self.password)
        
        # Create Get Request with adminBtn
        response = self.client.get(reverse('crm_user:register'), {'adminBtn': True})
        
        # Check that status code is 302
        self.assertEqual(response.status_code, 302)
        
    def test_redirect_customer_logged_in_create_employee(self):
        """ Test that User Registration View will redirect logged in customers who click on employee to home page """
        # Log in customer 
        self.client.login(email=self.customer.email, password=self.password)
        
        # Create Get Request with empBtn 
        response = self.client.get(reverse('crm_user:register'), {'empBtn': True})
        
        # Check that status code is 302
        self.assertEqual(response.status_code, 302)
        
# Create a TestCase for User Registration View Get Request with Employee login
# crm_user.tests.views.test_UserRegistrationView.GetEmployeeLoginTests 
class GetEmployeeLoginTests(TestCase):
    """ Define a TestCase for User Registration View Get Request with Employee login """
    def setUp(self):
        """ Define setUp for User Registration View Get Request with Employee login """
        self.password = 'P@ssw0rd3x@mpl3'
        self.empManager = Employee.objects.create_user(email='empmanager@example.com', password=self.password)
        self.empManager.emp_profile.is_manager = True
        self.empManager.emp_profile.save()
        self.employee = Employee.objects.create_user(email='employee@example.com', password=self.password)
        
    def test_redirect_employee_logged_in_not_manager_create_employee(self):
        """ Test that User Registration View will redirect logged in employees that are not managers who click on employee to home page """
        # Log in employee
        self.client.login(email=self.employee.email, password=self.password)
        
        # Create Get Request wight empBtn
        response = self.client.get(reverse('crm_user:register'), {'empBtn': True})
        
        # Check that status code is 302
        self.assertEqual(response.status_code, 302)
        
    def test_redirect_employee_logged_in_not_manager_create_admin(self):
        """ Test that User Registration View will redirect logged in employees that are not managers who click on admin to home page """
        # Log in employee 
        self.client.login(email=self.employee.email, password=self.password)
        
        # Create Get Request with adminBtn 
        response = self.client.get(reverse('crm_user:register'), {'adminBtn': True})
        
        # Check that status code is 302
        self.assertEqual(response.status_code, 302)

    def test_template_employee_logged_in_manager_create_employee(self):
        """ Test that User Registration View will render correct template and context for logged in employees that are managers who click on employee """
        # log in employee as manager
        self.client.login(email=self.empManager.email, password=self.password)
        
        # Check that employee is a manager
        self.assertEqual(self.empManager.emp_profile.is_manager, True)
        
        # Create a Get Request with empBtn 
        response = self.client.get(reverse('crm_user:register'), {'empBtn': True,})
        
        # Check that status code is 200
        self.assertEqual(response.status_code, 200)
        
        # Check that correct template is rendered
        self.assertTemplateUsed(response, 'crm_user/registration.html')
        
        # check that correct template context is rendered
        self.assertEqual(response.context['form'], SimpleEmployeeCreationForm)

    def test_template_employee_logged_in_manager_create_admin(self):
        """ Test that User Registration View will render correct template and context for logged in employees that are managers who click on admin """
        # Log in employee as manager 
        self.client.login(email=self.empManager.email, password=self.password)
        
        # Check that employee is a manager
        self.assertEqual(self.empManager.emp_profile.is_manager, True)
        
        # Create a Get Request with adminBtn
        response = self.client.get(reverse('crm_user:register'), {'adminBtn': True})
        
        # check that status code is 200
        self.assertEqual(response.status_code, 200)
        
        # Check that correct template is rendered
        self.assertTemplateUsed(response, 'crm_user/registration.html')
        
        # check that correct template context is rendered
        self.assertEqual(response.context['form'], SimpleAdminCreationForm)

    def test_template_employee_logged_in_manager_create_customer(self):
        """ Test that User Registration View will render correct template and context for logged in employees that are managers who click on customer """
        # Log in employee as manager 
        self.client.login(email=self.empManager.email, password=self.password)
        
        # check that employee is a manager
        self.assertEqual(self.empManager.emp_profile.is_manager, True)
        
        # Create a Get Request with customerBtn
        response = self.client.get(reverse('crm_user:register'), {'customerBtn': True})
        
        # check that status code is 200 
        self.assertEqual(response.status_code, 200)
        
        # Check that correct template is rendered
        self.assertTemplateUsed(response, 'crm_user/registration.html')
        
        # check that correct template context is rendered
        self.assertEqual(response.context['form'], CustomerCreationForm)

    def test_template_employee_logged_in_not_manager_create_customer(self):
        """ Test that User Registration View will render correct template and context for logged in employees that are not managers who click on customer """
        # Log in employee 
        self.client.login(email=self.employee.email, password=self.password)
        
        # Create a Get Request with customerBtn
        response = self.client.get(reverse('crm_user:register'), {'customerBtn': True})
        
        # Check that status code is 200
        self.assertEqual(response.status_code, 200)
        
        # Check that correct template is rendered
        self.assertTemplateUsed(response, 'crm_user/registration.html')
        
        # check that correct template context is rendered
        self.assertEqual(response.context['form'], CustomerCreationForm)

    def test_template_user_registration_employee_logged_in(self):
        """ Test that User Registration View will render correct template for logged in employees """
        #Log in employee 
        self.client.login(email=self.employee.email, password=self.password)
        
        # Create a Get Request
        response = self.client.get(reverse('crm_user:register'))
        
        # Check that status code is 200
        self.assertEqual(response.status_code, 200)
        
        # Check that correct template is rendered
        self.assertTemplateUsed(response, 'crm_user/user_registration.html')
        
# Create a TestCase for User Registration View Get Request with Admin login
# crm_user.tests.views.test_UserRegistrationView.GetAdminLoginTests 
class GetAdminLoginTests(TestCase):
    """ Define a TestCase for User Registration View Get Request with Admin login """
    def setUp(self):
        """ Define setUp for User Registration View Get Request with Admin login """
        self.password = 'P@ssw0rd3x@mpl3'
        self.admin = Admin.objects.create_user(email='admin@example.com', password=self.password)

    def test_template_admin_logged_in_create_customer(self):
        """ Test that User Registration View will render correct template and context for logged in admins who click on customer """
        # Log in admin 
        self.client.login(email=self.admin.email, password=self.password)
        
        # Create a Get Request with customerBtn
        response = self.client.get(reverse('crm_user:register'), {'customerBtn': True})
        
        # Check that status code is 200
        self.assertEqual(response.status_code, 200)
        
        # Check that correct template is rendered
        self.assertTemplateUsed(response, 'crm_user/registration.html')
        
        # check that correct template context is rendered
        self.assertEqual(response.context['form'], CustomerCreationForm)

    def test_template_admin_logged_in_create_employee(self):
        """ Test that User Registratoin View will render correct template and context for logged in admins who click on employee """
        # log in admin 
        self.client.login(email=self.admin.email, password=self.password)
        
        # Create a Get Request with empBtn
        response = self.client.get(reverse('crm_user:register'), {'empBtn': True})
        
        # Check that status code is 200
        self.assertEqual(response.status_code, 200)
        
        # Check that correct template is rendered
        self.assertTemplateUsed(response, 'crm_user/registration.html')
        
        # check that correct template context is rendered
        self.assertEqual(response.context['form'], SimpleEmployeeCreationForm)

    def test_template_admin_logged_in_create_admin(self):
        """ Test that User Registration View will render correct template and context for logged in admins who click on admin """
        # log in admin
        self.client.login(email=self.admin.email, password=self.password)
        
        # Create a Get Request with adminBtn
        response = self.client.get(reverse('crm_user:register'), {'adminBtn': True})
        
        # Check that status code is 200
        self.assertEqual(response.status_code, 200)
        
        # Check that correct template is rendered
        self.assertTemplateUsed(response, 'crm_user/registration.html')
        
        # check that correct template context is rendered
        self.assertEqual(response.context['form'], SimpleAdminCreationForm)

    def test_template_user_registration_admin_logged_in(self):
        """ Test that User Registration View will render correct template for logged in admins """
        # Log in admin
        self.client.login(email=self.admin.email, password=self.password)
        
        # Create a Get Request
        response = self.client.get(reverse('crm_user:register'))
        
        # Check that status code is 200
        self.assertEqual(response.status_code, 200)
        
        # Check that correct template is rendered
        self.assertTemplateUsed(response, 'crm_user/user_registration.html')
        
# Create a TestCase for User Registration View Post Request with anonymous user
# crm_user.tests.views.test_UserRegistrationView.PostAnonUserTests
class PostAnonUserTests(TestCase):
    """ Define a TestCase for User Registration View Post Request with anonymous user """
    def setUp(self):
        """ Define setUp for User Registration View Post Request with anonymouse user """
        self.customerdata = {
            'first_name': 'John',
            'last_name': 'Smith',
            'email': 'jsmith@example.com',
            'password1': 'JSm1th3x@mpl3',
            'password2': 'JSm1th3x@mpl3',
            'submitCustomer': True,
        }
        self.customerdataerror = {
            'first_name': 'John'*50,
            'last_name': 'Smith'*50,
            'email': 'jsmith@example',
            'password1': 'JSm1th',
            'password2': 'JSm1th3x@mpl3',
            'submitCustomer': True,
        }
    
    def test_redirect_on_success_customer_creation_form(self):
        """ Test that User Registration View will redirect to login after successful post from anonymous user """
        # create a Post Request with customerdata 
        response = self.client.post(reverse('crm_user:register'), self.customerdata)
        
        # Check that status code is 302
        self.assertEqual(response.status_code, 302)
        
        # Check that view redirects to login page
        self.assertRedirects(response, reverse('login'), 302, 200)

    def test_redirect_on_employee_creation_form(self):
        """ Test that User Registration View will redirect to home page if post is from anonymous user """
        # Create a Post Request with submitEmployeeSimple
        response = self.client.post(reverse('crm_user:register'), {'submitEmployeeSimple': True})
        
        # Check that status code is 302
        self.assertEqual(response.status_code, 302)
        
        # Check that view redirects to home page
        self.assertRedirects(response, reverse('crm_user:home'), 302, 302)
        
    def test_redirect_on_admin_creation_form(self):
        """ Test that user Registration View will redirect to home page if post is from anonymous user """
        # Create a Post Request with submitAdminSimple
        response = self.client.post(reverse('crm_user:register'), {'submitAdminSimple': True})
    
        # Check that status code is 302
        self.assertEqual(response.status_code, 302)
        
        # Check that view redirects to home page 
        self.assertRedirects(response, reverse('crm_user:home'), 302, 302)
        
    def test_template_on_errors_customer_creation_form(self):
        """ Test that User Registration View will render correct template and context when anonymous user submits an invalid CustomerCreationForm """
        # Create a Post Request with customerdataerror
        response = self.client.post(reverse('crm_user:register'), self.customerdataerror)
        
        # Check that status code is 200
        self.assertEqual(response.status_code, 200)
        
        # Check that the correct template is rendered
        self.assertTemplateUsed(response, 'crm_user/registration.html')        
           
        # Check that the correct template context is rendered
        self.assertIsInstance(response.context['form'], CustomerCreationForm)
        
    def test_form_errors_customer_creation_form(self):
        """" Test that User Registration View will render correct form errors when anonymous user submits an invalid CustomerCreationForm """
        # Create a Post Request with customerdata
        response = self.client.post(reverse('crm_user:register'), self.customerdataerror)
        
        # Check that status code is 200
        self.assertEqual(response.status_code, 200)
        
        # Check that form errors are correctly rendered
        self.assertFormError(response, 'form', 'first_name', 'Ensure this value has at most 50 characters (it has 200).')
        self.assertFormError(response, 'form', 'last_name', 'Ensure this value has at most 50 characters (it has 250).')
        self.assertFormError(response, 'form', 'email', 'Enter a valid email address.')
        self.assertFormError(response, 'form', 'password2', "The two password fields didn’t match.")
        
    def test_db_customer_creation_form(self):
        """ Test that User Registration View will update database correctly when anonymous user submits a valid CustomerCreationForm """
        # Create a Post Request with customerdata
        response = self.client.post(reverse('crm_user:register'), self.customerdata)
        
        # Check that status is 302
        self.assertEqual(response.status_code, 302)
        
        # Check that user was created successfully
        self.assertEqual(Customer.objects.filter(email=self.customerdata['email']).exists(), True)
        
# Create a TestCase for User Registration View Post Request with customer login
# crm_user.tests.views.test_UserRegistrationView.PostLoginTests
class PostCustomerLoginTests(TestCase):
    """ Define a TestCase for User Registration View Post Request with Customer login """
    def setUp(self):
        """ Define setUp for User Registration View Post Request with Customer login """
        self.password = 'P@ssw0rd3x@mpl3'
        self.customer = Customer.objects.create_user(email='customer@example.com', password=self.password)

    def test_redirect_on_customer_creation_form(self):
        """ Test that User Registration View will redirect to home page if post is from customer user """
        # Log in customer 
        self.client.login(email=self.customer.email, password=self.password)
        
        # Create a Post Request with submitCustomer
        response = self.client.post(reverse('crm_user:register'), {'submitCustomer': True})
        
        # Check that status code is 302
        self.assertEqual(response.status_code, 302)
        
        # Check that view redirects to home page
        self.assertRedirects(response, reverse('crm_user:home'), 302, 200)
        
    def test_redirect_on_employee_creation_form(self):
        """ Test that User Registration View will redirect to home page if post is from customer user """
        # Log in customer 
        self.client.login(email=self.customer.email, password=self.password)
        
        # Create a Post Request with submitEmployee
        response = self.client.post(reverse('crm_user:register'), {'submitEmployeeSimple': True})
        
        # Check that status code is 302
        self.assertEqual(response.status_code, 302)
        
        # Check that view redirects to home page
        self.assertRedirects(response, reverse('crm_user:home'), 302, 200)
        
    def test_redirect_on_admin_creation_form(self):
        """ Test that user Registration View will redirect to home page if post is from customer user """
        # Log in customer 
        self.client.login(email=self.customer.email, password=self.password)
        
        # Create a Post Request with submitAdmin
        response = self.client.post(reverse('crm_user:register'), {'submitAdminSimple': True})
        
        # Check that status code is 302
        self.assertEqual(response.status_code, 302)
        
        # Check that view redirects to home page
        self.assertRedirects(response, reverse('crm_user:home'), 302, 200)
        
# Create a TestCase for User Registration View Post Request with employee login
# crm_user.tests.views.test_UserRegistrationView.PostEmployeeLoginTests
class PostEmployeeLoginTests(TestCase):
    """ Define a TestCase for User Registration View Post Request with Employee login """
    def setUp(self):
        """ Define setUp for User Registration View Post Request with Employee login """
        self.password = 'P@ssw0rd3x@mpl3'
        self.empManager = Employee.objects.create_user(email='empmanager@example.com', password=self.password)
        self.empManager.emp_profile.is_manager = True
        self.empManager.emp_profile.save()
        self.employee = Employee.objects.create_user(email='employee@example.com', password=self.password)
        self.data = {
            'first_name': 'John',
            'last_name': 'Smith',
            'email': 'jsmith@example.com',
            'password1': 'JSm1th3x@mpl3',
            'password2': 'JSm1th3x@mpl3',
        }
        self.dataerror = {
            'first_name': 'John'*50,
            'last_name': 'Smith'*50,
            'email': 'jsmith@example',
            'password1': 'JSm1th',
            'password2': 'JSm1th3x@mpl3',
        }
    
    def test_redirect_on_success_customer_creation_form(self):
        """ Test that User Registration View will redirect to login after successful post from Employee user """
        # Log in employee
        self.client.login(email=self.employee.email, password=self.password)
        
        # Add submitCustomer to data
        self.data['submitCustomer'] = True 
        
        # Create a Post Request with data
        response = self.client.post(reverse('crm_user:register'), data=self.data)
        
        # Check that status code is 302
        self.assertEqual(response.status_code, 302)
        
        # Check that view redirects to login
        self.assertRedirects(response, reverse('login'), 302, 200)
    
    def test_redirect_manager_on_success_employee_creation_form(self):
        """ Test that User Registration View will redirect to login if post is from Employee Manager user """
        # Log in employee manager
        self.client.login(email=self.empManager.email, password=self.password)
        
        # Add submitEmployeeSimple to data
        self.data['submitEmployeeSimple'] = True 
        
        # Create a Post Request with data
        response = self.client.post(reverse('crm_user:register'), data=self.data)
        
        # Check that status code is 302
        self.assertEqual(response.status_code, 302)
        
        # Check that view redirects to login
        self.assertRedirects(response, reverse('login'), 302, 200)
    
    def test_redirect_manager_on_success_admin_creation_form(self):
        """ Test that User Registration View will redirect to login if post is from Employee Manager user """
        # Log in employee manager
        self.client.login(email=self.empManager.email, password=self.password)
        
        # Add submitAdminSimple to data
        self.data['submitAdminSimple'] = True 
        
        # Create a Post Request with data
        response = self.client.post(reverse('crm_user:register'), data=self.data)
        
        # Check that status code is 302
        self.assertEqual(response.status_code, 302)
        
        # Check that view redirects to login
        self.assertRedirects(response, reverse('login'), 302, 200)
    
    def test_redirect_nonmanager_on_employee_creation_form(self):
        """ Test that User Registration View will redirect to home page if post is from Employee Nonmanager user """
        # Log in employee
        self.client.login(email=self.employee.email, password=self.password)
        
        # Add submitEmployeeSimple to data
        self.data['submitEmployeeSimple'] = True 
        
        # Create a Post Request with data
        response = self.client.post(reverse('crm_user:register'), self.data)
        
        # Check that status code is 302
        self.assertEqual(response.status_code, 302)
        
        # Check that view redirects to login
        self.assertRedirects(response, reverse('crm_user:home'), 302, 200)
        
        # Check that db was not updated
        self.assertEqual(Employee.objects.filter(email=self.data['email']).exists(), False)
    
    def test_redirect_nonmanager_on_admin_creation_form(self):
        """ Test that User Registration View will redirect to home page if post is from Employee Nonmanager user """
        # Log in employee
        self.client.login(email=self.employee.email, password=self.password)
        
        # Add submitAdminSimple to data
        self.data['submitAdminSimple'] = True 
        
        # Create a Post Request with data
        response = self.client.post(reverse('crm_user:register'), self.data)
        
        # Check that status code is 302
        self.assertEqual(response.status_code, 302)
        
        # Check that view redirects to login
        self.assertRedirects(response, reverse('crm_user:home'), 302, 200)
        
        # Check that db was not updated
        self.assertEqual(Employee.objects.filter(email=self.data['email']).exists(), False)
    
    def test_template_on_errors_customer_creation_form(self):
        """ Test that User Registration View will render correct template and context when Employee user submits an invalid CustomerCreationForm """
        # Log in employee
        self.client.login(email=self.employee.email, password=self.password)
        
        # Add submitCustomer to data
        self.dataerror['submitCustomer'] = True 
        
        # Create a Post Request with data
        response = self.client.post(reverse('crm_user:register'), self.dataerror)
        
        # Check that status code is 200
        self.assertEqual(response.status_code, 200)
        
        # Check that the correct template is rendered
        self.assertTemplateUsed(response, 'crm_user/registration.html')
        
        # Check that the correct template context is rendered
        self.assertIsInstance(response.context['form'], CustomerCreationForm)
        
    def test_template_on_errors_employee_creation_form(self):
        """ Test that User Registration View will render correct template and context when Employee user submits an invalid CustomerCreationForm """
        # Log in employee manager
        self.client.login(email=self.empManager.email, password=self.password)
        
        # Add submitEmployeeSimple to data
        self.dataerror['submitEmployeeSimple'] = True 
        
        # Create a Post Request with data
        response = self.client.post(reverse('crm_user:register'), self.dataerror)
        
        # Check that status code is 200
        self.assertEqual(response.status_code, 200)
        
        # Check that the correct template is rendered
        self.assertTemplateUsed(response, 'crm_user/registration.html')
        
        # Check that the correct template context is rendered
        self.assertIsInstance(response.context['form'], SimpleEmployeeCreationForm)
        
    def test_template_on_errors_admin_creation_form(self):
        """ Test that User Registration View will render correct template and context when Employee user submits an invalid CustomerCreationForm """
        # Log in employee manager
        self.client.login(email=self.empManager.email, password=self.password)
        
        # Add submitAdminSimple to data
        self.dataerror['submitAdminSimple'] = True 
        
        # Create a Post Request with data
        response = self.client.post(reverse('crm_user:register'), self.dataerror)
        
        # Check that status code is 200
        self.assertEqual(response.status_code, 200)
        
        # Check that the correct template is rendered
        self.assertTemplateUsed(response, 'crm_user/registration.html')
        
        # Check that the correct template context is rendered
        self.assertIsInstance(response.context['form'], SimpleAdminCreationForm)
        
    def test_form_errors_customer_creation_form(self):
        """" Test that User Registration View will render correct form errors when Employee user submits an invalid CustomerCreationForm """
        # Log in employee manager
        self.client.login(email=self.empManager.email, password=self.password)
        
        # Add submitCustomer to data
        self.dataerror['submitCustomer'] = True 
        
        # Create a Post Request with data
        response = self.client.post(reverse('crm_user:register'), self.dataerror)
        
        # Check that status code is 200
        self.assertEqual(response.status_code, 200)
        
        # Check that form errors are correctly rendered
        self.assertFormError(response, 'form', 'first_name', 'Ensure this value has at most 50 characters (it has 200).')
        self.assertFormError(response, 'form', 'last_name', 'Ensure this value has at most 50 characters (it has 250).')
        self.assertFormError(response, 'form', 'email', 'Enter a valid email address.')
        self.assertFormError(response, 'form', 'password2', "The two password fields didn’t match.")
        
    def test_form_errors_employee_creation_form(self):
        """" Test that User Registration View will render correct form errors when Employee user submits an invalid SimpleEmployeeCreationForm """
        # Log in employee manager
        self.client.login(email=self.empManager.email, password=self.password)
        
        # Add submitEmployeeSimple to data
        self.dataerror['submitEmployeeSimple'] = True 
        
        # Create a Post Request with data
        response = self.client.post(reverse('crm_user:register'), self.dataerror)
        
        # Check that status code is 200
        self.assertEqual(response.status_code, 200)
        
        # Check that form errors are correctly rendered
        self.assertFormError(response, 'form', 'first_name', 'Ensure this value has at most 50 characters (it has 200).')
        self.assertFormError(response, 'form', 'last_name', 'Ensure this value has at most 50 characters (it has 250).')
        self.assertFormError(response, 'form', 'email', 'Enter a valid email address.')
        
    def test_form_errors_admin_creation_form(self):
        """" Test that User Registration View will render correct form errors when Employee user submits an invalid SimpleAdminCreationForm """
        # Log in employee manager
        self.client.login(email=self.empManager.email, password=self.password)
        
        # Add submitAdminSimple to data
        self.dataerror['submitAdminSimple'] = True 
        
        # Create a Post Request with data
        response = self.client.post(reverse('crm_user:register'), self.dataerror)
        
        # Check that status code is 200
        self.assertEqual(response.status_code, 200)
        
        # Check that form errors are correctly rendered
        self.assertFormError(response, 'form', 'first_name', 'Ensure this value has at most 50 characters (it has 200).')
        self.assertFormError(response, 'form', 'last_name', 'Ensure this value has at most 50 characters (it has 250).')
        self.assertFormError(response, 'form', 'email', 'Enter a valid email address.')
        
    def test_db_customer_creation_form(self):
        """ Test that User Registration View will update database correctly when Employee user submits a valid CustomerCreationForm """
        # Log in employee manager
        self.client.login(email=self.empManager.email, password=self.password)
        
        # Add submitCustomer to data
        self.data['submitCustomer'] = True 
        
        # Create a Post Request with data
        response = self.client.post(reverse('crm_user:register'), self.data)
        
        # Check that status code is 200
        self.assertEqual(response.status_code, 302)
        
        # Check that user is created successfully
        self.assertEqual(Customer.objects.filter(email=self.data['email']).exists(), True)
        
    def test_db_employee_creation_form(self):
        """ Test that User Registration View will update database correctly when Employee user submits a valid SimpleEmployeeCreationForm """
        # Log in employee manager
        self.client.login(email=self.empManager.email, password=self.password)
        
        # Add submitEmployeeSimple to data
        self.data['submitEmployeeSimple'] = True 
        
        # Create a Post Request with data
        response = self.client.post(reverse('crm_user:register'), self.data)
        
        # Check that status code is 200
        self.assertEqual(response.status_code, 302)
        
        # Check that user is created successfully
        self.assertEqual(Employee.objects.filter(email=self.data['email']).exists(), True)
        
    def test_db_admin_creation_form(self):
        """ Test that User Registration View will update database correctly when Employee user submits a valid SimpleAdminCreationForm """
        # Log in employee manager
        self.client.login(email=self.empManager.email, password=self.password)
        
        # Add submitAdminSimple to data
        self.data['submitAdminSimple'] = True 
        
        # Create a Post Request with data
        response = self.client.post(reverse('crm_user:register'), self.data)
        
        # Check that status code is 200
        self.assertEqual(response.status_code, 302)
        
        # Check that user is created successfully
        self.assertEqual(Admin.objects.filter(email=self.data['email']).exists(), True)
        

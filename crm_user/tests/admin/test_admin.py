# crm_user/tests/admin/test_admin.py
#-------------------------------------------------------------
#-------------------------------------------------------------
# IMPORTS

from django.test import TestCase, Client, RequestFactory
from django.urls import reverse 

# Admin Tests 
from crm_user.admin import CustomUserAdmin
from crm_user.forms import CustomUserCreationForm
from crm_user.models import Admin, Employee, Customer, User
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from django.contrib.admin.sites import AdminSite
from django.contrib.admin import site

#-------------------------------------------------------------
#-------------------------------------------------------------
# Create your Variables here.


#-------------------------------------------------------------
#-------------------------------------------------------------
# Create your Admin tests here.

# Create a TestCase for CustomUserAdmin 
# crm_user.tests.admin.test_admin.CustomUserAdminTests 
class CustomUserAdminTests(TestCase):
    """ Define a TestCase for CustomUserAdmin """
    @classmethod 
    def setUpTestData(cls):
        """ Define setUpTestData method for CustomUserAdmin """
        # Create users
        cls.password = 'P@ssw0rd'
        cls.admin = Admin.objects.create_user(email='admin@example.com', password=cls.password)
        cls.admin.is_superuser = True 
        cls.admin.is_staff = True
        cls.admin.save()
        cls.employee = Employee.objects.create_user(email='employee@example.com', password=cls.password, is_active=False)
        cls.customer = Customer.objects.create_user(email='customer@example.com', password=cls.password, is_active=False)
        
        # Create client
        cls.aclient = Client()
        cls.eclient = Client()
        
        # Log in Client 
        cls.aclient.login(email=cls.admin.email, password=cls.password)
      
    def setUp(self):
        """ Define setUp method for CustomUserAdmin """
        self.factory = RequestFactory()
    def test_activate_users(self):
        """ Test activate_users method """
        # Create a queryset
        query = {self.employee.id, self.customer.id}
        
        # Create a response
        response = self.aclient.get(reverse('admin:crm_user_user_changelist'), follow=True)
        
        # Check that the status code is 200
        self.assertEqual(response.status_code, 200)
        
        # Check that users are inactive
        self.assertEqual(self.employee.is_active, False)
        self.assertEqual(self.customer.is_active, False)
        
        # Create data
        data = {
            'action': 'activate_users',
            '_selected_action': query,
        }
        
        # create post request
        response = self.aclient.post(reverse('admin:crm_user_user_changelist'), data)
        
        # Check that the status code is 302
        self.assertEqual(response.status_code, 302)
        
        # Check that users are active
        employee = Employee.objects.get(id=self.employee.id)
        customer = Customer.objects.get(id=self.customer.id)
        self.assertEqual(employee.is_active, True)
        self.assertEqual(customer.is_active, True)
        
    def test_activate_users_no_perm(self):
        """ Test that activate users action is not displayed to users with no permissions """
        # add statuses to allow user to log in to admin 
        self.employee.is_staff = True 
        self.employee.is_active = True
        self.employee.save()
        
        # Log in 
        self.eclient.login(email=self.employee.email, password=self.password)
        
        # Create a response
        response = self.eclient.get(reverse('admin:index'), follow=True)
        
        # Check that the status code is 200
        self.assertEqual(response.status_code, 200)
        
        # Create Request
        request = self.factory.get(reverse('admin:crm_user_user_changelist'))
        request.user = self.employee
        
        # Call get_actions method 
        instance = CustomUserAdmin(User, site)
        actions = instance.get_actions(request)
        
        # Check that 'activate_users' is not in list of actions
        self.assertNotIn('activate_users', actions)
        
    def test_get_form_not_superuser(self):
        """ Test get_form method """
        # Create Request
        request = self.factory.get(reverse('admin:crm_user_user_change', args=[int(self.customer.id)]))
        request.user = self.employee
        
        # Call get_actions method 
        instance = CustomUserAdmin(User, site)
        form = instance.get_form(request, self.customer)
        
        # Check disabled_fields
        self.assertEqual(form.base_fields['is_superuser'].disabled, True)
        self.assertEqual(form.base_fields['user_permissions'].disabled, True)
        self.assertEqual(form.base_fields['is_staff'].disabled, False)        
        self.assertEqual(form.base_fields['groups'].disabled, False)         
        
        
    def test_get_form_is_superuser(self):
        """ Test get_form method """
        # Create Request
        request = self.factory.get(reverse('admin:crm_user_user_change', args=[int(self.customer.id)]))
        request.user = self.admin
        
        # Call get_actions method 
        instance = CustomUserAdmin(User, site)
        form = instance.get_form(request, self.customer)
        
        # Check disabled_fields
        self.assertEqual(form.base_fields['is_superuser'].disabled, False)
        self.assertEqual(form.base_fields['user_permissions'].disabled, False)
        self.assertEqual(form.base_fields['is_staff'].disabled, False)        
        self.assertEqual(form.base_fields['groups'].disabled, False)        
                 
        
    def test_get_form_not_superuser_editing_self(self):
        """ Test get_form method """
        # Create Request
        request = self.factory.get(reverse('admin:crm_user_user_change', args=[int(self.customer.id)]))
        request.user = self.employee
        
        # Call get_actions method 
        instance = CustomUserAdmin(User, site)
        form = instance.get_form(request, self.employee)
        
        # Check disabled_fields
        self.assertEqual(form.base_fields['is_superuser'].disabled, True)
        self.assertEqual(form.base_fields['user_permissions'].disabled, True) 
        self.assertEqual(form.base_fields['is_staff'].disabled, True)        
        self.assertEqual(form.base_fields['groups'].disabled, True)        
        
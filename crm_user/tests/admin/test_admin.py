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

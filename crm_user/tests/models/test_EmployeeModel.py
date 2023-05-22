#./crm_user/tests/models/test_EmployeeModel.py
#-------------------------------------------------------------
#-------------------------------------------------------------
# IMPORTS

from django.test import TestCase, override_settings
from crm_user.models import Employee
from django.core.files.uploadedfile import SimpleUploadedFile 
import shutil, tempfile 
from django.db.models.fields import NOT_PROVIDED
from django.utils import timezone
from freezegun import freeze_time

# For Testing Email Services
from django.core import mail 

#-------------------------------------------------------------
#-------------------------------------------------------------
# Create your Variables here.

MEDIA_ROOT = tempfile.mkdtemp()


#-------------------------------------------------------------
#-------------------------------------------------------------
# Create your Employee - PROXY Model tests here.

# Create a TestCase for Employee Labels
# crm_user.tests.models.test_EmployeeModel.LabelTests
class LabelTests(TestCase):
    """ Define a TestCase for Employee Model Labels """
    @classmethod 
    def setUpTestData(cls):
        """ Define setUpTestData method for Employee Model Labels """
        Employee.objects.create_user(
            email="doe@example.com",
            first_name="Sara",
            middle_name="Lee",
            last_name="Doe",
            birth_date='1993-04-14',
            profile_photo=SimpleUploadedFile("test_image.jpg", b"test_content", "image/jpeg"),
            phone_number="+12125556789",
        )
        
    def setUp(self):
        """ Define setUp method for Employee Model Labels """
        self.user = Employee.objects.get(id=1)
        
    def test_id_label(self):
        """ Test for Employee Model ID Label """
        field_label = self.user._meta.get_field('id').verbose_name 
        self.assertEqual(field_label, 'ID')
        
    def test_type_label(self):
        """ Test for Employee Model Type Label """
        field_label = self.user._meta.get_field('type').verbose_name
        self.assertEqual(field_label, 'Type')
        
    def test_email_label(self):
        """ Test for Employee Model Email Label """
        field_label = self.user._meta.get_field('email').verbose_name 
        self.assertEqual(field_label, 'Email')
        
    def test_first_name_label(self):
        """ Test for Employee Model First Name Label """
        field_label = self.user._meta.get_field('first_name').verbose_name 
        self.assertEqual(field_label, 'First Name')

    def test_middle_name_label(self):
        """ Test for Employee Model Middle Name Label """
        field_label = self.user._meta.get_field('middle_name').verbose_name 
        self.assertEqual(field_label, 'Middle Name')
        
    def test_last_name_label(self):
        """ Test for Employee Model Last Name Label """
        field_label = self.user._meta.get_field('last_name').verbose_name
        self.assertEqual(field_label, 'Last Name')
        
    def test_birth_date_label(self):
        """ Test for Employee Model Birth Date Label """
        field_label = self.user._meta.get_field('birth_date').verbose_name 
        self.assertEqual(field_label, 'Birth Date')
        
    def test_profile_photo_label(self):
        """ Test for Employee Model Profile Photo Label """
        field_label = self.user._meta.get_field('profile_photo').verbose_name 
        self.assertEqual(field_label, 'Profile Photo')
        
    def test_phone_number_label(self):
        """ Test for Employee Model Phone Number Label """
        field_label = self.user._meta.get_field('phone_number').verbose_name 
        self.assertEqual(field_label, 'Phone Number')
        
    def test_last_modified_label(self):
        """ Test for Employee Model Last Modified Label """
        field_label = self.user._meta.get_field('last_modified').verbose_name 
        self.assertEqual(field_label, 'Last Modified')
        
    def test_last_modified_by_label(self):
        """ Test for Employee Model Last Modified By Label """
        field_label = self.user._meta.get_field('last_modified_by').verbose_name 
        self.assertEqual(field_label, 'Last Modified By')


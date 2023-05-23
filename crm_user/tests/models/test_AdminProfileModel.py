#./crm_user/tests/models/test_AdminProfileModel.py
#-------------------------------------------------------------
#-------------------------------------------------------------
# IMPORTS

from django.test import TestCase
from crm_user.models import Admin, AdminProfile
from django.core.files.uploadedfile import SimpleUploadedFile 
from django.db.models.fields import NOT_PROVIDED

# For Testing Email Services
from django.core import mail 

#-------------------------------------------------------------
#-------------------------------------------------------------
# Create your Variables here.


#-------------------------------------------------------------
#-------------------------------------------------------------
# Create your AdminProfile Model tests here.

# Create a TestCase for Admin Profile Labels
# crm_user.tests.models.test_AdminProfileModel.LabelTests
class LabelTests(TestCase):
    """ Define a TestCase for Admin Profile Model Labels """
    @classmethod 
    def setUpTestData(cls):
        """ Define setUpTestData method for Admin Profile Model Labels """
        Admin.objects.create_user(
            email="doe@example.com",
            first_name="Sara",
            middle_name="Lee",
            last_name="Doe",
            birth_date='1993-04-14',
            profile_photo=SimpleUploadedFile("test_image.jpg", b"test_content", "image/jpeg"),
            phone_number="+12125556789",
        )
        
    def setUp(self):
        """ Define setUp method for Admin Profile Model Labels """
        self.user = AdminProfile.objects.get(id=1)
        
    def test_id_label(self):
        """ Test for Admin Profile Model ID Label """
        field_label = self.user._meta.get_field('id').verbose_name 
        self.assertEqual(field_label, 'ID')
        
    def test_work_id_label(self):
        """ Test for Admin Profile Model Work ID Label """
        field_label = self.user._meta.get_field('work_id').verbose_name 
        self.assertEqual(field_label, 'Work ID')
        
    def test_status_label(self):
        """ Test for Admin Profile Model Status Label """
        field_label = self.user._meta.get_field('status').verbose_name
        self.assertEqual(field_label, 'Status')
        
    def test_user_label(self):
        """ Test for Admin Profile Model User Label """
        field_label = self.user._meta.get_field('user').verbose_name 
        self.assertEqual(field_label, 'Admin')

    def test_is_manager_label(self):
        """ Test for Admin Profile Model Is Manager Label """
        field_label = self.user._meta.get_field('is_manager').verbose_name 
        self.assertEqual(field_label, 'Is Manager')

    def test_language_label(self):
        """ Test for Admin Profile Model Language Label """
        field_label = self.user._meta.get_field('language').verbose_name 
        self.assertEqual(field_label, 'Language')
        
    def test_theme_label(self):
        """ Test for Admin Profile Model Theme Label """
        field_label = self.user._meta.get_field('theme').verbose_name
        self.assertEqual(field_label, 'Theme')
        
# Create a TestCase for Admin Profile Max Lengths
# crm_user.tests.models.test_AdminProfileModel.MaxLengthTests
class MaxLengthTests(TestCase):
    """ Define a TestCase for Admin Profile Model Max Lengths """
    @classmethod 
    def setUpTestData(cls):
        """ Define setUpTestData method for Admin Profile Model Max Lengths """
        Admin.objects.create_user(
            email="doe@example.com",
            first_name="Sara",
            middle_name="Lee",
            last_name="Doe",
            birth_date='1993-04-14',
            profile_photo=SimpleUploadedFile("test_image.jpg", b"test_content", "image/jpeg"),
            phone_number="+12125556789",
        )
        
    def setUp(self):
        """ Define setUp method for Admin Profile Model Max Lengths """
        self.user = AdminProfile.objects.get(id=1)
        
    def test_id_max_length(self):
        """ Test for Admin Profile Model ID Max Length """
        max_length = self.user._meta.get_field('id').max_length 
        self.assertEqual(max_length, None)
        
    def test_work_id_max_length(self):
        """ Test for Admin Profile Model Work ID Max Length """
        max_length = self.user._meta.get_field('work_id').max_length 
        self.assertEqual(max_length, None)
        
    def test_status_max_length(self):
        """ Test for Admin Profile Model Status Max Length """
        max_length = self.user._meta.get_field('status').max_length
        self.assertEqual(max_length, 10)
        
    def test_user_max_length(self):
        """ Test for Admin Profile Model User Max Length """
        max_length = self.user._meta.get_field('user').max_length 
        self.assertEqual(max_length, None)

    def test_is_manager_max_length(self):
        """ Test for Admin Profile Model Is Manager Max Length """
        max_length = self.user._meta.get_field('is_manager').max_length 
        self.assertEqual(max_length, None)

    def test_language_max_length(self):
        """ Test for Admin Profile Model Language Max Length """
        max_length = self.user._meta.get_field('language').max_length 
        self.assertEqual(max_length, 10)
        
    def test_theme_max_length(self):
        """ Test for Admin Profile Model Theme Max Length """
        max_length = self.user._meta.get_field('theme').max_length
        self.assertEqual(max_length, 6)
        

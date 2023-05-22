#./crm_user/tests/models/test_CustomerModel.py
#-------------------------------------------------------------
#-------------------------------------------------------------
# IMPORTS

from django.test import TestCase, override_settings
from crm_user.models import Customer 
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
# Create your Customer - PROXY Model tests here.

# Create a TestCase for Customer Labels
# crm_user.tests.models.test_CustomerModel.LabelTests
class LabelTests(TestCase):
    """ Define a TestCase for Customer Model Labels """
    @classmethod 
    def setUpTestData(cls):
        """ Define setUpTestData method for Customer Model Labels """
        Customer.objects.create_user(
            email="doe@example.com",
            first_name="Sara",
            middle_name="Lee",
            last_name="Doe",
            birth_date='1993-04-14',
            profile_photo=SimpleUploadedFile("test_image.jpg", b"test_content", "image/jpeg"),
            phone_number="+12125556789",
        )
        
    def setUp(self):
        """ Define setUp method for Customer Model Labels """
        self.user = Customer.objects.get(id=1)
        
    def test_id_label(self):
        """ Test for Customer Model ID Label """
        field_label = self.user._meta.get_field('id').verbose_name 
        self.assertEqual(field_label, 'ID')
        
    def test_type_label(self):
        """ Test for Customer Model Type Label """
        field_label = self.user._meta.get_field('type').verbose_name
        self.assertEqual(field_label, 'Type')
        
    def test_email_label(self):
        """ Test for Customer Model Email Label """
        field_label = self.user._meta.get_field('email').verbose_name 
        self.assertEqual(field_label, 'Email')
        
    def test_first_name_label(self):
        """ Test for Customer Model First Name Label """
        field_label = self.user._meta.get_field('first_name').verbose_name 
        self.assertEqual(field_label, 'First Name')

    def test_middle_name_label(self):
        """ Test for Customer Model Middle Name Label """
        field_label = self.user._meta.get_field('middle_name').verbose_name 
        self.assertEqual(field_label, 'Middle Name')
        
    def test_last_name_label(self):
        """ Test for Customer Model Last Name Label """
        field_label = self.user._meta.get_field('last_name').verbose_name
        self.assertEqual(field_label, 'Last Name')
        
    def test_birth_date_label(self):
        """ Test for Customer Model Birth Date Label """
        field_label = self.user._meta.get_field('birth_date').verbose_name 
        self.assertEqual(field_label, 'Birth Date')
        
    def test_profile_photo_label(self):
        """ Test for Customer Model Profile Photo Label """
        field_label = self.user._meta.get_field('profile_photo').verbose_name 
        self.assertEqual(field_label, 'Profile Photo')
        
    def test_phone_number_label(self):
        """ Test for Customer Model Phone Number Label """
        field_label = self.user._meta.get_field('phone_number').verbose_name 
        self.assertEqual(field_label, 'Phone Number')
        
    def test_last_modified_label(self):
        """ Test for Customer Model Last Modified Label """
        field_label = self.user._meta.get_field('last_modified').verbose_name 
        self.assertEqual(field_label, 'Last Modified')
        
    def test_last_modified_by_label(self):
        """ Test for Customer Model Last Modified By Label """
        field_label = self.user._meta.get_field('last_modified_by').verbose_name 
        self.assertEqual(field_label, 'Last Modified By')

# Create a TestCase for Customer Max Lengths
# crm_user.tests.models.test_CustomerModel.MaxLengthTests
class MaxLengthTests(TestCase):
    """ Define a TestCase for Customer Model Max Lengths """
    @classmethod 
    def setUpTestData(cls):
        """ Define setUpTestData method for Customer Model Max Lengths """
        Customer.objects.create_user(
            email="doe@example.com",
            first_name="Sara",
            middle_name="Lee",
            last_name="Doe",
            birth_date='1993-04-14',
            profile_photo=SimpleUploadedFile("test_image.jpg", b"test_content", "image/jpeg"),
            phone_number="+12125556789",
        )
        
    def setUp(self):
        """ Define setUp method for Customer Model Max Lengths """
        self.user = Customer.objects.get(id=1)
        
    def test_id_max_length(self):
        """ Test for Customer Model ID Max Length """
        field_max_length = self.user._meta.get_field('id').max_length 
        self.assertEqual(field_max_length, None)
        
    def test_type_max_length(self):
        """ Test for Customer Model Type Max Length """
        field_max_length = self.user._meta.get_field('type').max_length
        self.assertEqual(field_max_length, 8)
        
    def test_email_max_length(self):
        """ Test for Customer Model Email Max Length """
        field_max_length = self.user._meta.get_field('email').max_length 
        self.assertEqual(field_max_length, 254)
        
    def test_first_name_max_length(self):
        """ Test for Customer Model First name Max Length """
        field_max_length = self.user._meta.get_field('first_name').max_length
        self.assertEqual(field_max_length, 50)
        
    def test_middle_name_max_length(self):
        """ Test for Customer Model Middle Name Max Length """
        field_max_length = self.user._meta.get_field('middle_name').max_length 
        self.assertEqual(field_max_length, 50)
    
    def test_last_name_max_length(self):
        """ Test for Customer Model Last Name Max Length """
        field_max_length = self.user._meta.get_field('last_name').max_length 
        self.assertEqual(field_max_length, 50)
        
    def test_birth_date_max_length(self):
        """ Test for Customer Model Birth Date Max Length """
        field_max_length = self.user._meta.get_field('birth_date').max_length 
        self.assertEqual(field_max_length, None)
        
    def test_profile_photo_max_length(self):
        """ Test for Customer Model Profile Photo Max Length """
        field_max_length = self.user._meta.get_field('profile_photo').max_length 
        self.assertEqual(field_max_length, 100)
        
    def test_phone_number_max_length(self):
        """ Test for Customer Model Phone Number Max Length """
        field_max_length = self.user._meta.get_field('phone_number').max_length 
        self.assertEqual(field_max_length, 128)
        
    def test_last_modified_max_length(self):
        """ Test for Customer Model Last Modified Max Length """
        field_max_length = self.user._meta.get_field('last_modified').max_length
        self.assertEqual(field_max_length, None)
        
    def test_last_modified_by_max_length(self):
        """ Test for Customer Model Last Modified By Max Length """
        field_max_length = self.user._meta.get_field('last_modified_by').max_length 
        self.assertEqual(field_max_length, None)
        

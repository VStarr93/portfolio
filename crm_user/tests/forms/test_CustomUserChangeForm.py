#./crm_user/tests/forms/test_CustomUserChangeForm.py
#-------------------------------------------------------------
#-------------------------------------------------------------
# IMPORTS

from django.test import TestCase
from crm_user.forms import CustomUserChangeForm
from crm_user.models import User
from django.core.files.uploadedfile import SimpleUploadedFile 

#-------------------------------------------------------------
#-------------------------------------------------------------
# Create your Variables here.


#-------------------------------------------------------------
#-------------------------------------------------------------
# Create your Custom User Change Form tests here.

# Create a TestCase for CustomUserChangeForm Labels 
# crm_user.tests.forms.test_CustomUserChangeForm.FormLabelTests 
class FormLabelTests(TestCase):
    """ Define a TestCase for CustomUserChangeForm Labels """
    @classmethod
    def setUpTestData(cls):
        """ FormLabel setUpTestData method to create test user """
        User.objects.create(email='test@example.com', password='T3st3x@mpl3')
        
    def setUp(self):
        """ FormLabel setUp method to create form data """
        self.user = User.objects.get(email='test@example.com')
        self.photo = SimpleUploadedFile("test_image.jpg", b"test_content", "image/jpeg")
        self.formdata = {
            'first_name': 'Sara',
            'middle_name': 'Elizabeth',
            'last_name': 'Jackson',
            'email': 'test@example.com',
            'birth_date': '1993-04-14',
            'phone_number': '+12125552368',
            'profile_photo': self.photo,
        }
    
    def test_change_field_first_name_label(self):
        """ Define a test for first_name field label """
        form = CustomUserChangeForm(self.formdata)
        self.assertTrue(form.fields['first_name'].label == 'First Name')
        
    def test_change_field_middle_name_label(self):
        """ Define a test for middle_name field label """
        form = CustomUserChangeForm(self.formdata)
        self.assertTrue(form.fields['middle_name'].label == 'Middle Name')
        
    def test_change_field_last_name_label(self):
        """ Define a test for last_name field label """
        form = CustomUserChangeForm(self.formdata)
        self.assertTrue(form.fields['last_name'].label == 'Last Name')
        
    def test_change_field_email_label(self):
        """ Define a test for email field label """
        form = CustomUserChangeForm(self.formdata)
        self.assertTrue(form.fields['email'].label == 'Email')
        
    def test_change_field_birth_date_label(self):
        """ Define a test for birth date field label """
        form = CustomUserChangeForm(self.formdata)
        self.assertTrue(form.fields['birth_date'].label == 'Birth Date')
        
    def test_change_field_phone_number_label(self):
        """ Define a test for phone number field label """
        form = CustomUserChangeForm(self.formdata)
        self.assertTrue(form.fields['phone_number'].label == 'Phone Number')
    
    def test_change_field_profile_photo_label(self):
        """ Define a test for profile photo field label """
        form = CustomUserChangeForm(self.formdata)
        self.assertTrue(form.fields['profile_photo'].label == 'Profile Photo')
              

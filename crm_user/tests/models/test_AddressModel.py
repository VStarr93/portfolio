#./crm_user/tests/models/test_AddressModel.py
#-------------------------------------------------------------
#-------------------------------------------------------------
# IMPORTS

from django.test import TestCase
from crm_user.models import Address, User
import datetime 

# For Testing Email Services
from django.core import mail 

#-------------------------------------------------------------
#-------------------------------------------------------------
# Create your Variables here.


#-------------------------------------------------------------
#-------------------------------------------------------------
# Create your Address Model tests here.

# Create a TestCase for Address Labels
# crm_user.tests.models.test_AddressModel.LabelTests
class LabelTests(TestCase):
    """ Define a TestCase for Address Model Labels """
    @classmethod 
    def setUpTestData(cls):
        """ Define setUpTestData method for Address Model Labels """
        User.objects.create_user(
            first_name="Sara",
            last_name="Doe",
            email="doe@example.com",
            type="CUSTOMER"
        )
        Address.objects.create(
            user=User.objects.get(id=1),
            name='home',
            type='RESIDENTIAL',
            address_line1='123 Sara Lane',
            city='Spring',
            state='TX',
            zip=77091
        )
        
    def setUp(self):
        """ Define setUp method for Address Model Labels """
        self.address = Address.objects.get(id=1)
        self.user = User.objects.get(id=1)
        
    def test_id_label(self):
        """ Test for Address Model ID Label """
        field_label = self.address._meta.get_field('id').verbose_name 
        self.assertEqual(field_label, 'ID')
        
    def test_last_modified_label(self):
        """ Test for Address Model Last Modified Label """
        field_label = self.address._meta.get_field('last_modified').verbose_name
        self.assertEqual(field_label, 'Last Modified')
        
    def test_last_modified_by_label(self):
        """ Test for Address Model Last Modified By Label """
        field_label = self.address._meta.get_field('last_modified_by').verbose_name
        self.assertEqual(field_label, 'Last Modified By')
        
    def test_address_line2_label(self):
        """ Test for Address Model Address Line2 Label """
        field_label = self.address._meta.get_field('address_line2').verbose_name 
        self.assertEqual(field_label, 'Address Line 2')
        
    def test_user_label(self):
        """ Test for Address Model User Label """
        field_label = self.address._meta.get_field('user').verbose_name 
        self.assertEqual(field_label, 'User')

    def test_address_line1_label(self):
        """ Test for Address Model Address Line1 Label """
        field_label = self.address._meta.get_field('address_line1').verbose_name 
        self.assertEqual(field_label, 'Address Line 1')
        
    def test_city_label(self):
        """ Test for Address Model City Label """
        field_label = self.address._meta.get_field('city').verbose_name
        self.assertEqual(field_label, 'City')
        
    def test_state_label(self):
        """ Test for Address Model State Label """
        field_label = self.address._meta.get_field('state').verbose_name 
        self.assertEqual(field_label, 'State')
        
    def test_zip_label(self):
        """ Test for Address Model Zip Label """
        field_label = self.address._meta.get_field('zip').verbose_name 
        self.assertEqual(field_label, 'Zip')
        
    def test_type_label(self):
        """ Test for Address Model Type Label """
        field_label = self.address._meta.get_field('type').verbose_name
        self.assertEqual(field_label, 'Type')
        
    def test_name_label(self):
        """ Test for Address Model Name Label """
        field_label = self.address._meta.get_field('name').verbose_name 
        self.assertEqual(field_label, 'Name')
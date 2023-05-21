#./crm_user/tests/models/test_AddressModel.py
#-------------------------------------------------------------
#-------------------------------------------------------------
# IMPORTS

from django.test import TestCase
from crm_user.models import Address, User
from django.db.models.fields import NOT_PROVIDED

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

# Create a TestCase for Address Max Lengths
# crm_user.tests.models.test_AddressModel.MaxLengthTests
class MaxLengthTests(TestCase):
    """ Define a TestCase for Address Model Max Lengths """
    @classmethod 
    def setUpTestData(cls):
        """ Define setUpTestData method for Address Model Max Lengths """
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
        """ Define setUp method for Address Model Max Lengths """
        self.address = Address.objects.get(id=1)
        self.user = User.objects.get(id=1)
        
    def test_id_max_length(self):
        """ Test for Address Model ID Max Length """
        field_label = self.address._meta.get_field('id').max_length 
        self.assertEqual(field_label, None)
        
    def test_address_line2_max_length(self):
        """ Test for Address Model Address Line2 Max Length """
        field_label = self.address._meta.get_field('address_line2').max_length 
        self.assertEqual(field_label, 254)
        
    def test_user_max_length(self):
        """ Test for Address Model User Max Length """
        field_label = self.address._meta.get_field('user').max_length 
        self.assertEqual(field_label, None )

    def test_address_line1_max_length(self):
        """ Test for Address Model Address Line1 Max Length """
        field_label = self.address._meta.get_field('address_line1').max_length 
        self.assertEqual(field_label, 254)
        
    def test_city_max_length(self):
        """ Test for Address Model City Max Length """
        field_label = self.address._meta.get_field('city').max_length
        self.assertEqual(field_label, 254)
        
    def test_state_max_length(self):
        """ Test for Address Model State Max Length """
        field_label = self.address._meta.get_field('state').max_length 
        self.assertEqual(field_label, 2)
        
    def test_zip_max_length(self):
        """ Test for Address Model Zip Max Length """
        field_label = self.address._meta.get_field('zip').max_length 
        self.assertEqual(field_label, None)
        
    def test_type_max_length(self):
        """ Test for Address Model Type Max Length """
        field_label = self.address._meta.get_field('type').max_length
        self.assertEqual(field_label, 11)
        
    def test_name_max_length(self):
        """ Test for Address Model Name Max Length """
        field_label = self.address._meta.get_field('name').max_length 
        self.assertEqual(field_label, 100)
        
# Create a TestCase for Address Help Text
# crm_user.tests.models.test_AddressModel.HelpTextTests
class HelpTextTests(TestCase):
    """ Define a TestCase for Address Model Help Text """
    @classmethod 
    def setUpTestData(cls):
        """ Define setUpTestData method for Address Model Help Text """
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
        """ Define setUp method for Address Model Help Text """
        self.address = Address.objects.get(id=1)
        self.user = User.objects.get(id=1)
        
    def test_id_help_text(self):
        """ Test for Address Model ID Help Text """
        field_help_text = self.address._meta.get_field('id').help_text 
        self.assertEqual(field_help_text, '')
        
    def test_address_line2_help_text(self):
        """ Test for Address Model Address Line2 Help Text """
        field_help_text = self.address._meta.get_field('address_line2').help_text 
        self.assertEqual(field_help_text, 'Enter the apartment or suite number')
        
    def test_user_help_text(self):
        """ Test for Address Model User Help Text """
        field_help_text = self.address._meta.get_field('user').help_text 
        self.assertEqual(field_help_text, 'The user who lives at this address' )

    def test_address_line1_help_text(self):
        """ Test for Address Model Address Line1 Help Text """
        field_help_text = self.address._meta.get_field('address_line1').help_text 
        self.assertEqual(field_help_text, 'Enter the street number and street name')
        
    def test_city_help_text(self):
        """ Test for Address Model City Help Text """
        field_help_text = self.address._meta.get_field('city').help_text
        self.assertEqual(field_help_text, 'Enter the city')
        
    def test_state_help_text(self):
        """ Test for Address Model State Help Text """
        field_help_text = self.address._meta.get_field('state').help_text 
        self.assertEqual(field_help_text, 'Enter the state as a 2 letter initial')
        
    def test_zip_help_text(self):
        """ Test for Address Model Zip Help Text """
        field_help_text = self.address._meta.get_field('zip').help_text 
        self.assertEqual(field_help_text, 'Enter the zip code')
        
    def test_type_help_text(self):
        """ Test for Address Model Type Help Text """
        field_help_text = self.address._meta.get_field('type').help_text
        self.assertEqual(field_help_text, 'Select the correct address type')
        
    def test_name_help_text(self):
        """ Test for Address Model Name Help Text """
        field_help_text = self.address._meta.get_field('name').help_text 
        self.assertEqual(field_help_text, 'Enter a nickname for this address')
        
# Create a TestCase for Address Required Fields
# crm_user.tests.models.test_AddressModel.ReqTests
class ReqTests(TestCase):
    """ Define a TestCase for Address Model Required Fields """
    @classmethod 
    def setUpTestData(cls):
        """ Define setUpTestData method for Address Model Required Fields """
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
        """ Define setUp method for Address Model Required Fields """
        self.address = Address.objects.get(id=1)
        self.user = User.objects.get(id=1)
        
    def test_id_required(self):
        """ Test that Address Model ID is Not Required """
        field_blank = self.address._meta.get_field('id').blank 
        field_null = self.address._meta.get_field('id').null 
        self.assertEqual(field_blank, True)
        self.assertEqual(field_null, False)
        
    def test_address_line2_required(self):
        """ Test that Address Model Address Line2 is Not Required """
        field_blank = self.address._meta.get_field('address_line2').blank 
        field_null = self.address._meta.get_field('address_line2').null 
        self.assertEqual(field_blank, True)
        self.assertEqual(field_null, True)
        
    def test_user_required(self):
        """ Test that Address Model User is Required """
        field_blank = self.address._meta.get_field('user').blank 
        field_null = self.address._meta.get_field('user').null 
        self.assertEqual(field_blank, False )
        self.assertEqual(field_null, False )

    def test_address_line1_required(self):
        """ Test that Address Model Address Line1 is Required """
        field_blank = self.address._meta.get_field('address_line1').blank 
        field_null = self.address._meta.get_field('address_line1').null 
        self.assertEqual(field_blank, False)
        self.assertEqual(field_null, False)
        
    def test_city_required(self):
        """ Test that Address Model City is Required """
        field_blank = self.address._meta.get_field('city').blank
        field_null = self.address._meta.get_field('city').null
        self.assertEqual(field_blank, False)
        self.assertEqual(field_null, False)
        
    def test_state_required(self):
        """ Test that Address Model State is Required """
        field_blank = self.address._meta.get_field('state').blank 
        field_null = self.address._meta.get_field('state').null 
        self.assertEqual(field_blank, False)
        self.assertEqual(field_null, False)
        
    def test_zip_required(self):
        """ Test that Address Model Zip is Required """
        field_blank = self.address._meta.get_field('zip').blank 
        field_null = self.address._meta.get_field('zip').null 
        self.assertEqual(field_blank, False)
        self.assertEqual(field_null, False)
        
    def test_type_required(self):
        """ Test that Address Model Type is Required """
        field_blank = self.address._meta.get_field('type').blank
        field_null = self.address._meta.get_field('type').null
        self.assertEqual(field_blank, False)
        self.assertEqual(field_null, False)
        
    def test_name_required(self):
        """ Test that Address Model Name is Required """
        field_blank = self.address._meta.get_field('name').blank 
        field_null = self.address._meta.get_field('name').null 
        self.assertEqual(field_blank, False)
        self.assertEqual(field_null, False)
        
# Create a TestCase for Address Defaults
# crm_user.tests.models.test_AddressModel.DefaultTests
class DefaultTests(TestCase):
    """ Define a TestCase for Address Model Defaults """
    @classmethod 
    def setUpTestData(cls):
        """ Define setUpTestData method for Address Model Defaults """
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
        """ Define setUp method for Address Model Defaults """
        self.address = Address.objects.get(id=1)
        self.user = User.objects.get(id=1)
        
    def test_id_default(self):
        """ Test that Address Model ID has no default value """
        field_default = self.address._meta.get_field('id').default 
        self.assertEqual(field_default, NOT_PROVIDED)
        
    def test_address_line2_default(self):
        """ Test that Address Model Address Line2 has no default value """
        field_default = self.address._meta.get_field('address_line2').default 
        self.assertEqual(field_default, NOT_PROVIDED)
        
    def test_user_default(self):
        """ Test that Address Model User has no default value """
        field_default = self.address._meta.get_field('user').default 
        self.assertEqual(field_default, NOT_PROVIDED )

    def test_address_line1_default(self):
        """ Test that Address Model Address Line1 has no default value """
        field_default = self.address._meta.get_field('address_line1').default 
        self.assertEqual(field_default, NOT_PROVIDED)
        
    def test_city_default(self):
        """ Test that Address Model City has no default value """
        field_default = self.address._meta.get_field('city').default
        self.assertEqual(field_default, NOT_PROVIDED)
        
    def test_state_default(self):
        """ Test that Address Model State has no default value """
        field_default = self.address._meta.get_field('state').default 
        self.assertEqual(field_default, NOT_PROVIDED)
        
    def test_zip_default(self):
        """ Test that Address Model Zip has no default value """
        field_default = self.address._meta.get_field('zip').default 
        self.assertEqual(field_default, NOT_PROVIDED)
        
    def test_type_default(self):
        """ Test that Address Model Type has default value """
        field_default = self.address._meta.get_field('type').default
        self.assertEqual(field_default, self.address.Type.RESIDENTIAL)
        
    def test_name_default(self):
        """ Test that Address Model Name has no default value """
        field_default = self.address._meta.get_field('name').default 
        self.assertEqual(field_default, NOT_PROVIDED)
        
# Create a TestCase for Address Choices Fields
# crm_user.tests.models.test_AddressModel.ChoicesTests
class ChoicesTests(TestCase):
    """ Define a TestCase for Address Model Choices Fields """
    @classmethod 
    def setUpTestData(cls):
        """ Define setUpTestData method for Address Model Choices Fields """
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
        """ Define setUp method for Address Model Choices Fields """
        self.address = Address.objects.get(id=1)
        self.user = User.objects.get(id=1)
        
    def test_id_choices(self):
        """ Test that Address Model ID has no choices value """
        field_choices = self.address._meta.get_field('id').choices 
        self.assertEqual(field_choices, None)
        
    def test_address_line2_choices(self):
        """ Test that Address Model Address Line2 has no choices value """
        field_choices = self.address._meta.get_field('address_line2').choices 
        self.assertEqual(field_choices, None)
        
    def test_user_choices(self):
        """ Test that Address Model User has no choices value """
        field_choices = self.address._meta.get_field('user').choices 
        self.assertEqual(field_choices, None )

    def test_address_line1_choices(self):
        """ Test that Address Model Address Line1 has no choices value """
        field_choices = self.address._meta.get_field('address_line1').choices 
        self.assertEqual(field_choices, None)
        
    def test_city_choices(self):
        """ Test that Address Model City has no choices value """
        field_choices = self.address._meta.get_field('city').choices
        self.assertEqual(field_choices, None)
        
    def test_state_choices(self):
        """ Test that Address Model State has no choices value """
        field_choices = self.address._meta.get_field('state').choices 
        self.assertEqual(field_choices, None)
        
    def test_zip_choices(self):
        """ Test that Address Model Zip has no choices value """
        field_choices = self.address._meta.get_field('zip').choices 
        self.assertEqual(field_choices, None)
        
    def test_type_choices(self):
        """ Test that Address Model Type has choices value """
        field_choices = self.address._meta.get_field('type').choices
        self.assertEqual(field_choices, self.address.Type.choices)
        
    def test_name_choices(self):
        """ Test that Address Model Name has no choices value """
        field_choices = self.address._meta.get_field('name').choices 
        self.assertEqual(field_choices, None)
        
# Create a TestCase for Address Foreign Key Fields
# crm_user.tests.models.test_AddressModel.ForeignKeyTests
class ForeignKeyTests(TestCase):
    """ Define a TestCase for Address Model Foreign Key Fields """
    @classmethod 
    def setUpTestData(cls):
        """ Define setUpTestData method for Address Model Foreign Key Fields """
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
        """ Define setUp method for Address Model Foreign Key Fields """
        self.address = Address.objects.get(id=1)
        self.user = User.objects.get(id=1)
        
    def test_user_foreign_key_related_name(self):
        """ Test that Address Model User has a related name value """
        self.assertIn(self.address, self.user.addresses.all())
        
    def test_user_foreign_key_on_delete(self):
        """ Test that Address Model user has on_delete models.CASCADE """
        address = Address.objects.get(id=1)
        user = User.objects.get(id=1)
        user.delete()
        self.assertEqual(Address.objects.filter(id=1).exists(), False)
        
# Create a TestCase for Address Methods
# crm_user.tests.models.test_AddressModel.MethodTests 
class MethodTests(TestCase):
    """ Define a TestCase for Address Model Methods """
    @classmethod 
    def setUpTestData(cls):
        """ Define setUpTestData method for Address Model Methods """
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
        """ Define setUp method for Address Model Methods """
        self.address = Address.objects.get(id=1)
        self.user = User.objects.get(id=1)
        
    def test_string_method(self):
        """ Test for Address Model String Method """
        expected_string = f"{self.address.user.first_name}'s {self.address.name} - {self.address.address_line1} {self.address.city}, {self.address.state}"
        self.assertEqual(str(self.address), expected_string)
        
# Create a TestCase for Address Meta
# crm_user.tests.models.test_AddressModel.MetaTests 
class MetaTests(TestCase):
    """ Define a TestCase for Address Model Meta """
    @classmethod 
    def setUpTestData(cls):
        """ Define setUpTestData method for Address Model Meta """
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
        
    def test_verbose_name(self):
        """ Test Address Model verbose name """
        address = Address.objects.get(id=1)
        self.assertEqual(address._meta.verbose_name, 'Address')
        
    def test_verbose_name_plural(self):
        """ Test Address Model verbose name plural """
        address = Address.objects.get(id=1)
        self.assertEqual(address._meta.verbose_name_plural, 'Addresses')
        
    def test_ordering(self):
        """ Test Address Model ordering """
        address = Address.objects.get(id=1)
        self.assertEqual(address._meta.ordering, ['user'])
        

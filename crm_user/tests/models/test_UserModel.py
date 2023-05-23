#./crm_user/tests/models/test_UserModel.py
#-------------------------------------------------------------
#-------------------------------------------------------------
# IMPORTS

from django.test import TestCase, override_settings
from crm_user.models import User
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
# Create your User Model tests here.

# Create a TestCase for User Labels
# crm_user.tests.models.test_UserModel.LabelTests
class LabelTests(TestCase):
    """ Define a TestCase for User Model Labels """
    @classmethod 
    def setUpTestData(cls):
        """ Define setUpTestData method for User Model Labels """
        User.objects.create_user(
            email="doe@example.com",
            first_name="Sara",
            middle_name="Lee",
            last_name="Doe",
            birth_date='1993-04-14',
            profile_photo=SimpleUploadedFile("test_image.jpg", b"test_content", "image/jpeg"),
            phone_number="+12125556789",
        )
        
    def setUp(self):
        """ Define setUp method for User Model Labels """
        self.user = User.objects.get(id=1)
        
    def test_id_label(self):
        """ Test for User Model ID Label """
        field_label = self.user._meta.get_field('id').verbose_name 
        self.assertEqual(field_label, 'ID')
        
    def test_type_label(self):
        """ Test for User Model Type Label """
        field_label = self.user._meta.get_field('type').verbose_name
        self.assertEqual(field_label, 'Type')
        
    def test_email_label(self):
        """ Test for User Model Email Label """
        field_label = self.user._meta.get_field('email').verbose_name 
        self.assertEqual(field_label, 'Email')
        
    def test_first_name_label(self):
        """ Test for User Model First Name Label """
        field_label = self.user._meta.get_field('first_name').verbose_name 
        self.assertEqual(field_label, 'First Name')

    def test_middle_name_label(self):
        """ Test for User Model Middle Name Label """
        field_label = self.user._meta.get_field('middle_name').verbose_name 
        self.assertEqual(field_label, 'Middle Name')
        
    def test_last_name_label(self):
        """ Test for User Model Last Name Label """
        field_label = self.user._meta.get_field('last_name').verbose_name
        self.assertEqual(field_label, 'Last Name')
        
    def test_birth_date_label(self):
        """ Test for User Model Birth Date Label """
        field_label = self.user._meta.get_field('birth_date').verbose_name 
        self.assertEqual(field_label, 'Birth Date')
        
    def test_profile_photo_label(self):
        """ Test for User Model Profile Photo Label """
        field_label = self.user._meta.get_field('profile_photo').verbose_name 
        self.assertEqual(field_label, 'Profile Photo')
        
    def test_phone_number_label(self):
        """ Test for User Model Phone Number Label """
        field_label = self.user._meta.get_field('phone_number').verbose_name 
        self.assertEqual(field_label, 'Phone Number')
        
    def test_last_modified_label(self):
        """ Test for User Model Last Modified Label """
        field_label = self.user._meta.get_field('last_modified').verbose_name 
        self.assertEqual(field_label, 'Last Modified')
        
    def test_last_modified_by_label(self):
        """ Test for User Model Last Modified By Label """
        field_label = self.user._meta.get_field('last_modified_by').verbose_name 
        self.assertEqual(field_label, 'Last Modified By')

# Create a TestCase for User Max Lengths
# crm_user.tests.models.test_UserModel.MaxLengthTests
class MaxLengthTests(TestCase):
    """ Define a TestCase for User Model Max Lengths """
    @classmethod 
    def setUpTestData(cls):
        """ Define setUpTestData method for User Model Max Lengths """
        User.objects.create_user(
            email="doe@example.com",
            first_name="Sara",
            middle_name="Lee",
            last_name="Doe",
            birth_date='1993-04-14',
            profile_photo=SimpleUploadedFile("test_image.jpg", b"test_content", "image/jpeg"),
            phone_number="+12125556789",
        )
        
    def setUp(self):
        """ Define setUp method for User Model Max Lengths """
        self.user = User.objects.get(id=1)
        
    def test_id_max_length(self):
        """ Test for User Model ID Max Length """
        field_max_length = self.user._meta.get_field('id').max_length 
        self.assertEqual(field_max_length, None)
        
    def test_type_max_length(self):
        """ Test for User Model Type Max Length """
        field_max_length = self.user._meta.get_field('type').max_length
        self.assertEqual(field_max_length, 8)
        
    def test_email_max_length(self):
        """ Test for User Model Email Max Length """
        field_max_length = self.user._meta.get_field('email').max_length 
        self.assertEqual(field_max_length, 254)
        
    def test_first_name_max_length(self):
        """ Test for User Model First name Max Length """
        field_max_length = self.user._meta.get_field('first_name').max_length
        self.assertEqual(field_max_length, 50)
        
    def test_middle_name_max_length(self):
        """ Test for User Model Middle Name Max Length """
        field_max_length = self.user._meta.get_field('middle_name').max_length 
        self.assertEqual(field_max_length, 50)
    
    def test_last_name_max_length(self):
        """ Test for User Model Last Name Max Length """
        field_max_length = self.user._meta.get_field('last_name').max_length 
        self.assertEqual(field_max_length, 50)
        
    def test_birth_date_max_length(self):
        """ Test for User Model Birth Date Max Length """
        field_max_length = self.user._meta.get_field('birth_date').max_length 
        self.assertEqual(field_max_length, None)
        
    def test_profile_photo_max_length(self):
        """ Test for User Model Profile Photo Max Length """
        field_max_length = self.user._meta.get_field('profile_photo').max_length 
        self.assertEqual(field_max_length, 100)
        
    def test_phone_number_max_length(self):
        """ Test for User Model Phone Number Max Length """
        field_max_length = self.user._meta.get_field('phone_number').max_length 
        self.assertEqual(field_max_length, 128)
        
    def test_last_modified_max_length(self):
        """ Test for User Model Last Modified Max Length """
        field_max_length = self.user._meta.get_field('last_modified').max_length
        self.assertEqual(field_max_length, None)
        
    def test_last_modified_by_max_length(self):
        """ Test for User Model Last Modified By Max Length """
        field_max_length = self.user._meta.get_field('last_modified_by').max_length 
        self.assertEqual(field_max_length, None)
        
# Create a TestCase for User Help Text
# crm_user.tests.models.test_UserModel.HelpTextTests
class HelpTextTests(TestCase):
    """ Define a TestCase for User Model Help Text """
    @classmethod 
    def setUpTestData(cls):
        """ Define setUpTestData method for User Model Help Text """
        User.objects.create_user(
            email="doe@example.com",
            first_name="Sara",
            middle_name="Lee",
            last_name="Doe",
            birth_date='1993-04-14',
            profile_photo=SimpleUploadedFile("test_image.jpg", b"test_content", "image/jpeg"),
            phone_number="+12125556789",
        )
        
    def setUp(self):
        """ Define setUp method for User Model Help Text """
        self.user = User.objects.get(id=1)
        
    def test_id_help_text(self):
        """ Test for User Model ID Help Text """
        help_text = self.user._meta.get_field('id').help_text 
        self.assertEqual(help_text, '')
        
    def test_type_help_text(self):
        """ Test for User Model Type Help Text """
        help_text = self.user._meta.get_field('type').help_text 
        self.assertEqual(help_text, 'Select the user type')

    def test_email_help_text(self):
        """ Test for User Model Email Help Text """
        help_text = self.user._meta.get_field('email').help_text 
        self.assertEqual(help_text, 'Enter your email address')
        
    def test_first_name_help_text(self):
        """ Test for User Model First Name Help Text """
        help_text = self.user._meta.get_field('first_name').help_text 
        self.assertEqual(help_text, 'Enter your first name')

    def test_middle_name_help_text(self):
        """ Test for User Model Middle Name Help Text """
        help_text = self.user._meta.get_field('middle_name').help_text 
        self.assertEqual(help_text, 'Enter your middle name')
        
    def test_last_name_help_text(self):
        """ Test for User Model Last Name Help Text """
        help_text = self.user._meta.get_field('last_name').help_text
        self.assertEqual(help_text, 'Enter your last name')
        
    def test_birth_date_help_text(self):
        """ Test for User Model Birth Date Help Text """
        help_text = self.user._meta.get_field('birth_date').help_text
        self.assertEqual(help_text, 'Enter your birth date as yyyy-mm-dd')

    def test_profile_photo_help_text(self):
        """ Test for User Model Profile Photo Help Text """
        help_text = self.user._meta.get_field('profile_photo').help_text 
        self.assertEqual(help_text, 'Upload a photo of yourself')
        
    def test_phone_number_help_text(self):
        """ Test for User Model Phone Number Help Text """
        help_text = self.user._meta.get_field('phone_number').help_text
        self.assertEqual(help_text, 'Enter a good contact phone number')
        
    def test_last_modified_help_text(self):
        """ Test for User Model Last Modified Help Text """
        help_text = self.user._meta.get_field('last_modified').help_text 
        self.assertEqual(help_text, 'The date and time of which the user was last modified.')
        
    def test_last_modified_by_help_text(self):
        """ Test for User Model Last Modified By Help Text """
        help_text = self.user._meta.get_field('last_modified_by').help_text
        self.assertEqual(help_text, 'The user who last modified this user.')
        
# Create a TestCase for User Required Fields
# crm_user.tests.models.test_UserModel.ReqTests
class ReqTests(TestCase):
    """ Define a TestCase for User Model Required Fields"""
    @classmethod 
    def setUpTestData(cls):
        """ Define setUpTestData method for User Model Required Fields """
        User.objects.create_user(
            email="doe@example.com",
            first_name="Sara",
            middle_name="Lee",
            last_name="Doe",
            birth_date='1993-04-14',
            profile_photo=SimpleUploadedFile("test_image.jpg", b"test_content", "image/jpeg"),
            phone_number="+12125556789",
        )
        
    def setUp(self):
        """ Define setUp method for User Model Required Fields """
        self.user = User.objects.get(id=1)
        
    def test_id_required(self):
        """ Test that User Model ID is not required """
        blank = self.user._meta.get_field('id').blank 
        null = self.user._meta.get_field('id').null
        self.assertEqual(blank, True)
        self.assertEqual(null, False)
        
    def test_type_required(self):
        """ Test that User Model Type is required """
        blank = self.user._meta.get_field('type').blank 
        null = self.user._meta.get_field('type').null
        self.assertEqual(blank, False)
        self.assertEqual(null, False)

    def test_email_required(self):
        """ Test that User Model Email is required """
        blank = self.user._meta.get_field('email').blank 
        null = self.user._meta.get_field('email').null 
        unique = self.user._meta.get_field('email').unique
        self.assertEqual(blank, False)
        self.assertEqual(null, False)
        self.assertEqual(unique, True)
        
    def test_first_name_required(self):
        """ Test that User Model First name is not required """
        blank = self.user._meta.get_field('first_name').blank 
        null = self.user._meta.get_field('first_name').null
        self.assertEqual(blank, True)
        self.assertEqual(null, True)
        
    def test_middle_name_required(self):
        """ Test that User Model Middle Name is not required """
        blank = self.user._meta.get_field('middle_name').blank
        null = self.user._meta.get_field('middle_name').null
        self.assertEqual(blank, True)
        self.assertEqual(null, True)
        
    def test_last_name_required(self):
        """ Test that User Model Last Name is not required """
        blank = self.user._meta.get_field('last_name').blank 
        null = self.user._meta.get_field('last_name').null 
        self.assertEqual(blank, True)
        self.assertEqual(null, True)
        
    def test_birth_date_required(self):
        """ Test that User Model Birth Date is not required """
        blank = self.user._meta.get_field('birth_date').blank
        null = self.user._meta.get_field('birth_date').null
        self.assertEqual(blank, True)
        self.assertEqual(null, True)
        
    def test_profile_photo_required(self):
        """ Test that User Model Profile Photo is not required """
        blank = self.user._meta.get_field('profile_photo').blank
        null = self.user._meta.get_field('profile_photo').null
        self.assertEqual(blank, True)
        self.assertEqual(null, True)
        
    def test_phone_number_required(self):
        """ Test that User Model Phone Number is not required """
        blank = self.user._meta.get_field('phone_number').blank
        null = self.user._meta.get_field('phone_number').null 
        self.assertEqual(blank, True)
        self.assertEqual(null, True)
        
    def test_last_modified_required(self):
        """ Test that User Model Last Modified is not required """
        blank = self.user._meta.get_field('last_modified').blank 
        null = self.user._meta.get_field('last_modified').null
        self.assertEqual(blank, True)
        self.assertEqual(null, True)
        
    def test_last_modified_by_required(self):
        """ Test that User Model Last Modified By is not required """
        blank = self.user._meta.get_field('last_modified_by').blank 
        null = self.user._meta.get_field('last_modified_by').null
        self.assertEqual(blank, True)
        self.assertEqual(null, True)
        
# Create a TestCase for User Defaults
# crm_user.tests.models.test_UserModel.DefaultTests
class DefaultTests(TestCase):
    """ Define a Testcase for User Model Defaults """
    @classmethod 
    def setUpTestData(cls):
        """ Define setUpTestData method for User Model Defaults """
        User.objects.create_user(
            email="doe@example.com",
            first_name="Sara",
            middle_name="Lee",
            last_name="Doe",
            birth_date='1993-04-14',
            profile_photo=SimpleUploadedFile("test_image.jpg", b"test_content", "image/jpeg"),
            phone_number="+12125556789",
        )
        
    def setUp(self):
        """ Define setUp method for User Model Defaults """
        self.user = User.objects.get(id=1)
        
    def test_id_default(self):
        """ Test that User Model ID has no default value """
        default = self.user._meta.get_field('id').default 
        self.assertEqual(default, NOT_PROVIDED)
        
    def test_type_default(self):
        """ Test that User Model Type has a default value """
        default = self.user._meta.get_field('type').default
        self.assertEqual(default, self.user.Types.CUSTOMER)

    def test_email_default(self):
        """ Test that User Model Email has no default value """
        default = self.user._meta.get_field('email').default 
        self.assertEqual(default, NOT_PROVIDED)
        
    def test_first_name_default(self):
        """ Test that User Model First Name has no default value """
        default = self.user._meta.get_field('first_name').default 
        self.assertEqual(default, NOT_PROVIDED)
        
    def test_middle_name_default(self):
        """ Test that User Model Middle Name has no default value """
        default = self.user._meta.get_field('middle_name').default 
        self.assertEqual(default, NOT_PROVIDED)
        
    def test_last_name_default(self):
        """ Test that User Model Last Name has no default value """
        default = self.user._meta.get_field('last_name').default 
        self.assertEqual(default, NOT_PROVIDED)
        
    def test_birth_date_default(self):
        """ Test that User Model Birth Date has no default value """
        default = self.user._meta.get_field('birth_date').default 
        self.assertEqual(default, NOT_PROVIDED)
        
    def test_profile_photo_default(self):
        """ Test that User Model profile_photo has no default value """
        default = self.user._meta.get_field('profile_photo').default 
        self.assertEqual(default, NOT_PROVIDED)
        
    def test_phone_number_default(self):
        """ Test that User Model Phone Number has no default value """
        default = self.user._meta.get_field('phone_number').default 
        self.assertEqual(default, NOT_PROVIDED)
        
    def test_last_modified_default(self):
        """ Test that User Model Last Modified has no default value """
        default = self.user._meta.get_field('last_modified').default 
        self.assertEqual(default, NOT_PROVIDED)
        
    def test_last_modified_by_default(self):
        """ Test that User Model Last Modified By has no default value """
        default = self.user._meta.get_field('last_modified_by').default 
        self.assertEqual(default, NOT_PROVIDED)
        
# Create a TestCase for User Choices Fields
# crm_user.tests.models.test_UserModel.ChoicesTests
class ChoicesTests(TestCase):
    """ Define a Testcase for User Model Choices """
    @classmethod 
    def setUpTestData(cls):
        """ Define setUpTestData method for User Model Choices """
        User.objects.create_user(
            email="doe@example.com",
            first_name="Sara",
            middle_name="Lee",
            last_name="Doe",
            birth_date='1993-04-14',
            profile_photo=SimpleUploadedFile("test_image.jpg", b"test_content", "image/jpeg"),
            phone_number="+12125556789",
        )
        
    def setUp(self):
        """ Define setUp method for User Model Choices """
        self.user = User.objects.get(id=1)
        
    def test_id_choices(self):
        """ Test that User Model ID has no choices value """
        choices = self.user._meta.get_field('id').choices 
        self.assertEqual(choices, None)
        
    def test_type_choices(self):
        """ Test that User Model Type has a choices value """
        choices = self.user._meta.get_field('type').choices
        self.assertEqual(choices, self.user.Types.choices)

    def test_email_choices(self):
        """ Test that User Model Email has no choices value """
        choices = self.user._meta.get_field('email').choices 
        self.assertEqual(choices, None)
        
    def test_first_name_choices(self):
        """ Test that User Model First Name has no choices value """
        choices = self.user._meta.get_field('first_name').choices 
        self.assertEqual(choices, None)
        
    def test_middle_name_choices(self):
        """ Test that User Model Middle Name has no choices value """
        choices = self.user._meta.get_field('middle_name').choices 
        self.assertEqual(choices, None)
        
    def test_last_name_choices(self):
        """ Test that User Model Last Name has no choices value """
        choices = self.user._meta.get_field('last_name').choices 
        self.assertEqual(choices, None)
        
    def test_birth_date_choices(self):
        """ Test that User Model Birth Date has no choices value """
        choices = self.user._meta.get_field('birth_date').choices 
        self.assertEqual(choices, None)
        
    def test_profile_photo_choices(self):
        """ Test that User Model profile_photo has no choices value """
        choices = self.user._meta.get_field('profile_photo').choices 
        self.assertEqual(choices, None)
        
    def test_phone_number_choices(self):
        """ Test that User Model Phone Number has no choices value """
        choices = self.user._meta.get_field('phone_number').choices 
        self.assertEqual(choices, None)
        
    def test_last_modified_choices(self):
        """ Test that User Model Last Modified has no choices value """
        choices = self.user._meta.get_field('last_modified').choices 
        self.assertEqual(choices, None)
        
    def test_last_modified_by_choices(self):
        """ Test that User Model Last Modified By has no choices value """
        choices = self.user._meta.get_field('last_modified_by').choices 
        self.assertEqual(choices, None)
        
# Create a TestCase for User Foreign Key Fields
# crm_user.tests.models.test_UserModel.ForeignKeyTests
class ForeignKeyTests(TestCase):
    """ Define a TestCase for User Model Foreign Key Fields """
    @classmethod 
    def setUpTestData(cls):
        """ Define setUpTestData method for User Model Foreign Key Fields """
        User.objects.create_user(
            email="doe@example.com",
            first_name="Sara",
            middle_name="Lee",
            last_name="Doe",
            birth_date='1993-04-14',
            profile_photo=SimpleUploadedFile("test_image.jpg", b"test_content", "image/jpeg"),
            phone_number="+12125556789",
        )
        
    def setUp(self):
        """ Define setUp method for User Model Foreign Key Fields """
        self.user = User.objects.get(id=1)
        
    def test_type_foreign_key_related_name(self):
        """ Test that User Model Type has a related name value """
        self.assertIn(self.user, self.user.modified_by.all())
        
    def test_type_foreign_key_on_delete(self):
        """ Test that User Model Type has on_delete models.SET_NULL """
        user1 = User.objects.get(id=1)
        user2 = User.objects.create_user(email='test@example.com')
        user1.last_modified_by = user2 
        user1.save()
        self.assertEqual(user1.last_modified_by, user2)
        user2.delete()
        user1 = User.objects.get(id=1)
        self.assertEqual(User.objects.filter(id=1).exists(), True)
        self.assertEqual(User.objects.filter(id=2).exists(), False)
        self.assertEqual(user1.last_modified_by, None)
 
# Create a TestCase for User Image Fields
# crm_user.tests.models.tests_UserModel.ImageTests 
@override_settings(MEDIA_ROOT=MEDIA_ROOT)
class ImageTests(TestCase):
    """ Define a TestCase for User Model Image Fields """
    @classmethod 
    def setUpTestData(cls):
        """ Define setUpTestData method for User Model Image Fields """
        User.objects.create_user(
            email="doe@example.com",
            first_name="Sara",
            middle_name="Lee",
            last_name="Doe",
            birth_date='1993-04-14',
            profile_photo=SimpleUploadedFile("test_image.jpg", b"test_content", "image/jpeg"),
            phone_number="+12125556789",
        )
        
    def setUp(self):
        """ Define setUp method for User Model Image Fields """
        self.user = User.objects.get(id=1)
        
    @classmethod 
    def tearDownClass(cls):
        shutil.rmtree(MEDIA_ROOT, ignore_errors=True)
        super().tearDownClass()

    def test_profile_photo_url(self):
        """ Test that User Model Profile Photo URL is correctly configured """
        self.assertEqual(self.user.profile_photo.name, 'profile_images/test_image.jpg')
        
# Create a TestCase for User Methods
# crm_user.tests.models.test_UserModel.MethodTests 
class MethodTests(TestCase):
    """ Define a TestCase for User Model Methods """
    @classmethod 
    def setUpTestData(cls):
        """ Define setUpTestData method for User Model Methods """
        User.objects.create_user(
            email="doe@example.com",
            first_name="Sara",
            middle_name="Lee",
            last_name="Doe",
            birth_date='1993-04-14',
            profile_photo=SimpleUploadedFile("test_image.jpg", b"test_content", "image/jpeg"),
            phone_number="+12125556789",
        )
        
    def setUp(self):
        """ Define setUp method for User Model Methods """
        self.user = User.objects.get(id=1)
        
    def test_age_method(self):
        """ Test for User Model Age Method """
        user = User.objects.get(id=1)
        self.assertEqual(user.age(), 30)
        
    @freeze_time(timezone.now())
    def test_save_method_last_modified(self):
        """ Test that User Model Save Method updates last_modified field"""
        user = User.objects.get(id=1)
        self.assertNotEqual(user.last_modified, timezone.now())
        user.first_name = 'John'
        user.save()
        self.assertEqual(user.last_modified, timezone.now())
        
    def test_full_name_method(self):
        """ Test for User Model Full Name Method """
        full_name = f'{self.user.first_name} {self.user.last_name}'
        self.assertEqual(self.user.full_name(), full_name)
        
    def test_string_method(self):
        """ Test for User Model String Method """
        string = f'{self.user.last_name}, {self.user.first_name}'
        self.assertEqual(str(self.user), string)
            
# Create a TestCase for User Meta
# crm_user.tests.models.test_UserModel.MetaTests 
class MetaTests(TestCase):
    """ Define a TestCase for User Model Meta """
    @classmethod 
    def setUpTestData(cls):
        """ Define setUpTestData method for User Model Meta """
        User.objects.create_user(
            email="doe@example.com",
            first_name="Sara",
            middle_name="Lee",
            last_name="Doe",
            birth_date='1993-04-14',
            profile_photo=SimpleUploadedFile("test_image.jpg", b"test_content", "image/jpeg"),
            phone_number="+12125556789",
        )
        
    def setUp(self):
        """ Define setUp method for User Model Meta """
        self.user = User.objects.get(id=1)
        
    def test_ordering(self):
        """ Test User Model Ordering """
        self.assertEqual(self.user._meta.ordering, ['last_name', 'first_name'])

    def test_verbose_name(self):
        """ Test User Model Verbose Name """
        self.assertEqual(self.user._meta.verbose_name, 'User')
        
    def test_verbose_name_plural(self):
        """ Test User Model Verbose Name Plural """
        self.assertEqual(self.user._meta.verbose_name_plural, 'Users')
        
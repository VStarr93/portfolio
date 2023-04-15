from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db.models.signals import post_save 
from django.dispatch import receiver 
from django.utils import timezone 
from phonenumber_field.modelfields import PhoneNumberField 
from django.urls import reverse 
from django.utils.translation import gettext_lazy as _ 

# Create your models here.

# Create UserManager from BaseUserManager
class UserManager(BaseUserManager):
    """Define a model manager for User model with no username field."""

    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """Create and save a User with the given email and password."""
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        """Create and save a regular User with the given email and no password."""
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        """Create and save a SuperUser with the given email and password."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)  
    
# Create User from AbstractUser
class User(AbstractUser):
    
    username = None
    # Required Fields
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    
    objects = UserManager()
    
    def get_absolute_url(self):
        return reverse("users:detail", kwargs={"username": self.username})
    
    # Custom Fields
    class Types(models.TextChoices):
        CUSTOMER = "CUSTOMER", "Customer"
        EMPLOYEE = "EMPLOYEE", "Employee"
        ADMIN = "ADMIN", "Admin"
    
    type = models.CharField(_('type'), max_length=50, choices=Types.choices, default=Types.CUSTOMER, help_text="Please select the user type")
    
    email = models.EmailField(_('email address'), unique=True, help_text="Please enter your email address")
    middle_name = models.CharField(_('middle name'), max_length=50, blank=True, help_text="Please enter your middle name")
    birth_date = models.DateField(_('birth date'), null=True, blank=True, help_text="Please enter your birth date")
    profile_photo = models.ImageField(_('profile photo'), upload_to='profile_images/', blank=True, help_text="Upload a photo of yourself")
    phone_number = PhoneNumberField(_('phone number'), blank=True, help_text="Enter a good contact phone number")
    
    # First Name and Last Name Do Not Cover Name Patterns
    # Around the Globe.
    name = models.CharField(_('Name of User'), blank=True, max_length=255, help_text="Please enter your full name")

# Create Customer Manager
class CustomerManager(UserManager):
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(type=User.Types.CUSTOMER)

# Create Employee Manager
class EmployeeManager(UserManager):
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(type=User.Types.EMPLOYEE)
    
# Create Admin Manager
class AdminManager(UserManager):
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(type=User.Types.ADMIN)
        
# Add Customer Model
class Customer(User):

    # Define objects model
    objects = CustomerManager()

    # Customize save method to automatically add user type
    def save(self, *args, **kwargs):
        if not self.pk:
            self.type = User.Types.CUSTOMER
        return super().save(*args, **kwargs)
    
    # Customize string method to display user name
    def __str__(self):
        return self.first_name + ' ' + self.last_name
        
# Add Employee Model
class Employee(User):
    objects = EmployeeManager()
    username = None
    
    def save(self, *args, **kwargs):
        if not self.pk:
            self.type = User.Types.EMPLOYEE
        return super().save(*args, **kwargs)
    
    def __str__(self):
        return self.first_name + ' ' + self.last_name
         
# Add Admin Model
class Admin(User):
    objects = AdminManager()
    username = None
    
    def save(self, *args, **kwargs):
        if not self.pk:
            self.type = User.Types.ADMIN
        return super().save(*args, **kwargs)
    
    def __str__(self):
        return self.first_name + ' ' + self.last_name
 
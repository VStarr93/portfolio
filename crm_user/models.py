#./crm_user/models.py
#-------------------------------------------------------------
#-------------------------------------------------------------
# IMPORTS

from django.db import models
from django.db.models import Model, TextChoices
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db.models.signals import post_save 
from django.dispatch import receiver 
from django.utils import timezone 
from phonenumber_field.modelfields import PhoneNumberField 
from django.urls import reverse 
from django.utils.translation import gettext_lazy as _ 

from django.core.mail import send_mail, EmailMessage, EmailMultiAlternatives 
from django.conf import settings 
from django.template.loader import render_to_string 
import datetime 

#-------------------------------------------------------------
#-------------------------------------------------------------
# Create your ModelManagers here.


# Create UserManager from BaseUserManager
class UserManager(BaseUserManager):
    """Define a model manager for User model with no username field."""

    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """Create and save a User with the given email and password."""
        if not email:
            raise ValueError('You must provide an email address for user.')

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.clean_fields()
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        """Create and save a regular User with the given email and no password."""
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        if password is None:
            password = User.objects.make_random_password(length=10, allowed_chars='abcdefghjkmnpqrstuvwxyzABCDEFGHJKLMNPQRSTUVWXYZ23456789')
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

# Create Customer Manager
class CustomerManager(UserManager):
    """
        Define a model manager for Customer model.
    """
    def get_queryset(self, *args, **kwargs):
        """
            Return users filtered by Types.CUSTOMER
        """
        return super().get_queryset(*args, **kwargs).filter(type=User.Types.CUSTOMER)

# Create Employee Manager
class EmployeeManager(UserManager):
    """
        Define a model manager for Employee model.
    """
    def get_queryset(self, *args, **kwargs):
        """
            Return users filtered by Types.EMPLOYEE
        """
        return super().get_queryset(*args, **kwargs).filter(type=User.Types.EMPLOYEE)
    
# Create Admin Manager
class AdminManager(UserManager):
    """
        Define a model manager for Admin model.
    """
    def get_queryset(self, *args, **kwargs):
        """
            Return users filtered by Types.ADMIN
        """
        return super().get_queryset(*args, **kwargs).filter(type=User.Types.ADMIN)


#-------------------------------------------------------------
#-------------------------------------------------------------
# Create your models here.
     
    
# Create User from AbstractUser
# django.contrib.auth.models.User
class User(AbstractUser):
    """
        Define custom User model based off AbstractUser.
    """
    
    # Required Fields
    username = None
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    
    # Specify custom model manager
    objects = UserManager()
    
    # list model methods
    def age(self):
        """
            Define method to calculate user's age from birth date
        """
        today = datetime.date.today()
        born = self.birth_date
        return today.year - born.year - ((today.month, today.day) < (born.month, born.day))
    
    def save(self, *args, **kwargs):
        """
            Define custom Save method.
        """
        self.clean_fields()
        return super().save(*args, **kwargs)
    
    def full_name(self):
        """
            Define method to display first and last name
        """
        return self.first_name + ' ' + self.last_name 

    def __str__(self):
        """String for representing the User object (in Admin site etc.)."""
        return self.last_name + ', ' + self.first_name
    
    # list model subclasses
    class Types(models.TextChoices):
        """
            Define text choices for user types.
        """
        CUSTOMER = "CUSTOMER", "Customer"
        EMPLOYEE = "EMPLOYEE", "Employee"
        ADMIN = "ADMIN", "Admin"
    
    # list model fields
    type = models.CharField(_('Type'), max_length=50, choices=Types.choices, default=Types.CUSTOMER, help_text="Select the user type")
    email = models.EmailField(_('Email'), unique=True, help_text="Enter your email address")
    first_name = models.CharField(_('First Name'), max_length=50, blank=True, help_text="Enter your first name")
    middle_name = models.CharField(_('Middle Name'), max_length=50, blank=True, help_text="Enter your middle name")
    last_name = models.CharField(_('Last Name'), max_length=50, blank=True, help_text="Enter your last name")
    birth_date = models.DateField(_('Birth Date'), null=True, blank=True, help_text="Enter your birth date as yyyy-MM-dd")
    profile_photo = models.ImageField(_('Profile Photo'), upload_to='profile_images/', blank=True, help_text="Upload a photo of yourself")
    phone_number = PhoneNumberField(_('Phone Number'), blank=True, help_text="Enter a good contact phone number")
    
# Add Customer Model - PROXY
# crm_user.models.Customer
class Customer(User):
    """
        Define Customer model based off User model.
    """

    # Define custom model manager
    objects = CustomerManager()

    # List model methods
    def welcome(self, *args, **kwargs):
        """
            Define method to send welcome email upon creation of new Customer.
        """
        customer = self 

        context={
            'Customer' : self,

        }
        subject = render_to_string('crm_user/email/customers/welcome_subject.txt', context).strip()
        text_message = render_to_string('crm_user/email/customers/welcome_body.txt', context)
        html_message = render_to_string('crm_user/email/customers/welcome_body.html', context)
        email = EmailMultiAlternatives(
            subject=subject,
            body=text_message, 
            from_email=settings.EMAIL_HOST_USER,
            to = [settings.RECIPIENT_ADDRESS],
        )
        email.attach_alternative(html_message, 'text/html')
        email.send()
    
    def save(self, *args, **kwargs):
        """
            Define custom Save method.
        """
        # Creating a new user
        if not self.pk:
            # Add default Type for Customer
            self.type = User.Types.CUSTOMER
            # Send Welcome Email to New Customer
            self.welcome()

        return super().save(*args, **kwargs)
    
    def __str__(self):
        """
            Define custom String method.
        """
        return self.first_name + ' ' + self.last_name
        
    # List model subclasses
    class Meta:
        proxy = True

# Add Employee Model - PROXY
# crm_user.models.Employee
class Employee(User):
    """
        Define Employee model based off User model.
    """

    # Define custom model manager
    objects = EmployeeManager()

    # List model methods    
    def welcome(self, *args, **kwargs):
        """
            Define method to send welcome email upon creation of new Employee.
        """
        employee = self 

        context={
            'Employee' : self,

        }
        subject = render_to_string('crm_user/email/employees/welcome_subject.txt', context).strip()
        text_message = render_to_string('crm_user/email/employees/welcome_body.txt', context)
        html_message = render_to_string('crm_user/email/employees/welcome_body.html', context)
        email = EmailMultiAlternatives(
            subject=subject,
            body=text_message, 
            from_email=settings.EMAIL_HOST_USER,
            to = [settings.RECIPIENT_ADDRESS],
        )
        email.attach_alternative(html_message, 'text/html')
        email.send()
    
    def save(self, *args, **kwargs):
        """
            Define custom Save method.
        """
        # Creating a new user
        if not self.pk:
            # Add default Type for Employee
            self.type = User.Types.EMPLOYEE
            # Send Welcome email to new Employee
            self.welcome()

        return super().save(*args, **kwargs)
    
    def __str__(self):
        """
            Define custom String method.
        """
        return self.first_name + ' ' + self.last_name
         
    # List model subclasses
    class Meta:
        proxy = True
        
# Add Admin Model - PROXY
# crm_user.models.Admin
class Admin(User):
    """
        Define Admin model based off User Model.
    """

    # Define custom model manager
    objects = AdminManager()
    
    # List model methods
    def welcome(self, *args, **kwargs):
        """
            Define method to send welcome email upon creation of new Admin.
        """
        admin = self 

        context={
            'Admin' : self,

        }
        subject = render_to_string('crm_user/email/admins/welcome_subject.txt', context).strip()
        text_message = render_to_string('crm_user/email/admins/welcome_body.txt', context)
        html_message = render_to_string('crm_user/email/admins/welcome_body.html', context)
        email = EmailMultiAlternatives(
            subject=subject,
            body=text_message, 
            from_email=settings.EMAIL_HOST_USER,
            to = [settings.RECIPIENT_ADDRESS],
        )
        email.attach_alternative(html_message, 'text/html')
        email.send()
    
    def save(self, *args, **kwargs):
        """
            Define custom Save method.
        """
        # Creating a new user
        if not self.pk:
            # Add default Type for Admin
            self.type = User.Types.ADMIN
            # Send Welcome email to new Admin
            self.welcome()
        return super().save(*args, **kwargs)
    
    def __str__(self):
        """
            Define custom String method.
        """
        return self.first_name + ' ' + self.last_name
 
    # List model subclasses
    class Meta:
        proxy = True

# Add Customer Profile Model
# crm_user.models.CustomerProfile
class CustomerProfile(Model):
    """
        Define a profile model for Users with type = Customer
    """

    # Define model methods
    def account_number():
        """
            Define method to calculate customer account number
        """
        # Define last customer
        last_customer = CustomerProfile.objects.all().order_by('pk').last()
        if not last_customer:
            return 'ACCT000001'
        # Define account number from last customer
        last_acct_no = last_customer.acct_no
        # if you want letters infront of invoice number
        # split account number from string and return integers (last index)
        account_int = int(last_acct_no.split('ACCT')[-1])
        # if you want only integers
        # invoice_int = int(invoice_no)
        # if you want to add x amount of 0's
        width = 6
        new_account_int = account_int + 1
        formatted = (width - len(str(new_account_int))) * "0" + str(new_account_int)
        new_account_no = 'ACCT' + str(formatted)
        return new_account_no
    
    def __str__(self):
        return self.user.first_name + " " + self.user.last_name
    # Define model subclasses
    class Status(TextChoices):
        """
            Define TextChoices for customer status.
            Customer status represents the frequncy of customer orders,
            whether they are:
            NEW (only 1 job), 
            RECURRING (more than 1 job),
            POTENTIAL (no jobs, but contact information is stored),
            OLD (has not had a job over 1 year)
        """
        NEW = 'NEW', 'New'
        RECURRING = 'RECURRING', 'Recurring'
        POTENTIAL = 'POTENTIAL', 'Potential'
        OLD = 'OLD', 'Old'
    
    class Language(TextChoices):
        """
            Define TextChoices for customer's primary language
        """
        ENGLISH = 'ENGLISH', 'English'
        SPANISH = 'SPANISH', 'Spanish'
        MANDARIN = 'MANDARIN', 'Mandarin'
        HINDI = 'HINDI', 'Hindi'
        FRENCH = 'FRENCH', 'French'
        ARABIC = 'ARABIC', 'Arabic'
        RUSSIAN = 'RUSSIAN', 'Russian'
        PORTUGUESE = 'PORTUGUESE', 'Portuguese'

    class Colors(TextChoices):
        """
            Define TextChoices for customer's selected theme
        """
        RED = 'RED', 'Red'
        BLUE = 'BLUE', 'Blue'
        GREEN = 'GREEN', 'Green'
        YELLOW = 'YELLOW', 'Yellow'
        ORANGE = 'ORANGE', 'Orange'
        PURPLE = 'PURPLE', 'Purple'
        BLACK = 'BLACK', 'Black'
        WHITE = 'WHITE', 'White'

    # Define AUTO-GENERATED model fields
    id = models.BigAutoField(primary_key=True) # Primary Key
    acct_no = models.CharField(_('Account Number'), max_length=10, unique=True, default=account_number, help_text="Your customer account number is auto-generated and cannot be changed.")
    status = models.CharField(_('Status'), max_length=9, default=Status.NEW, choices=Status.choices, help_text="Your customer status is adjusted based on frequency of jobs.")
    user = models.OneToOneField(Customer, on_delete=models.CASCADE, related_name='profile', verbose_name="Customer", unique=True, help_text="The Customer these details/model are associated with.")
    last_job = models.DateField(_('Last Job'), blank=True, null=True, help_text="The date of which the last job for customer was performed.")
    last_modified = models.DateTimeField(_('Last Modified'), auto_now=True, blank=True, null=True, help_text="The date and time of which the customer profile was last modified.")
    last_modified_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='profile_modified_by', verbose_name="Last Modified By", blank=True, null=True, help_text="The user who last modified this profile.")

    # Define BOOLEAN model fields
    balance_owed = models.BooleanField(_("Balance Owed"), default=False, help_text="The status of the customer's account balance.")
    credit_owed = models.BooleanField(_("Credit Owed"), default=False, help_text="The status of the customer's account credit.")

    # Define OPTIONAL model fields
    language = models.CharField(_("Language"), max_length=10, default=Language.ENGLISH, choices=Language.choices, help_text="What language do you speak?")
    theme = models.CharField(_("Theme"), max_length=6, default=Colors.GREEN, choices=Colors.choices, help_text="Choose a theme to use.")
  
# Add Employee Profile Model
# crm_user.models.EmployeeProfile
class EmployeeProfile(Model):
    """
        Define a profile model for Users with type = Employee
    """

    # Define model methods
    def calc_work_id():
        """
            Define method to calculate employee work id
        """
        # Define last customer
        last_employee = EmployeeProfile.objects.all().order_by('pk').last()
        if not last_employee:
            return 10001
        # Define work id from last employee
        last_id_no = last_employee.work_id
        # Increment last work id by 1
        new_work_id = last_id_no + 1
        # Return new work id
        return new_work_id
        
    def __str__(self):
        return self.user.first_name + " " + self.user.last_name
    # Define model subclasses
    class Status(TextChoices):
        """
            Define TextChoices for employee status.
        """
        ACTIVE = 'ACTIVE', 'Active'
        SUSPENDED = 'SUSPENDED', 'Suspended'
        TERMINATED = 'TERMINATED', 'Terminated'
        LEAVE = 'LEAVE', 'Leave'
        TRAINING = 'TRAINING', 'Training'
    
    class Language(TextChoices):
        """
            Define TextChoices for employee primary language
        """
        ENGLISH = 'ENGLISH', 'English'
        SPANISH = 'SPANISH', 'Spanish'
        MANDARIN = 'MANDARIN', 'Mandarin'
        HINDI = 'HINDI', 'Hindi'
        FRENCH = 'FRENCH', 'French'
        ARABIC = 'ARABIC', 'Arabic'
        RUSSIAN = 'RUSSIAN', 'Russian'
        PORTUGUESE = 'PORTUGUESE', 'Portuguese'

    class Colors(TextChoices):
        """
            Define TextChoices for employee selected theme.
        """
        RED = 'RED', 'Red'
        BLUE = 'BLUE', 'Blue'
        GREEN = 'GREEN', 'Green'
        YELLOW = 'YELLOW', 'Yellow'
        ORANGE = 'ORANGE', 'Orange'
        PURPLE = 'PURPLE', 'Purple'
        BLACK = 'BLACK', 'Black'
        WHITE = 'WHITE', 'White'

    # Define AUTO-GENERATED model fields
    id = models.BigAutoField(primary_key=True) # Primary Key
    work_id = models.IntegerField(_('Work ID'), unique=True, default=calc_work_id, help_text="Your employee work ID is auto-generated and cannot be changed.")
    status = models.CharField(_('Status'), max_length=10, default=Status.TRAINING, choices=Status.choices, help_text="Your employee status is adjusted based on employment status.")
    user = models.OneToOneField(Employee, on_delete=models.CASCADE, related_name='emp_profile', verbose_name="Employee", unique=True, help_text="The Employee these details/model are associated with.")
    last_modified = models.DateTimeField(_('Last Modified'), auto_now=True, blank=True, null=True, help_text="The date and time of which the employee profile was last modified.")
    last_modified_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='emp_profile_modified_by', verbose_name="Last Modified By", blank=True, null=True, help_text="The user who last modified this profile.")

    # Define BOOLEAN model fields
    is_manager = models.BooleanField(_("Is Manager"), default=False, help_text="Is this employee a manager?")

    # Define OPTIONAL model fields
    language = models.CharField(_("Language"), max_length=10, default=Language.ENGLISH, choices=Language.choices, help_text="What language do you speak?")
    theme = models.CharField(_("Theme"), max_length=6, default=Colors.GREEN, choices=Colors.choices, help_text="Choose a theme to use.")
    hire_date = models.DateField(_('Hire Date'), blank=True, null=True, help_text="The employee's hire date.") 

# Add Admin Profile Model
# crm_user.models.AdminProfile
class AdminProfile(Model):
    """
        Define a profile model for Users with type = Admin
    """

    # Define model methods
    def calc_work_id():
        """
            Define method to calculate admin work id
        """
        # Define last customer
        last_admin = AdminProfile.objects.all().order_by('pk').last()
        if not last_admin:
            return 500001
        # Define work id from last employee
        last_id_no = last_admin.work_id
        # Increment last work id by 1
        new_work_id = last_id_no + 1
        # Return new work id
        return new_work_id
       
    def __str__(self):
        return self.user.first_name + ' ' + self.user.last_name
    # Define model subclasses
    class Status(TextChoices):
        """
            Define TextChoices for admin status.
        """
        ACTIVE = 'ACTIVE', 'Active'
        SUSPENDED = 'SUSPENDED', 'Suspended'
        TERMINATED = 'TERMINATED', 'Terminated'
        LEAVE = 'LEAVE', 'Leave'
        TRAINING = 'TRAINING', 'Training'
    
    class Language(TextChoices):
        """
            Define TextChoices for admin primary language
        """
        ENGLISH = 'ENGLISH', 'English'
        SPANISH = 'SPANISH', 'Spanish'
        MANDARIN = 'MANDARIN', 'Mandarin'
        HINDI = 'HINDI', 'Hindi'
        FRENCH = 'FRENCH', 'French'
        ARABIC = 'ARABIC', 'Arabic'
        RUSSIAN = 'RUSSIAN', 'Russian'
        PORTUGUESE = 'PORTUGUESE', 'Portuguese'

    class Colors(TextChoices):
        """
            Define TextChoices for admin selected theme.
        """
        RED = 'RED', 'Red'
        BLUE = 'BLUE', 'Blue'
        GREEN = 'GREEN', 'Green'
        YELLOW = 'YELLOW', 'Yellow'
        ORANGE = 'ORANGE', 'Orange'
        PURPLE = 'PURPLE', 'Purple'
        BLACK = 'BLACK', 'Black'
        WHITE = 'WHITE', 'White'

    # Define AUTO-GENERATED model fields
    id = models.BigAutoField(primary_key=True) # Primary Key
    work_id = models.IntegerField(_('Work ID'), unique=True, default=calc_work_id, help_text="Your admin work ID is auto-generated and cannot be changed.")
    status = models.CharField(_('Status'), max_length=10, default=Status.TRAINING, choices=Status.choices, help_text="Your admin status is adjusted based on employment status.")
    user = models.OneToOneField(Admin, on_delete=models.CASCADE, related_name='admin_profile', verbose_name="Admin", unique=True, help_text="The Admin these details/model are associated with.")
    last_modified = models.DateTimeField(_('Last Modified'), auto_now=True, blank=True, null=True, help_text="The date and time of which the admin profile was last modified.")
    last_modified_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='admin_profile_modified_by', verbose_name="Last Modified By", blank=True, null=True, help_text="The user who last modified this profile.")

    # Define BOOLEAN model fields
    is_manager = models.BooleanField(_("Is Manager"), default=False, help_text="Is this admin a manager?")

    # Define OPTIONAL model fields
    language = models.CharField(_("Language"), max_length=10, default=Language.ENGLISH, choices=Language.choices, help_text="What language do you speak?")
    theme = models.CharField(_("Theme"), max_length=6, default=Colors.GREEN, choices=Colors.choices, help_text="Choose a theme to use.")
    
# Add Address Model
# crm_user.models.Address 
class Address(Model):
    """ Define an Address model for users """
    
    # Define model methods
    def __str__(self):
        return self.name + ' - ' + self.address_line1 + ' ' + self.city + ', ' + self.state
    
    def save(self, *args, **kwargs):
        if 'request' in kwargs:
            request = kwargs.get('request')
            self.last_modified_by = request.user
        else:
            self.last_modified_by = self.user
        return super().save(*args, **kwargs)   
    # Define model subclasses
    class Type(TextChoices):
        """
            Define TextChoices for address types.
        """
        RESIDENTIAL = 'RESIDENTIAL', 'Home'
        COMMERCIAL = 'COMMERCIAL', 'Commercial'
        INDUSTRIAL = 'INDUSTRIAL', 'Industrial'
    
    # Define Auto-Generated model fields
    id = models.BigAutoField(primary_key=True) # Primary Key
    last_modified = models.DateTimeField(_('Last Modified'), auto_now=True, blank=True, null=True, help_text="The date and time of which the address was last modified.")
    last_modified_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='address_modified_by', verbose_name="Last Modified By", blank=True, null=True, help_text="The user who last modified this address.")

    # Define Boolean model fields

    # Define Optional model fields
    address_line2 = models.CharField(_('Address Line 2'), max_length=254, blank=True, null=True, help_text="Enter the apartment or suite number" )
    
    # Define Required model fields
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='addresses', verbose_name="User", help_text="The user who lives at this address")
    address_line1 = models.CharField(_('Address Line 1'), max_length=254, help_text="Enter the street number and street name" )
    city = models.CharField(_('City'), max_length=254, help_text="Enter the city")
    state = models.CharField(_('State'), max_length=2, help_text="Enter the state as a 2 letter initial")
    zip = models.IntegerField(_('Zip'), help_text="Enter the zip code")
    type = models.CharField(_('Type'), max_length=11, default=Type.RESIDENTIAL, choices=Type.choices, help_text="Select the correct address type")
    name = models.CharField(_('Name'), max_length=100, help_text="Enter a nickname for this address")
    
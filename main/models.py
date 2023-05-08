#./main/models.py
#-------------------------------------------------------------
#-------------------------------------------------------------
# IMPORTS

from django.db import models
from django.db.models import Model, TextChoices
from django.utils import timezone 
from phonenumber_field.modelfields import PhoneNumberField 
from django.utils.translation import gettext_lazy as _ 

from django.core.mail import send_mail, EmailMessage, EmailMultiAlternatives 
from django.conf import settings 
from django.template.loader import render_to_string 
import datetime 

#-------------------------------------------------------------
#-------------------------------------------------------------
# Create your models here.

# Create Contact Model
# main.models.Contact 
class Contact(Model):
    """
        Define a contact model to gather information about a contact.
    """
    
    # Define model methods 
    
    # Define model subclasses 
    class Type(TextChoices):
        """
            Define TextChoices for contact types.
        """
        JOB = 'JOB', 'Work Request'
        GENERAL = 'GENERAL', 'General Inquiry'
    
    # Define Auto-Generated model fields 
    id = models.BigAutoField(primary_key=True) # Primary key
    date = models.DateTimeField(_('Date'), auto_now=True, blank=True, null=True, help_text="The date and time of the contact")
    type = models.CharField(_('Type'), max_length=7, default=Type.GENERAL, choices=Type.choices, help_text="The type of contact")
    
    # Define Boolean model fields 
    
    # Define Optional model fields
    phone_number = PhoneNumberField(_('Phone Number'), blank=True, help_text="The phone number of the contact")
    business = models.CharField(_('Business'), max_length=50, blank=True, null=True, help_text="The business name of the contact")
    
    # Define Required model fields
    first_name = models.CharField(_('First Name'), max_length=50, help_text="The first name of the contact")
    last_name = models.CharField(_('Last Name'), max_length=50, help_text="The last name of the contact")
    email = models.EmailField(_('Email'), help_text="The email address of the contact")
    message = models.TextField(_('Message'), help_text="The message of the contact")
    
# Create Certificate Model
# main.models.Certificate 
class Certificate(Model):   
    """
    Define a certificate model to collect information about certifications completed.
    """

    # Define model methods
    def __str__(self):
        return self.name

    # Define model subclasses
    class Type(TextChoices):
        """
            Define TextChoices for certificate types.
        """
        SPEC = 'SPEC', 'Specialization'
        COURSE = 'COURSE', 'Course'
        DIPLOMA = 'DIPLOMA', 'Diploma'
        DEGREE = 'DEGREE', 'Degree'

    # Define auto-generated model fields
    id = models.BigAutoField(primary_key=True) # Primary key
    date_submit = models.DateTimeField(_('Date Submitted'), auto_now=True, blank=True, null=True, help_text="The date and time of submission")

    # Define Boolean model fields

    # Define Optional model fields
    img = models.ImageField(_('Image'), upload_to='main/images/certs/', blank=True, null=True, help_text="Upload image for certificate")
    pdf = models.FileField(_('PDF'), upload_to='main/pdf/certs/', blank=True, null=True, help_text="Upload pdf for certificate")
    issued_by = models.CharField(_('Issued By'), max_length=50, blank=True, null=True, help_text="The issuer of the certificate")
    link = models.URLField(_('URL'), max_length=200, blank=True, null=True, help_text="The URL to the certificate")
    grade = models.DecimalField(_('Grade'), decimal_places=2, max_digits=5, blank=True, null=True, help_text="The grade of the certificate")

    # Define Required model fields
    name = models.CharField(_('Name'), max_length=100, help_text="The name of the certificate")
    type = models.CharField(_('Type'), max_length=7, default=Type.SPEC, choices=Type.choices, help_text="The type of certificate")
    date_complete = models.DateField(_('Date Complete'), help_text="The date of the certificate")

# Create Skill Model
# main.models.Skills 
class Skill(Model):   
    """
    Define a skill model to collect information about skills obtained.
    """

    # Define model methods
    def __str__(self):
        return self.name

    # Define model subclasses
    class Type(TextChoices):
        """
            Define TextChoices for certificate types.
        """
        FRAMEWORK = 'FRAMEWORK', 'Framework'
        LANGUAGE = 'LANGUAGE', 'Language'
        LIBRARY = 'LIBRARY', 'Library'
        PERSONAL = 'PERSONAL', 'Personal'
        BUSINESS = 'BUSINESS', 'Software - Business'
        DESIGN = 'DESIGN', 'Software - Design'
        PROGRAMMING = 'PROGRAMMING', 'Software - Programming'

    # Define auto-generated model fields
    id = models.BigAutoField(primary_key=True) # Primary key
    date_submit = models.DateTimeField(_('Date Submitted'), auto_now=True, blank=True, null=True, help_text="The date and time of submission")

    # Define Boolean model fields

    # Define Optional model fields
    
    # Define Required model fields
    name = models.CharField(_('Name'), max_length=100, help_text="The name of the skill")
    type = models.CharField(_('Type'), max_length=11, default=Type.PERSONAL, choices=Type.choices, help_text="The type of skill")

# Create Interest Model
# main.models.Interest 
class Interest(Model):   
    """
    Define a interest model to collect information about interests.
    """

    # Define model methods
    def __str__(self):
        return self.name

    # Define model subclasses
    class Type(TextChoices):
        """
            Define TextChoices for certificate types.
        """
        PERSONAL = 'PERSONAL', 'Personal'
        CAREER = 'CAREER', 'Career'

    # Define auto-generated model fields
    id = models.BigAutoField(primary_key=True) # Primary key
    date_submit = models.DateTimeField(_('Date Submitted'), auto_now=True, blank=True, null=True, help_text="The date and time of submission")

    # Define Boolean model fields

    # Define Optional model fields
    
    # Define Required model fields
    name = models.CharField(_('Name'), max_length=100, help_text="The name of the interest")
    type = models.CharField(_('Type'), max_length=8, default=Type.PERSONAL, choices=Type.choices, help_text="The type of interest")


# Create Project Model
# main.models.Project 
class Project(Model):   
    """
    Define a project model to collect information about projects.
    """

    # Define model methods
    def __str__(self):
        return self.name

    # Define model subclasses
    class Type(TextChoices):
        """
            Define TextChoices for project types.
        """
        LIBRARY = 'LIBRARY', 'Library'
        PROJECT = 'PROJECT', 'Project'
        SCHOOL = 'SCHOOL', 'School'
        TEMPLATE = 'TEMPLATE', 'Template'
        WORK = 'WORK', 'Work'

    # Define auto-generated model fields
    id = models.BigAutoField(primary_key=True) # Primary key
    date_submit = models.DateTimeField(_('Date Submitted'), auto_now=True, blank=True, null=True, help_text="The date and time of submission")

    # Define Boolean model fields
    is_featured = models.BooleanField(_('Is Featured'), default=False, help_text="Whether or not the project is featured")
    

    # Define Optional model fields
    description = models.TextField(_('Description'), blank=True, null=True, help_text="This is the description of the project")
    img = models.ImageField(_('Image'), upload_to="main/images/projects/", blank=True, null=True, help_text="The image to display for this project")
    link = models.URLField(_('Link'), max_length=200, blank=True, null=True, help_text="The link to this project")
    github = models.URLField(_('Github'), max_length=200, blank=True, null=True, help_text="The Github URL to this project")
    
    # Define Required model fields
    name = models.CharField(_('Name'), max_length=100, help_text="The name of the project")
    type = models.CharField(_('Type'), max_length=8, default=Type.PROJECT, choices=Type.choices, help_text="The type of project")

# Create Project Images Model
# main.models.ProjectImages 
class ProjectImage(Model):   
    """
    Define a project image model to collect images for specific project.
    """

    # Define model methods
    def __str__(self):
        return self.name

    # Define model subclasses
    class Type(TextChoices):
        """
            Define TextChoices for image types.
        """
        HOME = 'HOME', 'Home'
        CONTACT = 'CONTACT', 'Contact'
        MENU = 'MENU', 'Menu'
        OTHER = 'OTHER', 'Other'

    # Define auto-generated model fields
    id = models.BigAutoField(primary_key=True) # Primary key
    date_submit = models.DateTimeField(_('Date Submitted'), auto_now=True, blank=True, null=True, help_text="The date and time of submission")

    # Define Boolean model fields

    # Define Optional model fields
    
    # Define Required model fields
    name = models.CharField(_('Name'), max_length=100, help_text="The name of the image")
    type = models.CharField(_('Type'), max_length=8, default=Type.OTHER, choices=Type.choices, help_text="The type of image")
    img = models.ImageField(_('Image'), upload_to='main/images/projects/', help_text="The image to disply for this project")
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="Images", help_text="The project attached to this image")

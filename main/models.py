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
    
    
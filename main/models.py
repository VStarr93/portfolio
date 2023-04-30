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

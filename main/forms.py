# main/forms.py
#-------------------------------------------------------------
#-------------------------------------------------------------
# IMPORTS

from django import forms 
from django.forms import ModelForm
from main.models import *
from django.contrib.auth import get_user_model

#-------------------------------------------------------------
#-------------------------------------------------------------
# Forms

class ContactForm(ModelForm):
    """
        Define a Contact form to collect information about a contact.
    """
    
    class Meta:
        model = Contact 
        fields = ['first_name', 'last_name', 'business', 'email', 'phone_number', 'type', 'message']
    
    
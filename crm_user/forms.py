# crm_user/forms.py
#-------------------------------------------------------------
#-------------------------------------------------------------
# IMPORTS

from django import forms 
from crm_user.models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

#-------------------------------------------------------------
#-------------------------------------------------------------
# Forms

class CustomUserCreationForm(UserCreationForm):
    """
        Define a Custom UserCreationForm.
    """

    class Meta:
        model = get_user_model() 
        fields = ('first_name', 'last_name', 'type', 'email', 'password1', 'password2', )

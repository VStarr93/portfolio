#./crm_user/tests/forms/test_SimpleEmployeeCreationForm.py
#-------------------------------------------------------------
#-------------------------------------------------------------
# IMPORTS

from django.test import TestCase, override_settings
from crm_user.forms import *
from crm_user.models import *
from django.core.exceptions import ValidationError 
import datetime 
from django.core.files.uploadedfile import SimpleUploadedFile 
import shutil, tempfile 

# For Testing Email Services
from django.core import mail 
#-------------------------------------------------------------
#-------------------------------------------------------------
# Create your Variables here.

MEDIA_ROOT = tempfile.mkdtemp()


#-------------------------------------------------------------
#-------------------------------------------------------------
# Create your Simple Employee Creation Form tests here.
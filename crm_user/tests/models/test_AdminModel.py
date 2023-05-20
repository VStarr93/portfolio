#./crm_user/tests/models/test_AdminModel.py
#-------------------------------------------------------------
#-------------------------------------------------------------
# IMPORTS

from django.test import TestCase, override_settings
from crm_user.models import Admin
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
# Create your Admin - PROXY Model tests here.

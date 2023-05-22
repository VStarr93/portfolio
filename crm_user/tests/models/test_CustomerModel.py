#./crm_user/tests/models/test_CustomerModel.py
#-------------------------------------------------------------
#-------------------------------------------------------------
# IMPORTS

from django.test import TestCase, override_settings
from crm_user.models import Customer 
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
# Create your Customer - PROXY Model tests here.

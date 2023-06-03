#./crm_user/tests/test_views.py
#-------------------------------------------------------------
#-------------------------------------------------------------
# IMPORTS

from django.test import TestCase, override_settings, Client 
from crm_user.forms import *
from crm_user.models import *
from django.core.exceptions import ValidationError 
import datetime 
from django.core.files.uploadedfile import SimpleUploadedFile 
import shutil, tempfile 
from django.forms.models import modelformset_factory 
from django.conf import settings  

# For Testing Email Services
from django.core import mail 

# For HTTP 
from http import HTTPStatus

# For DB Freeze 
from freezegun import freeze_time 
from django.utils import timezone

#-------------------------------------------------------------
#-------------------------------------------------------------
# Create your Variables here.


#-------------------------------------------------------------
#-------------------------------------------------------------
# Create your Profile View tests here.



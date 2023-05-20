#./crm_user/tests/commands/test_commands.py
#-------------------------------------------------------------
#-------------------------------------------------------------
# IMPORTS

from django.test import TestCase

# Management Commands
from io import StringIO 
from django.core.management import call_command 
from django.contrib.auth.models import Group, Permission 
from django.contrib.contenttypes.models import ContentType 


#-------------------------------------------------------------
#-------------------------------------------------------------
# Create your Variables here.


#-------------------------------------------------------------
#-------------------------------------------------------------
# Create your Management Commands tests here.

# Create a TestCase for creategroup command
# crm_user.tests.test_commands.CreategroupTests
class CreategroupTests(TestCase):
    """
        Test creategroup command
    """
    def test_creategroup_output(self):
        """
            creategroup command runs successfully with 1 argument
        """
        out = StringIO()
        call_command("creategroup", 'new_group', stdout=out)
        self.assertIn("Successfully created", out.getvalue())


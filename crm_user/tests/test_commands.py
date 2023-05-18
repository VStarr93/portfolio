#./crm_user/tests/test_commands.py
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

#Create a TestCase for createperm command
# crm_user.tests.test_commands.CreatepermTests
class CreatepermTests(TestCase):
    """
        Test createperm command
    """
    def test_createperm_output(self):
        """
            createperm command runs successfully with 1 argument per option
        """
        out = StringIO()
        call_command("createperm", "add", "-m", "user", "-g", "admins", stdout=out)
        self.assertIn("Successfully added", out.getvalue())
        self.assertTrue(Group.objects.get(name='admins'))
        self.assertTrue(Permission.objects.get(name='Can add user'))
        self.assertTrue(Group.objects.get(name='admins').permissions.get(name='Can add user'))

    def test_createperm_two_models(self):
        """
            createperm command runs successfully with 2 arguments for model option
        """
        out = StringIO()
        call_command("createperm", "add", "-m", "user", 'customer', "-g", "admins", stdout=out)
        self.assertIn("Successfully added", out.getvalue())
        self.assertTrue(Group.objects.get(name='admins'))
        self.assertTrue(Permission.objects.get(name='Can add user'))
        self.assertTrue(Permission.objects.get(name='Can add customer'))
        self.assertTrue(Group.objects.get(name='admins').permissions.get(name='Can add user'))
        self.assertTrue(Group.objects.get(name='admins').permissions.get(name='Can add customer'))

    def test_createperm_two_groups(self):
        """
            createperm command runs successfully with 2 arguments for group option
        """
        out = StringIO()
        call_command("createperm", "add", "-m", "user", "-g", "admins", "customers", stdout=out)
        self.assertIn("Successfully added", out.getvalue())
        self.assertTrue(Group.objects.get(name='admins'))
        self.assertTrue(Group.objects.get(name='customers'))
        self.assertTrue(Permission.objects.get(name='Can add user'))
        self.assertTrue(Group.objects.get(name='admins').permissions.get(name='Can add user'))
        self.assertTrue(Group.objects.get(name='customers').permissions.get(name='Can add user'))

    def test_createperm_two_perms(self):
        """
            createperm command runs successfully with 2 arguments for perm_name positional argument
        """
        out = StringIO()
        call_command("createperm", "add", "view", "-m", "user", "-g", "admins", stdout=out)
        self.assertIn("Successfully added", out.getvalue())
        self.assertTrue(Group.objects.get(name='admins'))
        self.assertTrue(Permission.objects.get(name='Can add user'))
        self.assertTrue(Permission.objects.get(name='Can view user'))
        self.assertTrue(Group.objects.get(name='admins').permissions.get(name='Can add user'))
        self.assertTrue(Group.objects.get(name='admins').permissions.get(name='Can view user'))

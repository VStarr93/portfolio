# crm_user.management.commands.initperms.py
# This module will be available as a management command
#-------------------------------------------------------------
#-------------------------------------------------------------
# IMPORTS

from django.core.management.base import BaseCommand, CommandError
from crm_user.models import *
from django.contrib.auth.models import Group, Permission 
from django.contrib.contenttypes.models import ContentType 


#-------------------------------------------------------------
#-------------------------------------------------------------
# Variables
    
GROUPS = {
    'admins': {
        # Built-In Models
        'log entry': ['add', 'view', 'change', 'delete'],
        'group': ['add', 'view', 'change', 'delete'],
        'permission': ['add', 'view', 'change', 'delete'],
        'content type': ['add', 'view', 'change', 'delete'],
        'session': ['add', 'view', 'change', 'delete'],
            
        # App Models
        'user': ['add', 'view', 'change', 'delete'],
        'employee': ['add', 'view', 'change', 'delete'],
        'admin': ['add', 'view', 'change', 'delete'],
        'customer': ['add', 'view', 'change', 'delete'],
    },
    'empManagement': {
        'employee': ['add', 'view', 'change', 'delete'],
        'admin': ['view'],
        'customer': ['add', 'view', 'change', 'delete'],
    },
    'empStandard': {
        'employee': ['view', 'change'],
        'customer': ['add', 'view', 'change'],
    },
    'customers': {
        'employee': ['view'],
        'customer': ['view', 'change'],
    },
}


#-------------------------------------------------------------
#-------------------------------------------------------------
# COMMAND

class Command(BaseCommand):
    help = "Places built-in permissions into specified groups"
    
    def get_version(self):
        """
        Return the Django version, which should be correct for all built-in
        Django commands. User-supplied commands can override this method to
        return their own version.
        """
        return '1.0.0'

    def handle(self, *args, **options):

        # loop through groups
        for group in GROUPS:

            # get or create group
            groupname = group + '_group'
            groupname, created = Group.objects.get_or_create(name=group)

            # loop through models
            for model in GROUPS[group]:

                # loop through permissions
                for permission in GROUPS[group][model]:

                    # define name of permission in Django format
                    name = "Can {} {}".format(permission, model)

                    # Get existing permission
                    try:
                        perm = Permission.objects.get(name=name)
                    except Permission.DoesNotExist:
                        self.stdout.write(
                            self.style.ERROR('Permission not found with name "%s".' %name)
                        )
                        continue 

                    # add permission to group
                    groupname.permissions.add(perm)

                    # display success message
                    self.stdout.write(
                        self.style.SUCCESS('Permission named "%s" was successfully added to "%s"' %(name, groupname))
                    )
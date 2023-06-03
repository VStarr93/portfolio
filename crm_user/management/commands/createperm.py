# crm_user.management.commands.createperm.py
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
# COMMAND

class Command(BaseCommand):
    help = "Creates the specified permission and adds it to a group"

    def add_arguments(self, parser):
        # Positional arguments
        parser.add_argument(
            "perm_name", # argument name
            nargs="+", # REQUIRED. all arguments are gathered into a list
            type=str, # type must be a string
            help="Enter the name of the permission you wish to create" # text to be displayed with help command
        )

        # Named (optional) arguments
        parser.add_argument(
            "--model_name", "-m", # option name(s)
            action="store", # stores the argument's value
            nargs="+", # REQUIRED 1 argument
            #type=str, # type must be a string
            help="Enter the name of the permission you wish to create" # text to be displayed with help command
        )
        
        parser.add_argument(
            "--group_name", "-g", # option name(s)
            action="store", # stores the argument's value
            nargs="+", # REQUIRED. all arguments are gathered into a list
            type=str, # type must be a string
            help="Enter the name of the group you wish permissions to be attached to" # text to be displayed with help command
        )
        
    def get_version(self):
        """
        Return the Django version, which should be correct for all built-in
        Django commands. User-supplied commands can override this method to
        return their own version.
        """
        return '1.0.0'

    def handle(self, *args, **options):
        for perm in options["perm_name"]:
            # Get or Create permission
            for model in options["model_name"]:
                codename = perm + "_" + model
                name = "Can " + perm + " " + model
                contenttype = ContentType.objects.get(app_label='crm_user', model=model)
                try:
                    permission = Permission.objects.get(codename=codename, content_type=contenttype)
                    self.stdout.write("Permission already exists.")
                except Permission.DoesNotExist:
                    permission = Permission.objects.create(codename=codename, name=name, content_type=contenttype)
                    self.stdout.write("Permission was successfully created.")

                # Get or Create Group
                for group in options['group_name']:
                    groupname = group + "_group"
                    groupname, created = Group.objects.get_or_create(name=group)

                    # Add permissions to group
                    groupname.permissions.add(permission.id)

                self.stdout.write(
                    self.style.SUCCESS('Successfully added %s to %s!' %(permission.name, groupname))
                )
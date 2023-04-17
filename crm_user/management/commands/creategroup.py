# crm_user.management.commands.creategroup.py
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
    help = "Creates the specified group"

    def add_arguments(self, parser):
        # Positional arguments
        parser.add_argument(
            "group_name", # argument name
            nargs="+", # REQUIRED. all arguments are gathered into a list
            type=str, # type must be a string
            help="Enter the name of the group you wish to create" # text to be displayed with help command
        )

        # Named (optional) arguments
        parser.add_argument(
            "-p", "--permission", # option name(s)
            action="store", # stores the argument's value
            nargs="*", # all arguments are gathered into a list
            help="Add permission to group" # text to be displayed with help command
        )

    def get_version(self):
        """
        Return the Django version, which should be correct for all built-in
        Django commands. User-supplied commands can override this method to
        return their own version.
        """
        return '1.0.0'

    def handle(self, *args, **options):
        for group in options["group_name"]:
            groupname = group + '_group'
            groupname, created = Group.objects.get_or_create(name=group)

            self.stdout.write(
                self.style.SUCCESS('Successfully created %s_group!' %group)
            )
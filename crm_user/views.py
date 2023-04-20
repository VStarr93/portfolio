# crm_user/views.py
#-------------------------------------------------------------
#-------------------------------------------------------------
# IMPORTS

from django.shortcuts import render
from django.http import HttpResponse 

#-------------------------------------------------------------
#-------------------------------------------------------------
# Create your views here.

# INDEX view
def index(request):
    """
        This is a basic view for crm_user app.
    """
    return HttpResponse("This is the Index for CRM_USER app.")
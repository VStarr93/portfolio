# ./main/admin.py
#-------------------------------------------------------------
#-------------------------------------------------------------
# IMPORTS

from django.contrib import admin
from main.models import Contact, Certificate


#-------------------------------------------------------------
#-------------------------------------------------------------
# Register your models here.

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    """ This is the admin interface for the Contact Model."""
    readonly_fields = ['id', 'date']
        
@admin.register(Certificate)
class CertificateAdmin(admin.ModelAdmin):
    """ This is the admin interface for the Certificate Model."""
    readonly_fields = ['id', 'date_submit']
    

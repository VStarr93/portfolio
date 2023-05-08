# ./main/admin.py
#-------------------------------------------------------------
#-------------------------------------------------------------
# IMPORTS

from django.contrib import admin
from main.models import Contact, Certificate, Skill, Interest, Project, ProjectImage


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
    
@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    """ This is the admin interface for the Skill Model."""
    readonly_fields = ['id', 'date_submit']
    
@admin.register(Interest)
class InterestAdmin(admin.ModelAdmin):
    """ This is the admin interface for the Interest Model."""
    readonly_fields = ['id', 'date_submit']
    
@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    """ This is the admin interface for the Project Model."""
    readonly_fields = ['id', 'date_submit']
    
@admin.register(ProjectImage)
class ProjectImageAdmin(admin.ModelAdmin):
    """ This is the admin interface for the Project Images Model."""
    readonly_fields = ['id', 'date_submit']

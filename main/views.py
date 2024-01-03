# main/views.py
#-------------------------------------------------------------
#-------------------------------------------------------------
# IMPORTS

from django.shortcuts import render, redirect
from main.forms import ContactForm
from main.models import Certificate, Skill, Interest, Project, ProjectImage 

#-------------------------------------------------------------
#-------------------------------------------------------------
# Create your views here.

# Contact View 
def contact_view(request):
    """
        This is a Contact Me view.
    """
    
    if request.method == 'GET':
        form = ContactForm 
        return render(request, 'main/contact.html', context={'form': form})

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            message = form.errors 
            context = {
                'form': ContactForm(request.POST),
                'message': message,
            }
            return render(request, 'main/contact.html', context)
        
# About View
def about_view(request):
    """ This is an About view."""
    
    if request.method == 'GET':
        certs = Certificate.objects.all()
        skills = Skill.objects.all()
        interests = Interest.objects.all()
        return render(request, 'main/about.html', context={'certs': certs, 'skills': skills, 'interests': interests})

# Projects View
def projects_view(request):
    """ This is a Project List view."""
    
    if request.method == 'GET':
        projects = Project.objects.all()
        school = Project.objects.all().filter(type='SCHOOL')
        fun = Project.objects.all().filter(type='FUN')
        library = Project.objects.all().filter(type='LIBRARY')
        client = Project.objects.all().filter(type='CLIENT')
        template = Project.objects.all().filter(type='TEMPLATE')
        featured = Project.objects.all().filter(is_featured=True)
        context = {
            'projects': projects,
            'tschool': school,
            'tfun': fun,
            'tlibrary': library,
            'tclient': client,
            'ttemplate': template,
            'tfeatured': featured,
        }
        return render(request, 'main/projects.html', context=context)
    
# Project View
def project_view(request, id):
    """ This is an individual Project view."""
    
    if request.method == 'GET':
        project = Project.objects.get(id=id)
        images = ProjectImage.objects.filter(project=project)
        return render(request, 'main/project.html', context={'project': project, 'images': images})
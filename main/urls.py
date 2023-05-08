# main/urls.py
#-------------------------------------------------------------
#-------------------------------------------------------------
# IMPORTS

from django.urls import path 
from . import views 
from django.views.generic.base import TemplateView


#-------------------------------------------------------------
#-------------------------------------------------------------
# URL Patterns

app_name = 'main'
urlpatterns = [
    # path for index view
    path('', TemplateView.as_view(template_name='main/home.html'), name='home'),
    path('about/', views.about_view, name='about'),
    path('contact/', views.contact_view, name='contact'),
    path('projects/', views.projects_view, name='projects'),
    path('projects/<int:id>', views.project_view, name='project'),
]


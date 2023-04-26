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

]


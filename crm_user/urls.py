# crm_user/urls.py
#-------------------------------------------------------------
#-------------------------------------------------------------
# IMPORTS

from django.urls import path 
from . import views 
from django.views.generic.base import TemplateView


#-------------------------------------------------------------
#-------------------------------------------------------------
# URL Patterns

app_name = 'crm_user'
urlpatterns = [
    # path for index view
    path('', TemplateView.as_view(template_name='crm_user/home.html'), name='home'),
    path('register/', views.user_registration, name='register'),
    path('profile/', views.profile_view, name='profile'),

]


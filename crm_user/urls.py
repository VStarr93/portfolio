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
    path('', views.index, name='home'),
    path('register/', views.user_registration, name='register'),
    path('profile/', views.profile_view, name='profile'),
    path('user-details/<int:id>', views.user_details_view, name='user-details'),

]


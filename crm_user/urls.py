# crm_user/urls.py
#-------------------------------------------------------------
#-------------------------------------------------------------
# IMPORTS

from django.urls import path 
from . import views 

#-------------------------------------------------------------
#-------------------------------------------------------------
# URL Patterns

app_name = 'crm_user'
urlpatterns = [
    # path for index view
    path('', views.index, name='index'),
]


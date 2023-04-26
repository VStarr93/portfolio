# portfolio/urls.py
#-------------------------------------------------------------
#-------------------------------------------------------------
# IMPORTS

"""
URL configuration for portfolio project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include 
from django.views.generic.base import TemplateView

#-------------------------------------------------------------
#-------------------------------------------------------------
# URL Patterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('user/', include('crm_user.urls')),
    path('', include('main.urls')),
]

#-------------------------------------------------------------
#-------------------------------------------------------------
# URL Notes

# If you want specified url paths,
# you can call each view separately as follows:
# path('login/', views.LoginView.as_view(), name='login'),

# If you wish to change the template name a view uses,
# you can provide the template_name argument as follows:
# path('login/', views.LoginView.as_view(template_name="login-template.html")),


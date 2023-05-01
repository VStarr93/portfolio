# main/views.py
#-------------------------------------------------------------
#-------------------------------------------------------------
# IMPORTS

from django.shortcuts import render, redirect
from main.forms import ContactForm

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
# main/forms.py
#-------------------------------------------------------------
#-------------------------------------------------------------
# IMPORTS

from django import forms 
from django.forms import ModelForm
from main.models import *
from django.contrib.auth import get_user_model
from crispy_forms.helper import FormHelper 
from crispy_forms.layout import Submit, Layout, Fieldset, HTML, Div, Field
from crispy_forms.bootstrap import AppendedText, PrependedText  

#-------------------------------------------------------------
#-------------------------------------------------------------
# Forms

class ContactForm(ModelForm):
    """
        Define a Contact form to collect information about a contact.
    """
    
    def __init__(self, *args, **kwargs):
        """ Define init method for ContactForm"""
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-contactform'
        self.helper.form_class = 'v-forms'
        self.helper.form_method = 'post'
        
        self.helper.label_class = ""
        self.helper.field_class = ""
        
        self.helper.layout = Layout(
            HTML("""
                <h2 class="text-center">Reach Out!</h2>
                <p class="text-center">
                    Please fill out the following form and I will reach out to you as soon as possible.
                </p>
            """),
            Div(
                Fieldset(
                    'Contact Information',
                    HTML("""<hr/>"""),
                    Div(
                        Div(
                            Field('first_name', wrapper_class="me-2 w-50", css_class="w-100"),
                            Field('last_name', wrapper_class="ms-2 w-50", css_class="w-100"),
                            css_class="d-flex flex-row justify-content-start",
                        ),
                        'business',
                        AppendedText('email', '@example.com'),
                        PrependedText('phone_number', '+1'),
                        css_class="text-start",
                    ),
                    css_class = "text-center m-2",
                ),
                Fieldset(
                    'Inquiry Information',
                    HTML("""<hr/>"""),
                    Div(
                        'type',
                        'message',
                        css_class="text-start",
                    ),
                    css_class="text-center m-2",
                ),
                css_class="d-flex flex-column flex-lg-row justify-content-around",
            ),
            Div(
                Submit('submit', 'Submit'),
                css_class="text-center",
            ),
        )
        
        # self.helper.add_input(Submit('submit', 'Submit'))
    
    class Meta:
        model = Contact 
        fields = ['first_name', 'last_name', 'business', 'email', 'phone_number', 'type', 'message']
    
    
# crm_user/forms.py
#-------------------------------------------------------------
#-------------------------------------------------------------
# IMPORTS

from django import forms 
from crm_user.models import *
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import get_user_model
from crispy_forms.helper import FormHelper 
from crispy_forms.layout import Layout, Submit, HTML, Div, Field 
from crispy_forms.bootstrap import FormActions, StrictButton

#-------------------------------------------------------------
#-------------------------------------------------------------
# Forms

class CustomUserCreationForm(UserCreationForm):
    """
        Define a Custom UserCreationForm.
    """

    class Meta:
        model = get_user_model() 
        fields = ('first_name', 'last_name', 'type', 'email', 'password1', 'password2', )

# Create CustomerCreationForm
class CustomerCreationForm(UserCreationForm):
    """ Define a CustomerCreationForm """
    
    type = User.Types.CUSTOMER
    
    def __init__(self, *args, **kwargs):
        """ Define init method for Custom User Change Form """
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-customercreationform'
        self.helper.form_class = 'v-forms'
        self.helper.form_method = 'post'
        
        self.helper.layout = Layout(
            HTML("""
                <h2 class="text-center">Register</h2>
                <p class='text-center'>
                    Fill out the form below to create a new customer account. 
                </p>
            """),
            Div(
                Div(
                    Field('first_name', wrapper_class='v-fields-name', css_class="w-100"),
                    Field('middle_name', wrapper_class='v-fields-name', css_class="w-100"),
                    Field('last_name', wrapper_class='v-fields-name', css_class="w-100"),
                    css_class="d-flex flex-column flex-sm-row justify-content-start",
                ),
                'email',
                'password1',
                'password2',
                css_class="text-start",
            ),
            Div(
                Submit('submitCustomer', 'Create My Account'),
                css_class="d-flex justify-content-center mt-3",
            )
        )
    
    class Meta:
        model = Customer 
        fields = ('first_name', 'middle_name', 'last_name', 'email', 'password1', 'password2')

# Create EmployeeCreationForm
class EmployeeCreationForm(UserCreationForm):
    """ Define a EmployeeCreationForm """
    
    type = User.Types.EMPLOYEE
    
    def __init__(self, *args, **kwargs):
        """ Define init method for Employee Creation Form """
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-employeecreationform'
        self.helper.form_class = 'v-forms'
        self.helper.form_method = 'post'
        
        self.helper.layout = Layout(
            HTML("""
                <h2 class="text-center">Register</h2>
                <p class='text-center'>
                    Fill out the form below to create a new employee account. 
                </p>
            """),
            Div(
                Div(
                    Field('first_name', wrapper_class='v-fields-name', css_class="w-100"),
                    Field('middle_name', wrapper_class='v-fields-name', css_class="w-100"),
                    Field('last_name', wrapper_class='v-fields-name', css_class="w-100"),
                    css_class="d-flex flex-column flex-sm-row justify-content-start",
                ),
                'email',
                'password1',
                'password2',
                css_class="text-start",
            ),
            Div(
                Submit('submitEmployee', 'Create My Account'),
                css_class="d-flex justify-content-center mt-3",
            )
        )
    
    class Meta:
        model = Employee 
        fields = ('first_name', 'middle_name', 'last_name', 'email', 'password1', 'password2')

# Create AdminCreationForm
class AdminCreationForm(UserCreationForm):
    """ Define a AdminCreationForm """
    
    type = User.Types.ADMIN
    
    def __init__(self, *args, **kwargs):
        """ Define init method for Admin Creation Form """
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-admincreationform'
        self.helper.form_class = 'v-forms'
        self.helper.form_method = 'post'
        
        self.helper.layout = Layout(
            HTML("""
                <h2 class="text-center">Register</h2>
                <p class='text-center'>
                    Fill out the form below to create a new admin account. 
                </p>
            """),
            Div(
                Div(
                    Field('first_name', wrapper_class='v-fields-name', css_class="w-100"),
                    Field('middle_name', wrapper_class='v-fields-name', css_class="w-100"),
                    Field('last_name', wrapper_class='v-fields-name', css_class="w-100"),
                    css_class="d-flex flex-column flex-sm-row justify-content-start",
                ),
                'email',
                'password1',
                'password2',
                css_class="text-start",
            ),
            Div(
                Submit('submitAdmin', 'Create My Account'),
                css_class="d-flex justify-content-center mt-3",
            )
        )
    
    class Meta:
        model = Admin 
        fields = ('first_name', 'middle_name', 'last_name', 'email', 'password1', 'password2')

# Create CustomerCreationForm without password Required
class SimpleCustomerCreationForm(forms.ModelForm):
    """ Define a SimpleCustomerCreationForm without password"""
    
    def __init__(self, *args, **kwargs):
        """ Define init method for Simple Customer Creation Form """
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-simplecustomercreationform'
        self.helper.form_class = 'v-forms'
        self.helper.form_method = 'post'
        
        self.helper.layout = Layout(
            HTML("""
                <h2 class="text-center">Register</h2>
                <p class='text-center'>
                    Fill out the form below to create a new customer account. 
                </p>
            """),
            Div(
                Div(
                    Field('first_name', wrapper_class='v-fields-name', css_class="w-100"),
                    Field('middle_name', wrapper_class='v-fields-name', css_class="w-100"),
                    Field('last_name', wrapper_class='v-fields-name', css_class="w-100"),
                    css_class="d-flex flex-column flex-sm-row justify-content-start",
                ),
                'email',
                'password1',
                'password2',
                css_class="text-start",
            ),
            Div(
                Submit('submitCustomerSimple', 'Create My Account'),
                css_class="d-flex justify-content-center mt-3",
            )
        )
    
    def save(self, commit=True):
        instance = super().save(commit=False)
        email = self.cleaned_data['email']
        password = None 
        first_name = self.cleaned_data['first_name']
        middle_name = self.cleaned_data['middle_name']
        last_name = self.cleaned_data['last_name']
        if commit:
            user = Customer.objects.create_user(email, password, first_name=first_name, last_name=last_name, middle_name=middle_name)
        return instance
        
    
    class Meta:
        model = Customer 
        fields = ('first_name', 'middle_name', 'last_name', 'email')
        # exclude = ('password1', 'password2')

# Create EmployeeCreationForm without password Required
class SimpleEmployeeCreationForm(forms.ModelForm):
    """ Define a SimpleEmployeeCreationForm without password"""
    
    def __init__(self, *args, **kwargs):
        """ Define init method for Simple Employee Creation Form """
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-simpleemployeecreationform'
        self.helper.form_class = 'v-forms'
        self.helper.form_method = 'post'
        
        self.helper.layout = Layout(
            HTML("""
                <h2 class="text-center">Register</h2>
                <p class='text-center'>
                    Fill out the form below to create a new employee account. 
                </p>
            """),
            Div(
                Div(
                    Field('first_name', wrapper_class='v-fields-name', css_class="w-100"),
                    Field('middle_name', wrapper_class='v-fields-name', css_class="w-100"),
                    Field('last_name', wrapper_class='v-fields-name', css_class="w-100"),
                    css_class="d-flex flex-column flex-sm-row justify-content-start",
                ),
                'email',
                'password1',
                'password2',
                css_class="text-start",
            ),
            Div(
                Submit('submitEmployeeSimple', 'Create My Account'),
                css_class="d-flex justify-content-center mt-3",
            )
        )
    
    def save(self, commit=True):
        instance = super().save(commit=False)
        email = self.cleaned_data['email']
        password = None 
        first_name = self.cleaned_data['first_name']
        middle_name = self.cleaned_data['middle_name']
        last_name = self.cleaned_data['last_name']
        if commit:
            user = Employee.objects.create_user(email, password, first_name=first_name, last_name=last_name, middle_name=middle_name)
        return instance
    
    class Meta:
        model = Employee 
        fields = ('first_name', 'middle_name', 'last_name', 'email')

# Create AdminCreationForm without password Required
class SimpleAdminCreationForm(forms.ModelForm):
    """ Define a SimpleAdminCreationForm without password"""
       
    def __init__(self, *args, **kwargs):
        """ Define init method for Simple Admin Creation Form """
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-simpleadmincreationform'
        self.helper.form_class = 'v-forms'
        self.helper.form_method = 'post'
        
        self.helper.layout = Layout(
            HTML("""
                <h2 class="text-center">Register</h2>
                <p class='text-center'>
                    Fill out the form below to create a new admin account. 
                </p>
            """),
            Div(
                Div(
                    Field('first_name', wrapper_class='v-fields-name', css_class="w-100"),
                    Field('middle_name', wrapper_class='v-fields-name', css_class="w-100"),
                    Field('last_name', wrapper_class='v-fields-name', css_class="w-100"),
                    css_class="d-flex flex-column flex-sm-row justify-content-start",
                ),
                'email',
                'password1',
                'password2',
                css_class="text-start",
            ),
            Div(
                Submit('submitAdminSimple', 'Create My Account'),
                css_class="d-flex justify-content-center mt-3",
            )
        )
    
    def save(self, commit=True):
        instance = super().save(commit=False)
        email = self.cleaned_data['email']
        password = None 
        first_name = self.cleaned_data['first_name']
        middle_name = self.cleaned_data['middle_name']
        last_name = self.cleaned_data['last_name']
        if commit:
            user = Admin.objects.create_user(email, password, first_name=first_name, last_name=last_name, middle_name=middle_name)
        return instance
        
    
    class Meta:
        model = Admin 
        fields = ('first_name', 'middle_name', 'last_name', 'email')

# Create User Change Form
class CustomUserChangeForm(UserChangeForm):
    """
        Define a Custom UserChangeForm.
    """
    password = None 

    def __init__(self, *args, **kwargs):
        """ Define init method for Custom User Change Form """
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-changeform'
        self.helper.form_class = 'v-forms'
        self.helper.form_method = 'post'
        
        self.helper.layout = Layout(
            HTML("""
                <h2 class="text-center">User Profile</h2>
                <hr />
            """),
            Div(
                Div(
                    Field('first_name', wrapper_class='v-fields-name', css_class="w-100"),
                    Field('middle_name', wrapper_class='v-fields-name', css_class="w-100"),
                    Field('last_name', wrapper_class='v-fields-name', css_class="w-100"),
                    css_class="d-flex flex-column flex-sm-row justify-content-start",
                ),
                'email',
                'phone_number',
                'birth_date',
                'profile_photo',
                css_class="text-start",
            ),
            HTML("""
                <div>Password</div>
                <div>To change your password, click <a href="{% url 'password_change' %} ">here</a>.</div>
            """),
            Div(
                Submit('submitChange', 'Update My Info'),
                HTML("""
                    <a type="button" class="btn ms-3" href="{% url 'crm_user:profile' %}">Cancel</a>
                """),
                css_class="d-flex justify-content-center mt-3",
            )
        )
    
    class Meta:
        model = get_user_model()
        fields = ('first_name','middle_name', 'last_name', 'email', 'birth_date', 'phone_number', 'profile_photo')
        exclude = ('password',)
        
# Create Address Form
class AddressForm(forms.ModelForm):
    """ Define an Address form """
    
    class Meta:
        model = Address
        fields = ('type', 'name', 'address_line1', 'address_line2', 'city', 'state', 'zip')

class AddressFormHelper(FormHelper):
    """ Define a FormHelper for AddressForm """
    
    def __init__(self, *args, **kwargs):
        """ Define init method for AddressFormHelper """
        super().__init__(*args, **kwargs)
        self.form_method = 'post'
        self.form_class = 'v-forms'
        self.field_class = 'v-table-fields'
        self.add_input(Submit('submitAddress', 'Save My Addresses'))
        self.template = 'crm_user/snippets/table_inline_formset.html'
    
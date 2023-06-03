# ./crm_user/admin.py
#-------------------------------------------------------------
#-------------------------------------------------------------
# IMPORTS

from django.contrib import admin
from crm_user.models import User, Customer, Employee, Admin, AdminProfile, CustomerProfile, EmployeeProfile 
from crm_user.models import Address 
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from crm_user.forms import CustomUserChangeForm, CustomUserCreationForm
from django.contrib.auth.models import Permission

from guardian.admin import GuardedModelAdmin

#-------------------------------------------------------------
#-------------------------------------------------------------
# Register your models here.

admin.site.register(AdminProfile)
admin.site.register(CustomerProfile)
admin.site.register(EmployeeProfile)
admin.site.register(Permission)

#-------------------------------------------------------------
#-------------------------------------------------------------
# Create your Inline Models here.

class InlineCustomerProfile(admin.TabularInline):
    model = CustomerProfile 
   
class InlineEmployeeProfile(admin.TabularInline):
    model = EmployeeProfile
    
class InlineAdminProfile(admin.TabularInline):
    model = AdminProfile
    
#-------------------------------------------------------------
#-------------------------------------------------------------
# Create your Admin Models here.

@admin.register(Address)
class AddressAdmin(GuardedModelAdmin):
    """ This is the admin interface for the Address model. """
    readonly_fields = ['id']
    
    class Meta:
        model = Address 
    
@admin.register(User)
class CustomUserAdmin(GuardedModelAdmin, BaseUserAdmin):
    """ This is the customer user admin interface for the CustomUser model. """
    ordering = ('last_name', 'first_name')
    search_fields = ('first_name', 'last_name', 'email')
    list_display = ('first_name', 'last_name', 'email', 'is_staff', 'is_active')
    list_filter = ('first_name', 'last_name', 'email', 'is_staff', 'is_active')
    filter_horizontal = ('groups', 'user_permissions')
    readonly_fields = ('last_modified','last_modified_by', 'date_joined', 'last_login',)
    fieldsets = [
        ("Log In ", {'fields': ['email', 'password']}),
        ("Personal Information", {'fields': ['first_name','middle_name', 'last_name', 'phone_number', 'birth_date', 'profile_photo', ]}),
        ("Account Information", {'fields': ['type', 'last_modified', 'last_modified_by', 'date_joined', 'last_login', ]}),
        ("Permissions", {'fields': ['is_superuser', 'is_staff', 'is_active', 'groups', 'user_permissions']}),
    ]
    add_fieldsets = [
        (None, {'fields': ['email', 'password']}),
        ("Personal Information", {'fields': ['first_name','middle_name', 'last_name', 'phone_number', 'birth_date', 'profile_photo', ]}),
        ("Account Information", {'fields': ['type', ]}),
        ("Permissions", {'fields': ['is_superuser', 'is_staff', 'is_active', 'groups', 'user_permissions']}),
    ]
    actions = ['activate_users']

    @admin.action(description="Activate users")
    def activate_users(self, request, queryset):
        assert request.user.has_perm('auth.change_user')
        cnt = queryset.filter(is_active=False).update(is_active=True)
        self.message_user(request, 'Activated {} users.'.format(cnt))

    def get_actions(self, request):
        actions = super().get_actions(request)
        if not request.user.has_perm('auth.change_user'):
            del actions['activate_users']
        return actions
    
    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        is_superuser = request.user.is_superuser
        disabled_fields = set()  # type: Set[str]

        if not is_superuser:
            disabled_fields |= {
                'is_superuser',
                'user_permissions',
            }

        # Prevent non-superusers from editing their own permissions
        if (
            not is_superuser
            and obj is not None
            and obj == request.user
        ):
            disabled_fields |= {
                'is_staff',
                'is_superuser',
                'groups',
                'user_permissions',
            }

        for f in disabled_fields:
            if f in form.base_fields:
                form.base_fields[f].disabled = True

        return form
    
    class Meta:
        model = User 
        
@admin.register(Admin)
class AdminAdmin(CustomUserAdmin):
    inlines = [InlineAdminProfile,]
    
    class Meta:
        model = Admin 
        
@admin.register(Customer)
class CustomerAdmin(CustomUserAdmin):
    
    class Meta:
        model = Customer
        
@admin.register(Employee)
class EmployeeAdmin(CustomUserAdmin):
    inlines = [InlineEmployeeProfile,]
    
    class Meta:
        model = Employee
        
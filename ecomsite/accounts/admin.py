<<<<<<< HEAD
from django.contrib import admin
from .models import Account
from django.contrib.auth.admin import UserAdmin
# Register your models here.

class AccountAdmin(UserAdmin):
    list_display=('email','first_name','last_name','date_joined','is_active')
    list_display_links=('email','first_name','last_name')
    readonly_fields=('date_joined','is_active')

    ordering=('-date_joined',)
    
    filter_horizontal=()
    fieldsets=()
    list_filter=()
admin.site.register(Account,AccountAdmin)
=======
from django.contrib import admin
from .models import Account
from django.contrib.auth.admin import UserAdmin
# Register your models here.

class AccountAdmin(UserAdmin):
    list_display=('email','first_name','last_name','date_joined','is_active')
    list_display_links=('email','first_name','last_name')
    readonly_fields=('date_joined','is_active')

    ordering=('-date_joined',)
    
    filter_horizontal=()
    fieldsets=()
    list_filter=()
admin.site.register(Account,AccountAdmin)
>>>>>>> 1b920148f1a38f4fbf6aa142e7f7c9e4481a5ad6

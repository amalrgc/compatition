from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import *
from  mptt.admin import MPTTModelAdmin
from . import models

class MyUserAdmin(BaseUserAdmin):
    list_display=('email','username','date_joined','last_login','is_admin','is_staff')
    search_fields=('email','username') 
    readonly_fields=('date_joined','last_login')
    filter_horizontal=()
    list_filter=('last_login',)
    fieldsets=()
    ordering=('email',)

    add_fieldsets=(
        (None,{
            'classes':('wide'),
            'fields':('email','username','phone','password1','password2'),
        }),
    )
admin.site.register(MyUser,MyUserAdmin)
admin.site.register(Branch)
admin.site.register(Products)
admin.site.register(Variant)
admin.site.register(Warranty)
admin.site.register(CartItems)
admin.site.register(models.Category, MPTTModelAdmin)
admin.site.register(Checkout)
admin.site.register(Orders)
admin.site.register(Profile)



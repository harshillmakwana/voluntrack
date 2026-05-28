from django.contrib import admin
from app_modules.userapp import models

# Register your models here.

@admin.register(models.CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('email', 'role', 'is_approved')
    list_filter = ('role', 'is_approved')
    
admin.site.register(models.booking),
admin.site.register(models.payment),
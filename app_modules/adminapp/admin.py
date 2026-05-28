from django.contrib import admin
from app_modules.adminapp import models 

# Register your models here.

admin.site.register(models.Event),
admin.site.register(models.EventRole),
admin.site.register(models.VolunteerApplication),
admin.site.register(models.TaskAssignment),
admin.site.register(models.Attendance),
admin.site.register(models.Category),
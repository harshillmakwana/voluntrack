from django import forms
from app_modules.adminapp import models


class Event_form(forms.ModelForm):
    class Meta:
        model = models.Event
        fields = '__all__'
        
class EventRole_form(forms.ModelForm):
    class Meta:
        model = models.EventRole
        fields = '__all__'
        
class VolunteerApplication_form(forms.ModelForm):
    class Meta:
        model = models.VolunteerApplication
        fields = '__all__'
        
class TaskAssignment_form(forms.ModelForm):
    class Meta:
        model = models.TaskAssignment
        fields = '__all__'
        
class Attendance_form(forms.ModelForm):
    class Meta:
        model = models.Attendance
        fields = '__all__'
        
class Category_form(forms.ModelForm):
    class Meta:
        model = models.Category
        fields = '__all__'
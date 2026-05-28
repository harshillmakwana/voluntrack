from django import forms
from app_modules.userapp import models
from app_modules.userapp.models import booking 


class VolunteerRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = models.CustomUser
        fields = ['username', 'email', 'phone_number', 'city', 'skills', 'availability', 'password']

class OrganizerRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = models.CustomUser
        fields = ['username', 'email', 'phone_number', 'organization_name', 'organization_type', 'password']
        
class booking_form(forms.ModelForm):
    class Meta:
        model = booking
        fields = '__all__'
        
class payment_form(forms.ModelForm):
    class Meta:
        model = models.payment
        fields = '__all__'        

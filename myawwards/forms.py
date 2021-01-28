from django import forms
from .models import Project,Profile
from django_registration.forms import RegistrationForm

    
class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['project_title', 'project_photo', 'bio','link']
        widgets = {
          'project_description': forms.Textarea(attrs={'rows':4, 'cols':10,}),
        }
        
class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']
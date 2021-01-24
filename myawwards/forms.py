from django import forms
from .models import Project,Profile
from django_registration.forms import RegistrationForm

    
class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        exclude = ['pub_date', 'Developer', 'developer_profile']
        widgets = {
          'project_description': forms.Textarea(attrs={'rows':4, 'cols':10,}),
        }
        
class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']
        widgets = {
          'bio': forms.Textarea(attrs={'rows':2, 'cols':10,}),
        }

        
        
        
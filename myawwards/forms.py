from django import forms
from .models import Image,Profile,Comment
from django_registration.forms import RegistrationForm

    
class NewProjectForm(forms.ModelForm):
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
        }]
    class Meta:
        model = Comment
        exclude = ['pub_date', 'developer']
        
class NewsLetterForm(forms.Form):
    your_name = forms.CharField(label='First Name',max_length=30)
    email = forms.EmailField(label='Email')
        
        
        
        
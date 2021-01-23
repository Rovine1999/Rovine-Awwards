from django import forms
from .models import Image,Profile,Comment
from django_registration.forms import RegistrationForm

    
class NewProjectForm(forms.ModelForm):
    class Meta:
        model = Image
        exclude = ['pub_date', 'Developer', 'developer_profile']
      
        
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['photo','bio']

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']
        
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ['pub_date', 'developer']
        
class NewsLetterForm(forms.Form):
    your_name = forms.CharField(label='First Name',max_length=30)
    email = forms.EmailField(label='Email')
        
        
        
        
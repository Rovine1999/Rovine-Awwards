from django.db import models
import datetime as dt
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Create your models here.

class Project(models.Model):
    project_title = models.CharField(max_length=255)
    project_photo = CloudinaryField('images')
    project_description = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
    link = models.URLField()
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
   
    
    def save_profile(self):
        self.save()
        
    def delete_profile(self):
        self.delete()

     
    @classmethod
    def search_projects(cls, search_term):
        projects = cls.objects.filter(project_title__icontains=search_term)
        return projects
    
    
    @classmethod
    def get_by_author(cls, author):
        projects = cls.objects.filter(author=author)
        return projects
    
    
    @classmethod
    def get_project(request, id):
        try:
            project = Projects.objects.get(pk = id)
            
        except ObjectDoesNotExist:
            raise Http404()
        
        return project
    
    def __str__(self):
        return self.project_title
    
    

        

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    photo = CloudinaryField('profile_pics/', blank=True)

    def save_profile(self):
        self.save()                   

    def delete_profile(self):
        self.delete()
    
    def __str__(self):
        return self.bio


        
    
    
    
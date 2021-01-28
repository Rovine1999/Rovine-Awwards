from django.shortcuts import render,redirect,get_object_or_404
from django.http  import HttpResponse,Http404,HttpResponseRedirect
import datetime as dt
from django.contrib.auth.decorators import login_required
from .models import Project,Profile
from .forms import ProjectForm,RegistrationForm,ProfileUpdateForm
from django.views.generic import (ListView,DetailView,CreateView,UpdateView,DeleteView)

# Create your views here.


@login_required
def awwards(request):
    images = Project.objects.all()
   
        
    return render(request, 'awwards.html',{'images':images})

def register(request):
    if request.method=="POST":
        form=RegistrationForm(request.POST)
        profileForm=ProjectForm(request.POST, request.FILES)
        if form.is_valid() and profileForm.is_valid():
            username=form.cleaned_data.get('username')
            user=form.save()
            profile=profileForm.save(commit=False)
            profile.user=user
            profile.save()
            messages.success(request, f'Successfully created Account!.You can now login as {username}!')
            return redirect('login')
    else:
        form= RegistrationForm()
        profileForm=ProjectForm()
    context={
        'form':form,
        'profileForm': profileForm
    }
    return render(request, 'registration/registration.html', context)



def awwards(request):
    current_user = request.user
    if request.method == 'POST':
        form =ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.user = current_user
            project.save()
        return redirect('home')

    else:
        form =ProjectForm()
    return render(request, 'awwards.html', {"form":form})





@login_required(login_url='/accounts/login/')
def profile(request):
    current_user = request.user
    developer = current_user
    project = Project.get_by_developer(developer)
    
    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.photo)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.save()
        return redirect('profile')
        
    else:
        form = ProfileUpdateForm()    
    return render(request, 'django_registration/profile.html', {"form":form, "project":project})


@login_required(login_url='/accounts/login/')
def search_awward(request):
    if 'keyword' in request.GET and request.GET["keyword"]:
        search_term = request.GET.get("keyword")
        searched_awward = Project.search_awward(search_term)
        message = f"{search_term}"

        return render(request, 'search.html', {"message":message,"project": searched_awward})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html', {"message": message})





class PostListView(ListView):
    model = Project
    template_name = 'index.html'
    context_object_name = 'posts'
    ordering = ['-pub_date']
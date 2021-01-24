from django.shortcuts import render,redirect,get_object_or_404
from django.http  import HttpResponse,Http404,HttpResponseRedirect
import datetime as dt
from django.contrib.auth.decorators import login_required

# Create your views here.
def register(request):
    if request.method=="POST":
        form=RegistrationForm(request.POST)
        profileForm=ProfileForm(request.POST, request.FILES)
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
        profileForm=ProfileForm()
    context={
        'form':form,
        'profileForm': profileForm
    }
    return render(request, 'registration/registration.html', context)



@login_required
def profile(request):
    if request.method == 'POST':
        useForm=UserUpdateForm(request.POST, instance=request.user)
        profileForm=ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if useForm.is_valid() and profileForm.is_valid():
            useForm.save()
            profileForm.save()
            messages.success(request, f'Your account has been updated!')
        return redirect('profile')
    else:
        useForm=UserUpdateForm(instance=request.user.profile)
        profileForm=ProfileUpdateForm(instance=request.user.profile)
    context={
        'useForm':useForm,
        'profileForm':profileForm
    }
    return render(request, 'registration/profile.html', context)
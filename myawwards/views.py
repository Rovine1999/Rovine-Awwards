from django.shortcuts import render

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
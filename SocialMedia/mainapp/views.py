from django.shortcuts import render, redirect
from . import models
from django.urls import reverse, reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView



class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = "registration/signup.html"


def base(request):
    return render(request,'base.html')

@login_required(login_url="/login")
def profileCreate(request):
    check = models.Profile.objects.filter(username=request.user)
    if check:
        return redirect(reverse('mainapp:base'))
    else:
        if request.POST:  
            profile_image=request.POST["profile_image"]
            cover_image = request.POST["cover_image"]
            email=request.POST["email"]
            age=request.POST["age"]
            info=request.POST["info"]
            models.Profile.objects.create(username=request.user, profile_image=profile_image, cover_image=cover_image, email=email, age=age, info=info)
            return redirect(reverse('mainapp:base'))
        else:
            return render(request, 'registration/profilecreation.html')

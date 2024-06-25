from django.shortcuts import render, redirect
from . import models
from django.urls import reverse, reverse_lazy
from django.contrib.auth.decorators import login_required, user_passes_test
from django.utils.decorators import method_decorator
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView


def not_logged_in(user):
    return not user.is_authenticated

class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = "registration/signup.html"

    @method_decorator(user_passes_test(not_logged_in, redirect_field_name=None, login_url="/"))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


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

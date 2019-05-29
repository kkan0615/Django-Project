from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from .forms import SiteUserCreationForm

class SignUp(generic.CreateView):
    form_class = SiteUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

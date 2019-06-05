from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views import generic
from .models import SiteUser
from django.contrib.auth.decorators import login_required

from .forms import SiteUserCreationForm

class SignUp(generic.CreateView):
    form_class = SiteUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

@login_required
def mypage(request, username):
    user = get_object_or_404(SiteUser, username=username)
    return render(request, 'mypage.html', {'user': user})
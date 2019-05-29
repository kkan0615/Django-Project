from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import SiteUser

class SiteUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = SiteUser
        fields = ('username', 'email', 'nickname')

class SiteUserChangeForm(UserChangeForm):

    class Meta:
        model = SiteUser
        fields = ('username', 'email', 'nickname')
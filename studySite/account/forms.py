from django import forms
from django.contrib.auth.forms import UserCreationForm as oldCreationForm
from django.contrib.auth.forms import UserChangeForm as oldChangeForm
from .models import User

class UserCreationForm(oldCreationForm):

    class Meta(oldCreationForm):
        model = User
        fields = ('username', 'email', 'nickname')

class UserChangeForm(oldChangeForm):

    class Meta:
        model = User
        fields = ('username', 'email', 'nickname')
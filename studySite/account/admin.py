from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin as oldUserAdmin

from .forms import UserCreationForm, UserChangeForm
from .models import User

class UserAdmin(oldUserAdmin):
    add_form = UserCreationForm
    form = UserChangeForm
    model = User
    list_display = ['email', 'username', 'nickname']

admin.site.register(User, UserAdmin)
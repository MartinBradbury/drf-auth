from django.contrib import admin
from .models import CustomUserAuth
from .forms import *
from django.contrib.auth.admin import UserAdmin

@admin.register(CustomUserAuth)
class CustomAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    
    model = CustomUserAuth
    

from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUserAuth

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        models = CustomUserAuth
        fields = ["email",]
        
class CustomUserChangeForm(UserChangeForm):
    class Meta:
        models = CustomUserAuth
        fields =["email",]
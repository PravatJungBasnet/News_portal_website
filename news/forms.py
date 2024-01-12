from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User,news

class signupform(UserCreationForm):
    class Meta:
        model=User
        fields=['username','email','password1','password2']
class newsform(forms.ModelForm):
    class Meta:
        model=news
        fields=['category','title','image','description']
from django.contrib.auth.models import User
from django import forms

class UserForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput )
# class meta is for having model of userform
    class Meta:
        model=User
        fields=['username','email','password']


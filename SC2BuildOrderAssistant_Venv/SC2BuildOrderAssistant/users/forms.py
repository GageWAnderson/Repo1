from django import forms
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django.views.generic.edit import UpdateView
from .models import Profile

#Create a form that inherits from UserCreationForm
#In order to register these new classes in the database
#There needs to be a meta class

class UserRegisterForm(UserCreationForm):
    #Special Registration form that inherits from
    #The django default class UserCreationForm

    #This inherited class simply adds an email field
    email = forms.EmailField()

    def save(self, *args, **kwargs):
        super().save(*args,**kwargs)

    #This class gives a nested namespace for configurations
    #Keeps configurations in one place
    class Meta:
        #In Meta, you specify the DB model that you want this
        #Form to interact with (model = User)
        model = User

        #These are the fields that you want to show on the 
        #Form
        fields = ['username', 'email', 'password1','password2']

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username','email']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']
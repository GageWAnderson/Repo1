from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

#Create a form that inherits from UserCreationForm
#In order to register these new classes in the database
#There needs to be a meta class

class UserRegisterForm(UserCreationForm):
    #Special Registration form that inherits from
    #The django default class UserCreationForm

    #This inherited class simply adds an email field
    email = forms.EmailField()

    #This class gives a nested namespace for configurations
    #Keeps configurations in one place
    class Meta:
        #In Meta, you specify the DB model that you want this
        #Form to interact with (model = User)
        model = User

        #These are the fields that you want to show on the 
        #Form
        fields = ['username', 'email', 'password1','password2']
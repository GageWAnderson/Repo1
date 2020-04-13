from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from .forms import UserRegisterForm

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save() #Save the user to the database
            username = form.cleaned_data.get('username')
            #send a 1-time message to the template
            #That registration was successful!
            messages.success(request, f'Account creation for {username} successful!')
            #Next, re-direct user back to the homepage
            return redirect('forum-home')

    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html',{'form':form})


class AccountView(LoginRequiredMixin,TemplateView):
    template_name = "users/account_management.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        #Context here should include classes from the user object
        #(Model) you made in the database 

        return context


class AccountUpdateView(LoginRequiredMixin,TemplateView):
    template_name = "users/account_update.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        #Context here should include classes from the user object
        #(Model) you made in the database 

        return context
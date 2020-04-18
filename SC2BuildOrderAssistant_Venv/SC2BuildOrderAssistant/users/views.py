from django.shortcuts import render, redirect
from django.http import HttpResponse
from . models import Profile, User
from django.urls import reverse, reverse_lazy
from django.views.generic.base import TemplateView
from django.views.generic.edit import UpdateView, FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from . forms import UserUpdateForm, ProfileUpdateForm, UserRegisterForm

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
            return redirect('account-login')

    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html',{'form':form})


class AccountView(LoginRequiredMixin,TemplateView):
    template_name = "users/account_management.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        return context

class UserUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'users/account_update_form.html'
    model = User
    form = UserUpdateForm
    fields = ['username','email']
    success_url = reverse_lazy('forum-home')
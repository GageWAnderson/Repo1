from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Build

#Use some kind of user mixin to add different options
#To what the context dictionary passes into ForumView
class ForumView(TemplateView):
    template_name = "forum/forum_home.html"
    model = Build
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        #Add additional content fields to be displayed on
        #The home page
        #Bug is Post.objects.all(), can't query this table
        #Since it's empty an hasn't been created yet!
        context['builds'] = Build.objects.all()
        return context

#When you make a view for all posts for a given matchup, use this .filter method
#On Build.objects.filter(matchup = 'PvZ')
# queryset = Book.objects.filter(publisher__name='ACME Publishing')

#Use the LoginRequiredMixin to only show this page to users
#That are logged in
class AccountView(LoginRequiredMixin,TemplateView):
    template_name = "account_management.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        #Add additional content fields to be displayed on
        #The home page
        # context['latest_articles'] = Placeholder
        return context

    #Define register,email,profile update forms here

class BuildsView(AccountView):
    template_name = "account_management.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        #Add additional content fields to be displayed on
        #The home page
        # context['latest_articles'] = Placeholder
        return context

    #Define register,email,profile update forms here
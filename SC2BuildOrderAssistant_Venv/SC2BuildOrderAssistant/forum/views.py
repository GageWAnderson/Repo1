from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.base import TemplateView

# Create your views here.

class ForumView(TemplateView):
    template_name = "forum_home.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        #Add additional content fields to be displayed on
        #The home page
        # context['latest_articles'] = Placeholder
        return context
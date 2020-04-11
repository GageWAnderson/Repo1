from django.urls import path
from .views import ForumView


urlpatterns = [
    path('',ForumView.as_view(), name='forum-home'),
    path('forum/',ForumView.as_view(), name='forum-home')
]
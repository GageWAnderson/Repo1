from django.urls import path
from .views import ForumView, AccountView
# from .views import (
#     PostListView,
#     PostDetailView,
#     PostCreateView,
#     PostUpdateView,
#     PostDeleteView,
#     UserPostListView
# )
from django.urls import path, include
import users

#Views for managing how users interact with the forum are located
#In blog/views - GOAL: make custom views based on class-based views
#In order to change the forum based on the user
urlpatterns = [
    path('',ForumView.as_view(), name='forum-home'),
    path('matchups/',ForumView.as_view(), name='forum-matchups'),
    path('new_post/',ForumView.as_view(), name='forum-new-post'),
    path('users/',include('users.urls')),
]
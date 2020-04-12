from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.AccountView.as_view(),name='account-home'),
    path('register/',views.register,name='account-register'),
    path('builds/',views.AccountView.as_view(), name='account-builds'),
]
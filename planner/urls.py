"""Projekt_koncowy URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from planner import views

urlpatterns = [
    path('add_task/', views.AddTaskView.as_view(), name='add_task'),
    path('all_tasks/', views.ShowAllTasks.as_view(), name='show_all_tasks'),
    path('all_events/', views.ShowAllEvents.as_view(), name='show_all_events'),
    path('add_event/', views.AddEventView.as_view(), name='add_event'),
    path('daily_planner/', views.UserDailyPlanner.as_view(), name='daily_planner'),
    path('manage_tags/', views.ManageTags.as_view(), name='manage_tags'),
    path('update_tag/<int:pk>/', views.UpdateTag.as_view(), name='update_tag'),
    path('delete_tag/<int:pk>/', views.DeleteTagView.as_view(), name='delete_tag'),
]

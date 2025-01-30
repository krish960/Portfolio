"""
URL configuration for Portfolio project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from website import views
from anmins import views as adminss

urlpatterns = [
    path('',views.index),
    path('7823040317/',adminss.home),
    path('admin/IMG/',adminss.IMG),
    path('admin/save_img/',adminss.save_img),
    path('admin/About/',adminss.About),
    path('admin/save_about/',adminss.save_about),
    path('admin/delete_rec/',adminss.delete_rec),
    path('admin/delete_img/',adminss.delete_img),
    path('admin/about_me/',adminss.about_me),
    path('admin/delete_Desc/',adminss.delete_Desc),
    path('admin/save_about_me/',adminss.save_about_me),
    path('admin/About_info/',adminss.About_info),
    path('admin/save_about_info/',adminss.save_about_info),
    path('admin/delete_about_info/',adminss.delete_about_info),
    path('admin/Resume/',adminss.Resume),
    path('admin/save_Resume_link/',adminss.save_Resume_link),
    path('admin/delete_Resume/',adminss.delete_Resume),
    path('admin/Experience/',adminss.Experience),
    path('admin/save_Experience/',adminss.save_Experience),
    path('admin/delete_experience/',adminss.delete_experience),
    path('admin/Education/',adminss.Education),
    path('admin/save_Education/',adminss.save_Education),
    path('admin/delete_Education/',adminss.delete_Education),
    path('admin/Projects/',adminss.Projects),
    path('admin/save_Projects/',adminss.save_Projects),
    path('admin/delete_Projects/',adminss.delete_Projects),

]

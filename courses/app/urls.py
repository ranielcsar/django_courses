"""
URL configuration for app project.

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
from teacher.views import home, create_new_course, edit_course, delete_course
from login.views import signup, register_user, login_view
from student.views import home as student_home

urlpatterns = [
    path(
        "admin/",
        admin.site.urls,
    ),
    path(
        "",
        login_view,
        name="login",
    ),
    path(
        "cadastrar/",
        signup,
        name="cadastrar",
    ),
    path(
        "register_user/",
        register_user,
        name="register_user",
    ),
    path(
        "home/",
        home,
        name="home",
    ),
    path(
        "student_home/",
        student_home,
        name="student_home",
    ),
    path(
        "new-course/",
        create_new_course,
        name="new-course",
    ),
    path(
        "edit-course/<uuid:id>/",
        edit_course,
        name="edit-course",
    ),
    path(
        "delete-course/<uuid:id>/",
        delete_course,
        name="delete-course",
    ),
]

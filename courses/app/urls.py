from django.contrib import admin
from django.urls import include, path
from login.views import logout

urlpatterns = [
    path(
        "admin/",
        admin.site.urls,
    ),
    path("", include("login.urls")),
    path("teacher/", include("teacher.urls")),
    path("student/", include("student.urls")),
    path(
        "logout/",
        logout,
        name="logout",
    ),
]

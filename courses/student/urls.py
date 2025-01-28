from django.urls import path

from .views import home, buy_course

urlpatterns = [
    path(
        "",
        home,
        name="student_home",
    ),
    path(
        "buy-course/<slug:slug>/",
        buy_course,
        name="buy-course",
    ),
]

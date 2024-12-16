from django.urls import path

from .views import (
    home,
    create_new_course,
    edit_course,
    delete_course,
)

urlpatterns = [
    path(
        "",
        home,
        name="teacher_home",
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

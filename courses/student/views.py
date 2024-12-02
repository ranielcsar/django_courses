from django.contrib.auth.decorators import login_required
from django.http import HttpRequest
from django.shortcuts import render
from teacher.models import Course, StatusEnum


@login_required
def home(request: HttpRequest):
    courses = Course.objects.filter(status=StatusEnum.ACTIVE.value)

    return render(
        request,
        "index.html",
        {
            "student": request.user,
            "courses": courses,
        },
    )

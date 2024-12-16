from decimal import Decimal
from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpRequest, HttpResponse

from .models import Course
from login.models import User


def get_course_values(request: HttpRequest):
    name = request.POST.get("name")
    category = request.POST.get("category")
    status = request.POST.get("status")
    price = request.POST.get("price")

    return (
        name,
        category,
        status,
        price,
    )


def create_new_course(request: HttpRequest):
    if request.method == "POST":
        (
            name,
            category,
            status,
            price,
        ) = get_course_values(request)
        try:
            course = Course.create(
                name=name,
                category=category,
                status=status,
                teacher=request.user,
                price=Decimal(price.replace(",", ".")),
            )
            if course:
                for lesson_data in zip(
                    request.POST.getlist("lessons[][name]"),
                    request.POST.getlist("lessons[][url]"),
                ):
                    name, url = lesson_data
                    course.lessons.create(name=name, youtube_url=url, course=course)
                return redirect("/home")
        except Exception as e:
            return HttpResponse(f"Erro ao criar o curso: {str(e)}", status=500)
    return render(request, "new_course.html")


def edit_course(request: HttpRequest, id: str):
    course = get_object_or_404(Course, id=id)

    if request.method == "POST":
        (
            name,
            category,
            status,
            price,
        ) = get_course_values(request)
        course.lessons.all().delete()

        try:
            course.name = name
            course.category = category
            course.status = status
            course.price = price
            course.save()

            for lesson_data in zip(
                request.POST.getlist("lessons[][name]"),
                request.POST.getlist("lessons[][url]"),
            ):
                name, url = lesson_data
                course.lessons.create(name=name, youtube_url=url, course=course)

            return redirect("/home")
        except Exception as e:
            return HttpResponse(f"Erro ao editar o curso: {str(e)}", status=500)

    context = {
        "course": course,
        "lessons": course.lessons.all(),
    }
    return render(request, "edit_course.html", context)


def delete_course(request: HttpRequest, id: str):
    course = get_object_or_404(Course, id=id)
    course.delete()

    return redirect("/")


def get_courses(request: HttpRequest):
    courses = Course.objects.all()

    return courses


def home(request: HttpRequest):
    courses = get_courses(request)
    return render(request, "teacher_home.html", {"courses": courses})

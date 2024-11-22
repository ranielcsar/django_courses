from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpRequest, HttpResponse

from .models import Course


def get_course_values(request: HttpRequest):
    name = request.POST.get("name")
    category = request.POST.get("category")
    status = request.POST.get("status")

    return (
        name,
        category,
        status,
    )


def create_new_course(request: HttpRequest):
    if request.method == "POST":
        (name, category, status) = get_course_values(request)

        try:
            course = Course.create(
                name=name,
                category=category,
                status=status,
            )
            course.save()

            for lesson_data in zip(
                request.POST.getlist("lessons[][name]"),
                request.POST.getlist("lessons[][url]"),
            ):
                name, url = lesson_data
                course.lessons.create(name=name, youtube_url=url, course=course)

            return redirect("/")
        except Exception as e:
            return HttpResponse(f"Erro ao criar o curso: {str(e)}", status=500)
    return render(request, "new_course.html")


def edit_course(request: HttpRequest, id: str):
    course = get_object_or_404(Course, id=id)

    if request.method == "POST":
        (name, category, status) = get_course_values(request)
        course.lessons.all().delete()

        try:
            course.name = name
            course.category = category
            course.status = status
            course.save()

            for lesson_data in zip(
                request.POST.getlist("lessons[][name]"),
                request.POST.getlist("lessons[][url]"),
            ):
                name, url = lesson_data
                course.lessons.create(name=name, youtube_url=url, course=course)

            return redirect("/")
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


def home(request: HttpRequest):
    courses = Course.objects.all()

    return render(request, "home.html", {"courses": courses})

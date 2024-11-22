from django.db import models
import uuid
from enum import Enum


class CategoryEnum(Enum):
    FRONTEND = "frontend"
    BACKEND = "backend"


class StatusEnum(Enum):
    ACTIVE = "ativo"
    INACTIVE = "inativo"


class Lesson(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )
    name = models.CharField(max_length=255)
    youtube_url = models.URLField(max_length=500)
    course = models.ForeignKey(
        "Course",
        on_delete=models.CASCADE,
        related_name="lesson_set",
        null=True,
        blank=True,
    )

    @classmethod
    def create(cls, name, youtube_url, course):
        return cls.objects.create(
            name=name,
            youtube_url=youtube_url,
            course=course,
        )


class Course(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )
    name = models.CharField(max_length=255)
    category = models.CharField(
        max_length=50,
        choices=[(tag.name, tag.value) for tag in CategoryEnum],
    )
    status = models.CharField(
        max_length=50,
        choices=[(tag.name, tag.value) for tag in StatusEnum],
    )
    lessons = models.ManyToManyField("Lesson", blank=True, related_name="courses")

    @classmethod
    def create(cls, name, category, status, lessons=None):
        course = cls(
            name=name,
            category=category,
            status=status,
        )
        course.save()
        if lessons:
            course.lessons.set(lessons)
        return course

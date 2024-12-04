import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser


class Role(models.TextChoices):
    ADMIN = "ADMIN", "Admin"
    TEACHER = "TEACHER", "Teacher"
    STUDENT = "STUDENT", "Student"


class User(AbstractUser):
    role = models.CharField(max_length=50, choices=Role.choices)

    def save(self, *args, **kwargs):
        if not self.pk:
            return super().save(*args, **kwargs)

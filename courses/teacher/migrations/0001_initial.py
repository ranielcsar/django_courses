# Generated by Django 5.1.3 on 2024-11-29 14:45

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('category', models.CharField(choices=[('FRONTEND', 'frontend'), ('BACKEND', 'backend')], max_length=50)),
                ('status', models.CharField(choices=[('ACTIVE', 'ativo'), ('INACTIVE', 'inativo')], max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('youtube_url', models.URLField(max_length=500)),
                ('course', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='lesson_set', to='teacher.course')),
            ],
        ),
        migrations.AddField(
            model_name='course',
            name='lessons',
            field=models.ManyToManyField(blank=True, related_name='courses', to='teacher.lesson'),
        ),
    ]

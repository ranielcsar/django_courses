# Generated by Django 5.1.3 on 2024-12-04 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0002_alter_user_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]

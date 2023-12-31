# Generated by Django 4.2.5 on 2023-09-17 14:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("department_module", "0001_initial"),
        ("school_module", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Teacher",
            fields=[
                (
                    "teacher_id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                        unique=True,
                    ),
                ),
                ("phone_number", models.CharField(max_length=255)),
                ("date_of_birth", models.DateField()),
                ("gender", models.CharField(max_length=255)),
                ("license_number", models.CharField(max_length=255)),
                ("licence_expiry_date", models.DateField()),
                ("licence_issue_date", models.DateField()),
                (
                    "licence_certificate",
                    models.ImageField(upload_to="teacher_licence_certificate"),
                ),
                ("street_address", models.CharField(max_length=255)),
                ("city", models.CharField(max_length=255)),
                ("state", models.CharField(max_length=255)),
                ("country", models.CharField(max_length=255)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "department",
                    models.ManyToManyField(
                        related_name="teachers", to="department_module.department"
                    ),
                ),
                (
                    "school",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="school_module.school",
                    ),
                ),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]

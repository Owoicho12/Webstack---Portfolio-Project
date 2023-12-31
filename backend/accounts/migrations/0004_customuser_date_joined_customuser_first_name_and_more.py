# Generated by Django 4.2.5 on 2023-09-14 00:21

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):
    dependencies = [
        ("accounts", "0003_alter_customuser_role"),
    ]

    operations = [
        migrations.AddField(
            model_name="customuser",
            name="date_joined",
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name="customuser",
            name="first_name",
            field=models.CharField(default="abiola", max_length=150),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="customuser",
            name="is_active",
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name="customuser",
            name="is_superuser",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="customuser",
            name="last_name",
            field=models.CharField(default="adedayo", max_length=150),
            preserve_default=False,
        ),
    ]

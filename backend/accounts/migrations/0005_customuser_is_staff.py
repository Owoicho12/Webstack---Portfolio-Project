# Generated by Django 4.2.5 on 2023-09-14 00:24

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("accounts", "0004_customuser_date_joined_customuser_first_name_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="customuser",
            name="is_staff",
            field=models.BooleanField(default=True),
        ),
    ]

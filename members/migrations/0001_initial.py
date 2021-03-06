# Generated by Django 4.0.2 on 2022-02-04 23:27

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Member",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("f_name", models.CharField(max_length=100)),
                ("l_name", models.CharField(max_length=100)),
                ("email", models.EmailField(max_length=254)),
                (
                    "phone_number",
                    models.CharField(
                        max_length=15,
                        unique=True,
                        validators=[
                            django.core.validators.RegexValidator(
                                regex="^\\+?1?\\d{8,15}$"
                            )
                        ],
                    ),
                ),
                (
                    "role",
                    models.CharField(
                        choices=[
                            ("Admin", "Can delete members"),
                            ("Regular", "Can't delete members"),
                        ],
                        default="Regular",
                        max_length=7,
                    ),
                ),
            ],
        ),
    ]

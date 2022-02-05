# Generated by Django 4.0.2 on 2022-02-05 21:24

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("members", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="member",
            name="phone_number",
            field=models.CharField(
                max_length=15,
                unique=True,
                validators=[
                    django.core.validators.RegexValidator(
                        regex="^\\d{3}-?\\d{3}-?\\d{4}$"
                    )
                ],
            ),
        ),
    ]

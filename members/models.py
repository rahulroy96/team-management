from django.db import models
from django.core.validators import RegexValidator


class Member(models.Model):

    f_name = models.CharField(max_length=100)
    l_name = models.CharField(max_length=100)
    email = models.EmailField()

    # TODO: Improve the regex
    phone_number_regex = RegexValidator(
        regex=r"^\d{3}-?\d{3}-?\d{4}$"
    )  # allows only US styled phone numbers
    phone_number = models.CharField(
        validators=[phone_number_regex], max_length=15, unique=True
    )

    class Role(models.TextChoices):
        ADMIN = "Admin", "Can delete members"
        REGULAR = "Regular", "Can't delete members"

    role = models.CharField(
        max_length=7,
        choices=Role.choices,
        default=Role.REGULAR,
    )

    def is_admin(self):
        return self.role == self.Role.ADMIN

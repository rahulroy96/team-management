from django.db import models
from django.core.validators import RegexValidator


class Member(models.Model):

    name_regex = RegexValidator(regex=r"^[A-Za-z ]+$")
    f_name = models.CharField(
        max_length=100,
        validators=[name_regex],
        verbose_name="First Name",
    )
    l_name = models.CharField(
        max_length=100,
        validators=[name_regex],
        verbose_name="Last Name",
    )
    email = models.EmailField()

    # TODO: Improve the regex
    phone_number_regex = RegexValidator(
        regex=r"^\d{3}-?\d{3}-?\d{4}$"
    )  # allows only US styled phone numbers
    phone_number = models.CharField(
        validators=[phone_number_regex], max_length=15, unique=True, verbose_name="Phone Number",
    )

    class Role(models.TextChoices):
        ADMIN = "Admin", "Admin - Can delete members"
        REGULAR = "Regular", "Regular - Can't delete members"

    role = models.CharField(
        max_length=7,
        choices=Role.choices,
        default=Role.REGULAR,
        verbose_name="Role",
    )

    def is_admin(self):
        return self.role == self.Role.ADMIN

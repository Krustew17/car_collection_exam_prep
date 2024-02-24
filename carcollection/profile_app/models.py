from django.core.validators import MinValueValidator, MaxValueValidator, MinLengthValidator
from django.db import models


# Create your models here.

class ProfileModel(models.Model):
    MAX_USERNAME_LENGTH = 10
    MIN_USERNAME_LENGTH = 2
    MIN_USERNAME_MESSAGE = "The username must be a minimum of 2 chars"

    MIN_AGE = 18

    MAX_PASSWORD_LENGTH = 30

    MAX_FIRSTNAME_LENGTH = 30

    MAX_LASTNAME_LENGTH = 30

    username = models.CharField(
        null=False,
        blank=False,
        max_length=MAX_USERNAME_LENGTH,
        validators=(
            MinLengthValidator(MIN_USERNAME_LENGTH, message=MIN_USERNAME_MESSAGE),
        )
    )

    email = models.EmailField(
        null=False,
        blank=False
    )

    age = models.IntegerField(
        null=False,
        blank=False,
        validators=(
            MinValueValidator(MIN_AGE),
        )
    )

    password = models.CharField(
        null=False,
        blank=False,
        max_length=MAX_PASSWORD_LENGTH,
    )

    first_name = models.CharField(
        null=False,
        blank=True,
        max_length=MAX_FIRSTNAME_LENGTH,
    )

    last_name = models.CharField(
        null=False,
        blank=True,
        max_length=MAX_LASTNAME_LENGTH,
    )

    profile_picture = models.URLField(
        null=False,
        blank=True,
    )

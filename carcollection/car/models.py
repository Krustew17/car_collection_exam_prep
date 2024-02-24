from django.core.validators import MinLengthValidator, MinValueValidator, MaxValueValidator
from django.db import models


# Create your models here.
class CarModel(models.Model):
    TYPE_MAX_LENGTH = 10

    SPORTS_CAR = "Sports Car"
    PICKUP = "Pickup"
    CROSSOVER = "Crossover"
    MINIBUS = "Minibus"
    OTHER = "Other"

    TYPE_CHOICES = (
        (SPORTS_CAR, SPORTS_CAR),
        (PICKUP, PICKUP),
        (CROSSOVER, CROSSOVER),
        (MINIBUS, MINIBUS),
        (OTHER, OTHER),
    )

    MAX_MODEL_LENGTH = 21
    MIN_MODEL_LENGTH = 2

    MIN_YEAR = 1980
    MAX_YEAR = 2049
    YEAR_VALIDATION_MESSAGE = "Year must be between 1980 and 2049"

    MIN_CAR_PRICE = 1

    type = models.CharField(
        max_length=TYPE_MAX_LENGTH,
        choices=TYPE_CHOICES,
        null=False,
        blank=False,
    )

    car_model = models.CharField(
        null=False,
        blank=False,
        max_length=MAX_MODEL_LENGTH,
        validators=(
            MinLengthValidator(MIN_MODEL_LENGTH),
        )
    )

    year = models.IntegerField(
        null=False,
        blank=False,
        validators=(
            MinValueValidator(MIN_YEAR, message=YEAR_VALIDATION_MESSAGE),
            MaxValueValidator(MAX_YEAR, message=YEAR_VALIDATION_MESSAGE),
        )
    )

    image_url = models.URLField(
        null=False,
        blank=False,
    )

    price = models.FloatField(
        null=False,
        blank=False,
        validators=(
            MinValueValidator(MIN_CAR_PRICE),
        )
    )


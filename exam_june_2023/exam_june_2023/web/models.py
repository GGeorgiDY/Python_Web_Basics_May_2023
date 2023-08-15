from django.core import validators, exceptions
from django.db import models


def first_char_must_be_letter(value):
    first_char = value[0]
    if not first_char.isalnum():
        raise exceptions.ValidationError("Your name must start with a letter!")


def validate_fruit_name_contains_only_letters(value):
    for ch in value:
        if not ch.isalnum():
            raise exceptions.ValidationError("Fruit name should contain only letters!")


class Profile(models.Model):
    MAX_LEN_FIRST_NAME = 25
    MIN_LEN_FIRST_NAME = 2
    MAX_LEN_LAST_NAME = 35
    MIN_LEN_LAST_NAME = 1
    MAX_LEN_EMAIL = 40
    MAX_LEN_PASSWORD = 20
    MIN_LEN_PASSWORD = 8

    first_name = models.CharField(
        max_length=MAX_LEN_FIRST_NAME,
        validators=(
            validators.MinLengthValidator(MIN_LEN_FIRST_NAME),
            first_char_must_be_letter,
        ),
        # required
        null=False,
        blank=False,
    )

    last_name = models.CharField(
        max_length=MAX_LEN_LAST_NAME,
        validators=(
            validators.MinLengthValidator(MIN_LEN_LAST_NAME),
            first_char_must_be_letter,
        ),
        # required
        null=False,
        blank=False,
    )

    email = models.EmailField(
        max_length=MAX_LEN_EMAIL,
        # required
        null=False,
        blank=False,
    )

    password = models.CharField(
        max_length=MAX_LEN_PASSWORD,
        validators=(
            validators.MinLengthValidator(MIN_LEN_PASSWORD),
        ),
        # required
        null=False,
        blank=False,
    )

    image_url = models.URLField(
        # optional
        null=True,
        blank=True,
    )

    age = models.PositiveIntegerField(
        default=18,
        # optional
        null=True,
        blank=True,
    )


class Fruit(models.Model):
    MAX_LEN_FRUIT = 30
    MIN_LEN_FRUIT = 2

    fruit_name = models.CharField(
        max_length=MAX_LEN_FRUIT,
        validators=(
            validators.MinLengthValidator(MIN_LEN_FRUIT),
            validate_fruit_name_contains_only_letters,
        ),
        # required
        null=False,
        blank=False,
    )

    image_url = models.URLField(
        # required
        null=False,
        blank=False,
    )

    description = models.TextField(
        # required
        null=False,
        blank=False,
    )

    nutrition = models.TextField(
        # optional
        null=True,
        blank=True,
    )
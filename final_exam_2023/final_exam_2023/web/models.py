from django.core import validators, exceptions
from django.db import models


def validate_field_starts_with_letter(value):
    first_character = value[0]
    if not first_character.isalpha():
        raise exceptions.ValidationError("Your name must start with a letter!")


def validate_only_alphanumeric(value):
    for ch in value:
        if not ch.isalpha():
            raise exceptions.ValidationError("Fruit name should contain only letters!")


class ProfileModel(models.Model):
    FIRST_NAME_MAX_CHARS = 25
    FIRST_NAME_MIN_CHARS = 2
    LAST_NAME_MAX_CHARS = 35
    LAST_NAME_MIN_CHARS = 1
    EMAIL_LENGTH = 40
    PASSWORD_MAX_LENGTH = 20
    PASSWORD_MIM_LENGTH = 8

    first_name = models.CharField(
        max_length=FIRST_NAME_MAX_CHARS,
        validators=(
            validators.MinLengthValidator(FIRST_NAME_MIN_CHARS),
            validate_field_starts_with_letter,
        ),

        # понеже по условие трябва да е required пишем
        null=False,
        blank=False,
    )

    last_name = models.CharField(
        max_length=LAST_NAME_MAX_CHARS,
        validators=(
            validators.MinLengthValidator(LAST_NAME_MIN_CHARS),
            validate_field_starts_with_letter,
        ),

        # понеже по условие трябва да е required пишем
        null=False,
        blank=False,
    )

    email = models.EmailField(
        max_length=EMAIL_LENGTH,

        # понеже по условие трябва да е required пишем
        null=False,
        blank=False,
    )

    password = models.CharField(
        max_length=PASSWORD_MAX_LENGTH,
        validators=(
            validators.MinLengthValidator(PASSWORD_MIM_LENGTH),
        ),

        # понеже по условие трябва да е required пишем
        null=False,
        blank=False,
    )

    image_url = models.URLField(
        null=True,
        blank=True,
    )

    age = models.PositiveIntegerField(
        default= 18,
        null=True,
        blank=True,
    )


class FruitModel(models.Model):
    FRUIT_NAME_MAX_CHARS = 25
    FRUIT_NAME_MIN_CHARS = 2

    name = models.CharField(
        max_length=FRUIT_NAME_MAX_CHARS,
        validators=(
            validators.MinLengthValidator(FRUIT_NAME_MIN_CHARS),
            validate_only_alphanumeric,
        ),

        # понеже по условие трябва да е required пишем
        null=False,
        blank=False,
    )

    image_url = models.URLField(
        null=False,
        blank=False,
    )

    description = models.TextField(
        null=False,
        blank=False,
    )

    nutrition = models.CharField(
        null=True,
        blank=True,
    )
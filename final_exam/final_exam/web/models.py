from django.core import exceptions, validators
from django.db import models
from django.utils import timezone


def validate_name_contains_only_letters(value):
    for ch in value:
        if not ch.isalpha():
            raise exceptions.ValidationError("The name should contain only letters!")


def password_contains_at_least_one_digit(value):
    digits = 0
    for ch in value:
        if ch.isdigit():
            digits += 1
    if digits == 0:
        raise exceptions.ValidationError("The password must contain at least 1 digit!")


def validate_date_not_in_past(value):
    if value < timezone.now().date():
        raise exceptions.ValidationError("The date cannot be in the past!")


class ProfileModel(models.Model):
    MAX_LEN_FIRST_NAME = 20
    MAX_LEN_LAST_NAME = 30
    MIN_LEN_LAST_NAME = 4
    MAX_LEN_EMAIL = 45
    MAX_LEN_PASSWORD = 20
    MIN_LEN_PASSWORD = 5

    first_name = models.CharField(
        max_length=MAX_LEN_FIRST_NAME,
        validators=(
            validate_name_contains_only_letters,
        ),
        # required
        null=False,
        blank=False,
    )

    last_name = models.CharField(
        max_length=MAX_LEN_LAST_NAME,
        validators=(
            validators.MinLengthValidator(MIN_LEN_LAST_NAME),
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

    profile_picture = models.URLField(
        # optional
        null=True,
        blank=True,
    )

    password = models.CharField(
        max_length=MAX_LEN_PASSWORD,
        validators=(
            validators.MinLengthValidator(MIN_LEN_PASSWORD),
            password_contains_at_least_one_digit,
        ),
        # required
        null=False,
        blank=False,
    )


class EventModel(models.Model):
    MAX_LEN_EVENT_NAME = 30
    MIN_LEN_EVENT_NAME = 2

    CATEGORY_CHOICES = (
        ("Sports", "Sports"),
        ("Festivals", "Festivals"),
        ("Conferences", "Conferences"),
        ("Performing Art", "Performing Art"),
        ("Concerts", "Concerts"),
        ("Theme Party", "Theme Party"),
        ("Other", "Other"),
    )

    event_name = models.CharField(
        max_length=MAX_LEN_EVENT_NAME,
        validators=(
            validators.MinLengthValidator(MIN_LEN_EVENT_NAME),
        ),
        # required
        null=False,
        blank=False,
    )

    category = models.CharField(
        max_length=50,
        choices=CATEGORY_CHOICES,
        # required
        null=False,
        blank=False,
    )

    description = models.TextField(
        # optional
        null=True,
        blank=True,
    )

    date = models.DateField(
        validators=(
            validate_date_not_in_past,
        ),
        # validators=[],
        # required
        null=False,
        blank=False,
    )

    event_image = models.URLField(
        # required
        null=False,
        blank=False,
    )

    # def clean(self):
    #     if self.date < timezone.now().date():
    #         raise ValidationError("The date cannot be in the past!")

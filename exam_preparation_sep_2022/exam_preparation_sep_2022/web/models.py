from django.core import validators, exceptions
from django.db import models


def validate_only_alphanumeric(value):
    for ch in value:
        if not ch.isalnum() and ch != '_':
            raise exceptions.ValidationError("Ensure this value contains only letters, numbers, and underscore.")


class Profile(models.Model):
    MAX_LEN_USERNAME = 15
    MIN_LEN_USERNAME = 2

    username = models.CharField(
        max_length=MAX_LEN_USERNAME,
        validators=(
            validators.MinLengthValidator(MIN_LEN_USERNAME),
            # can consist only letters, numbers and underscore, otherwise raise ValidationError
            validate_only_alphanumeric,
        ),
        # required
        null=False,
        blank=False,
    )

    email = models.EmailField(
        # required
        null=False,
        blank=False,
    )

    age = models.PositiveIntegerField(
        # optional
        null=True,
        blank=True,
    )


class Album(models.Model):
    MAX_LEN_NAME = 30
    MAX_LEN_ARTIST = 30
    MAX_LEN_GENRE = 30

    POP_MUSIC = 'Pop Music'
    JAZZ_MUSIC = 'Jazz Music'
    RNB_MUSIC = 'R&B Music'
    ROCK_MUSIC = 'Rock Music'
    COUNTRY_MUSIC = 'Country Music'
    DANCE_MUSIC = 'Dance Music'
    KIP_HO_MUSIC_MUSIC = 'Hip Hop Music'
    OTHER_MUSIC = 'Other'

    # Защо ги подаваме в тюпъл и ги подаваме по 2 пъти? Защото така работят в джанго моделите.
    # На choices трябва да подадем две стойности
    MUSICS = (
        (POP_MUSIC, POP_MUSIC),
        (JAZZ_MUSIC, JAZZ_MUSIC),
        (RNB_MUSIC, RNB_MUSIC),
        (ROCK_MUSIC, ROCK_MUSIC),
        (COUNTRY_MUSIC, COUNTRY_MUSIC),
        (DANCE_MUSIC, DANCE_MUSIC),
        (KIP_HO_MUSIC_MUSIC, KIP_HO_MUSIC_MUSIC),
        (OTHER_MUSIC, OTHER_MUSIC),
    )

    name = models.CharField(
        max_length=MAX_LEN_NAME,
        unique=True,
        # required
        null=False,
        blank=False,
    )

    artist = models.CharField(
        max_length=MAX_LEN_ARTIST,
        # required
        null=False,
        blank=False,
    )

    genre = models.CharField(
        max_length=MAX_LEN_GENRE,
        choices=MUSICS,
        # required
        null=False,
        blank=False,
    )

    description = models.TextField(
        # optional
        null=True,
        blank=True,
    )

    image_url = models.URLField(
        # required
        null=False,
        blank=False,
    )

    price = models.FloatField(
        # да не може да е по-малко от 0
        validators=(
          validators.MinValueValidator(0.0),
        ),
        # required
        null=False,
        blank=False,
    )

    # така правим в сайта да ни се сортират по id
    class Meta:
        ordering = ('pk',)
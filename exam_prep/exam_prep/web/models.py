from django.core import validators, exceptions
from django.db import models


def validate_only_alphanumeric(value):
    for ch in value:
        if not ch.isalnum() and ch != '_':
            raise exceptions.ValidationError("Ensure this value contains only letters, numbers, and underscore.")


class Profile(models.Model):
    MIN_LENGTH_USERNAME = 2
    MAX_LENGTH_USERNAME = 15
    username = models.CharField(
        max_length=MAX_LENGTH_USERNAME,
        validators=(
          validators.MinLengthValidator(MIN_LENGTH_USERNAME),
          # can consist only letters, numbers and underscore, otherwise raise ValidationError
          validate_only_alphanumeric,
        ),

        # понеже по условие трябва да е required пишем
        null=False,
        blank=False,
    )

    email = models.EmailField(
        # понеже по условие трябва да е required пишем
        null=False,
        blank=False,
    )

    age = models.PositiveIntegerField(
        # понеже по условие трябва да е optional пишем
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

    album_name = models.CharField(
        # така казваме как да бъде изписано името на колоната в сайта
        verbose_name='Album Name',
        max_length=MAX_LEN_NAME,
        unique=True,
        null=False,
        blank=False,
    )

    artist = models.CharField(
        max_length=MAX_LEN_ARTIST,
        null=False,
        blank=False,
    )

    genre = models.CharField(
        max_length=MAX_LEN_GENRE,
        #   The choices are "Pop Music", "Jazz Music", "R&B Music", "Rock Music", "Country Music", "Dance Music", "Hip Hop Music", and "Other".
        choices=MUSICS,

        null=False,
        blank=False,
    )

    description = models.TextField(
        null=True,
        blank=True,
    )

    image_url = models.URLField(
        # така казваме как да бъде изписано името на колоната в сайта
        verbose_name='Image URL',
        null=False,
        blank=False,
    )

    price = models.FloatField(
        validators=(
            validators.MinValueValidator(0.0),
        ),
        null=False,
        blank=False,
    )

    # така правим в сайта да ни се сортират по id
    class Meta:
        ordering = ('pk',)
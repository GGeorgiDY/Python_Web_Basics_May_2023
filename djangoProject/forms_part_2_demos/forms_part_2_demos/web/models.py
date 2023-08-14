from django.db import models
from forms_part_2_demos.web.validators import validate_text, ValueInRangeValidator


class Person(models.Model):
    MAX_LEN_NAME = 20
    name = models.CharField(
        max_length=MAX_LEN_NAME,
    )

    profile_image = models.ImageField(
        # казва къде да качим снимката
        upload_to='persons',
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.name


class ToDo(models.Model):
    MAX_TODOS_COUNT_PER_PERSON = 2
    MAX_LEN_TEXT = 25
    text = models.CharField(
        max_length=MAX_LEN_TEXT,
        validators=(
            validate_text,
        ),
        null=False,
        blank=False,
    )

    priority = models.IntegerField(
        validators=(
            ValueInRangeValidator(1, 10),
        ),
        null=False,
        blank=False,
    )

    is_done = models.BooleanField(
        null=False,
        blank=False,
        default=False,
    )

    assignee = models.ForeignKey(
        Person,
        on_delete=models.RESTRICT,
    )

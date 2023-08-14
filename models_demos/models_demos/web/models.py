from enum import Enum

from django.db import models


class Department(models.Model):
    name = models.CharField(max_length=15)

    def __str__(self):
        return f'Id: {self.pk}; Name: {self.name}'


class Project(models.Model):
    name = models.CharField(max_length=30)
    code_name = models.CharField(
        max_length=10,
        unique=True,
    )
    deadline = models.DateField()


class Employee(models.Model):
    LEVEL_JUNIOR = 'Junior'
    LEVEL_REGULAR = 'Regular'
    LEVEL_SENIOR = 'Senior'

    LEVELS = (
        (LEVEL_JUNIOR, LEVEL_JUNIOR),
        (LEVEL_REGULAR, LEVEL_REGULAR),
        (LEVEL_SENIOR, LEVEL_SENIOR),
    )

    first_name = models.CharField(
        max_length=30,
    )
    last_name = models.CharField(
        max_length=50,
        null=True,
    )

    level = models.CharField(
        max_length=25,
        choices=LEVELS,
        verbose_name='Seniority level',
    )

    age = models.IntegerField(default=-1)

    years_of_experience = models.PositiveIntegerField()
    review = models.TextField()

    # тук датата се попълва ръчно
    start_date = models.DateField()
    email = models.EmailField(
        unique=True,
        editable=False,
    )
    is_full_time = models.BooleanField(
        null=True,
    )

    # пази дата с час
    created_on = models.DateTimeField(
        # ще се създава автоматично при създаване на запис
        auto_now_add=True,
    )
    updated_on = models.DateTimeField(
        # ще се записва автоматично при всеки ъпдейт
        auto_now=True,
    )

    # един към много
    department = models.ForeignKey(
        Department,
        on_delete=models.RESTRICT,
    )

    # много към много
    projects = models.ManyToManyField(
        Project,
    )

    @property
    def fullname(self):
        return f'{self.first_name} {self.last_name}'

    def __str__(self):
        return f'Id: {self.pk}, Name: {self.fullname}'


class AccessCard(models.Model):
    employee = models.OneToOneField(
        Employee,
        on_delete=models.CASCADE,
        primary_key=True,
    )


class Category(models.Model):
    name = models.CharField(
        max_length=15,
    )
    parent_category = models.ForeignKey(
        'Category',
        on_delete=models.RESTRICT,
        null=True,
        blank=True,
    )


# Employee.objects.all()
# Employee.objects.create()
# Employee.objects.filter()
# Employee.objects.update()


class NullBlankDemo(models.Model):
    blank = models.IntegerField(
        blank=True,
        null=False,
    )

    null = models.IntegerField(
        blank=False,
        null=True,
    )

    blank_null = models.IntegerField(
        blank=True,
        null=True,
    )

    default = models.IntegerField(
        blank=False,
        null=False,
    )

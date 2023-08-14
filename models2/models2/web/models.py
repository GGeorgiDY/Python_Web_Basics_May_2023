from django.db import models


class AuditInfoMixin(models.Model):

    class Meta:
        abstract = True

    created_on = models.DateTimeField(
        # ще се създава автоматично при създаване на запис
        auto_now_add=True,
    )
    updated_on = models.DateTimeField(
        # ще се записва автоматично при всеки ъпдейт
        auto_now=True,
    )


class Department(AuditInfoMixin, models.Model):
    name = models.CharField(max_length=15)

    slug = models.SlugField(unique=True)

    def __str__(self):
        return f'Id: {self.pk}; Name: {self.name}'


class Project(AuditInfoMixin, models.Model):
    name = models.CharField(max_length=30)
    code_name = models.CharField(
        max_length=10,
        unique=True,
    )
    deadline = models.DateField()


class Employee(AuditInfoMixin, models.Model):

    class Meta:
        ordering = ('-age',)

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

    # verbose_name - това казва как искам да се казва в админ панела това тази колона
    level = models.CharField(
        max_length=25,
        choices=LEVELS,
        verbose_name='Seniority level',
    )

    age = models.IntegerField(default=-1)

    years_of_experience = models.PositiveIntegerField()
    review = models.TextField()

    start_date = models.DateField()

    email = models.EmailField(
        unique=True,
    )

    is_full_time = models.BooleanField(
        null=True,
    )

    # пази дата с час


    department = models.ForeignKey(
        Department,
        on_delete=models.CASCADE,
    )

    projects = models.ManyToManyField(Project)

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
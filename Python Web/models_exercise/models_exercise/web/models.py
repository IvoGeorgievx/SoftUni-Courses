from django.db import models


class Department(models.Model):
    name = models.CharField(max_length=15, )

    def __str__(self):
        return f"ID: {self.pk} ; Name: {self.name}"


class Project(models.Model):
    name = models.CharField(max_length=25, )
    code_name = models.CharField(
        max_length=15,
        unique=True
    )


class ExtraInfo(models.Model):
    name = models.TextField()


class Employees(models.Model):
    LEVEL_JUNIOR = 'Junior'
    LEVEL_REGULAR = 'Regular'
    LEVEL_SENIOR = 'Senior'

    LEVELS = (
        (LEVEL_JUNIOR, LEVEL_JUNIOR),
        (LEVEL_REGULAR, LEVEL_REGULAR),
        (LEVEL_SENIOR, LEVEL_SENIOR),
    )

    first_name = models.CharField(max_length=30, )

    last_name = models.CharField(max_length=50, null=True)

    level = models.CharField(
        max_length=len(LEVEL_REGULAR),
        choices=LEVELS,
        verbose_name='Seniority level:'
    )

    age = models.IntegerField(default=-1)

    years_of_experience = models.PositiveIntegerField()

    review = models.TextField()

    start_date = models.DateField()

    email = models.EmailField(unique=True)

    is_full_time = models.BooleanField(null=True, )

    created_on = models.DateTimeField(
        auto_now_add=True, )

    updated_on = models.DateTimeField(
        auto_now=True
    )
    # One-to-many
    department = models.ForeignKey(
        Department, on_delete=models.CASCADE
    )

    # Many-to-many
    projects = models.ManyToManyField(Project)

    # One-to-many
    extra_info = models.ForeignKey(ExtraInfo, on_delete=models.RESTRICT)

    def __str__(self):
        return f"{self.id}:{self.first_name} {self.last_name}"


class AccessCard(models.Model):
    employee = models.OneToOneField(
        Employees, on_delete=models.CASCADE,
        primary_key=True,
    )

    def __str__(self):
        return f"ID: {self.pk}"

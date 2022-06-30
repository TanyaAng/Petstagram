from django.db import models
from django.core.validators import MinLengthValidator, URLValidator

from petstagram.main.validators import only_letters_validator


class Profile(models.Model):
    FIRST_NAME_MIN_LENGTH = 2
    LAST_NAME_MIN_LENGTH = 2
    FIRST_NAME_MAX_LENGTH = 30
    LAST_NAME_MAX_LENGTH = 30
    MALE = 'Male'
    FEMALE = 'Female'
    DO_NOT_SHOW = 'Do not show'
    GENDER = [(x, x) for x in (MALE, FEMALE, DO_NOT_SHOW)]
    # id/pk by default
    first_name = models.CharField(
        max_length=FIRST_NAME_MAX_LENGTH,
        validators=(
            MinLengthValidator(FIRST_NAME_MIN_LENGTH),
            only_letters_validator,

        ),
    )
    last_name = models.CharField(
        max_length=LAST_NAME_MAX_LENGTH,
        validators=(
            MinLengthValidator(LAST_NAME_MIN_LENGTH),
            only_letters_validator,

        )
    )

    picture = models.URLField()

    date_of_birth = models.DateField(null=True, blank=True)

    description = models.TextField(null=True, blank=True)

    email = models.EmailField(null=True, blank=True)

    gender = models.CharField(
        max_length=max(len(x) for x, _ in GENDER),
        choices=GENDER,
        null=True,
        blank=True,
    )

    # same as
    # picture2=models.CharField(validators=(URLValidator()))

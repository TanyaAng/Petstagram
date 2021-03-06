import datetime

from django.db import models
from django.core.validators import MinLengthValidator

from petstagram.main.validators import only_letters_validator, validate_file_max_size_in_mb


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
        default=DO_NOT_SHOW,
    )

    # same as
    # picture2=models.CharField(validators=(URLValidator()))

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Pet(models.Model):
    '''CONSTANTS'''
    CAT = 'Cat'
    DOG = 'Dog'
    BUNNY = 'Bunny'
    PARROT = 'Parrot'
    FISH = 'Fish'
    OTHER = 'Other'
    TYPES = [(x, x) for x in [CAT, DOG, BUNNY, PARROT, FISH, OTHER]]

    NAME_MAX_LENGTH = 30

    '''COLUMNS/ FIELDS'''
    name = models.CharField(
        max_length=NAME_MAX_LENGTH,
    )
    type = models.CharField(
        max_length=max(len(x) for x, _ in TYPES),
        choices=TYPES,
    )

    date_of_birth = models.DateField(null=True, blank=True)

    '''ONE TO ONE RELATIONS'''

    '''ONE TO MANY RELATIONS'''
    user_profile = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
    )

    '''MANY TO MANY RELATIONS'''

    @property
    def age(self):
        return datetime.datetime.now().year-self.date_of_birth.year

    '''DUNDER METHODS'''

    '''META'''

    class Meta:
        unique_together = ('user_profile', 'name')


class PetPhoto(models.Model):
    photo = models.ImageField(
        validators=(#validate_file_max_size_in_mb,
                    )
    )

    # TODO validate at least one pet
    tagged_pets = models.ManyToManyField(Pet, )

    description = models.TextField(null=True, blank=True)

    publication_date = models.DateTimeField(
        auto_now_add=True,

    )
    likes = models.IntegerField(
        default=0,
    )

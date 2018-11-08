from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    GENDER_CHOICES = (
        ('male', 'Male'),
        ('female', 'Female'),
        ('not-specified', 'Not specified')
    )

    birth_date = models.DateField(_('User Birthday'), null=True)
    gender = models.CharField(_('User Gender'), max_length=80, choices=GENDER_CHOICES, null=True, blank=True)

    def __str__(self):
        return self.username
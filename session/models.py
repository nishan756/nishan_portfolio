from django.db import models

from django.contrib.auth.models import AbstractUser

from django.core.exceptions import ValidationError

import uuid


class Country(models.Model):
    name = models.CharField(max_length = 50 , unique = True)

    code = models.CharField(max_length = 3 , unique = True)

    def clean(self):
        queryset = Country.objects.filter(name__iexact = self.name)

        if self.pk:
            queryset = queryset.exclude(id = id)

        if queryset:
            raise ValidationError("Country with this name is already exists.")

    def __str__(self):
        return self.name

class CustomUser(AbstractUser):
    id = models.UUIDField(primary_key = True , default = uuid.uuid4 , editable = False)

    image = models.ImageField(upload_to = "user_images/" , blank = True , null = True)

    phone_number = models.CharField(max_length = 15 , unique = True)

    country = models.ForeignKey(Country , on_delete = models.SET_NULL , null = True)

    class Meta:
        ordering = ["-date_joined"]

        verbose_name = "User"

        verbose_name_plural = "Users"
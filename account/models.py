from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth.base_user import BaseUserManager
from django.core.validators import validate_email

from shared.enums import UserType


# Create your models here.
class UserManager(BaseUserManager):
    def create_superuser(self, username, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        if username and password:
            user = self.create_user(username, password, UserType.Admin, **extra_fields)
            return user
        else:
            raise Exception("username and password required")

    def create_user(self, username, password, role, **extra_fields):
        if username and password:
            user = self.model(username=username, password=password, role=role, **extra_fields)
            user.set_password(password)
            user.save()
            return user
        else:
            raise Exception("username or password or role is missing!")


class User(AbstractUser):
    role = models.CharField(choices=[(UserType.Admin, UserType.Admin.title()), (UserType.Doctor, UserType.Doctor.title()), (UserType.Patient, UserType.Patient.title())], max_length=10)
    objects = UserManager()



"""
1: AbstractUser: Use this option if you are happy with the existing fields on the User model and just want to remove the username field.
2: AbstractBaseUser: Use this option if you want to start from scratch by creating your own, completely new User model.

The steps are the same for each:

Create a custom User model and Manager
Update settings.py
Customize the UserCreationForm and UserChangeForm forms
Update the admin

"""

from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.utils.translation import gettext_lazy as _
from django.utils import timezone

from .managers import CustomUserManager

class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('email Address'), unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default = timezone.now)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__ (self):
        return self.email




"""
- Created a new class called CustomUser that subclasses AbstractBaseUser
- Added fields for email, is_staff, is_active, and date_joined
- Set the USERNAME_FIELD -- which defines the unique identifier for the User model -- to email
- Specified that all objects for the class come from the CustomUserManager


You can now reference the User model with either get_user_model() or settings.AUTH_USER_MODEL. 
Refer to Referencing the User model from the official docs for more info.

"""










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
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
import uuid

from .managers import CustomUserManager


class CustomUser(AbstractBaseUser, PermissionsMixin):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    first_name = models.CharField(max_length=200, blank=True)
    last_name = models.CharField(max_length=200, blank=True)
    email = models.EmailField(max_length=200, unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(null=True)
    # any fields you would like to add

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__ (self):
        return self.email


# We can set up signals for creating a user profile autmoatically when a user is created

class Profile(models.Model):
    objects = models.Manager()   # this will remove the pylint error
    GENDER_CHOICES = (
        ('m', 'Male'),
        ('f', 'Female'),
    )

    MARITAL_STATUS_CHOICES = (
        ('s', 'Single'),
        ('m', 'Married')
    )

    user = models.OneToOneField('CustomUser', on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    marital_status = models.CharField(max_length=1, choices=MARITAL_STATUS_CHOICES)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)

    def __str__(self):
        return f'{self.user.first_name} Profile'





"""
- Created a new class called CustomUser that subclasses AbstractBaseUser
- Added fields for email, is_staff, is_active, and date_joined
- Set the USERNAME_FIELD -- which defines the unique identifier for the User model -- to email
- Specified that all objects for the class come from the CustomUserManager


You can now reference the User model with either get_user_model() or settings.AUTH_USER_MODEL. 
Refer to Referencing the User model from the official docs for more info.

"""










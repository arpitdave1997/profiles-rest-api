from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager

class UserProfileManager(BaseUserManager):
    """Manager for User profiles"""

    def create_user(self, email, name, password = None):
        """Create a new user profile"""
        if not email:
            raise ValueError("User must have an email address")

        email = self.normalize_email(email)
        user = self.Model(email = email, name = name)
        user.set_password(password)
        user.save(using = self._db)
        return user

    def create_superuser(self, email, name, password):
        """Create and save a new SuperUser"""
        user = self.create_user(email, name, password)
        ## This is automatically created.
        user.is_superuser = True
        user.is_staff = True
        user.save(using = self._db)
        return user


class UserProfile(AbstractBaseUser, PermissionsMixin):
    """Database setup for Users present in System"""

    # Specifying the Data values
    email = models.EmailField(max_length=255, unique = True)
    name = models.CharField(max_length = 255)
    is_activate = models.BooleanField(default = True)
    is_Staff = models.BooleanField(default = False)

    ## Specifying Model Manager
    objects = UserProfileManager()

    # Setting up variables which would define the use of the following Columns
    USERNAME_FIELD = 'email'
    REQUIRED_FIELD = ['name']

    def get_full_Name(self):
        """Fetch Full name of the Customer"""
        return self.name

    def get_short_name(self):
        """Fetch short Name of the Customer"""
        return self.name

    def __str__(self):
        """"Return string representation of our user"""
        ## In this case, Email represents the identity of user.
        return self.email
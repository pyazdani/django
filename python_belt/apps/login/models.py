from __future__ import unicode_literals
from django.db import models
import bcrypt
import re
from datetime import date

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class UserManager(models.Manager):
    def register(self, name, alias, email, password, confirm_password, dob):
        errors = []
        if len(name) < 3:
            errors.append("Name is required")
        if len(alias) < 3:
            errors.append("You need an alias/nickname!!")
        if len(email)< 1:
            errors.append("Email is required")
        elif not EMAIL_REGEX.match(email):
            errors.append("Invalid email")
        else:
            user= User.userManager.filter(email=email.lower())
            if len(user) > 0:
                errors.append("Email is already in use")
        if len(password) < 1:
            errors.append("Password is required")
        elif len(password) < 8:
            errors.append("Password must be 8 characters or more")
        if len(confirm_password) < 1:
            errors.append("Confirm password is required")
        elif password != confirm_password:
            errors.append("Password must match confirm password")
        if len(errors) > 0:
            return (False, errors)
        else:
            user = User.userManager.create(name=name, alias=alias, email=email, password= bcrypt.hashpw(password.encode(), bcrypt.gensalt()), dob=dob)
            return (True, user)
    def login(self, email, password):
        errors = []

        if len(email)< 1:
            errors.append("Email not found")
        elif not EMAIL_REGEX.match(email):
            errors.append("Invalid email")
        else:
            user= User.userManager.filter(email=email.lower())
            if len(user) == 0:
                errors.append("Email not found")

        if len(password) < 1:
            errors.append("Password is required")
        elif len(password) < 8:
            errors.append("Password must be 8 characters of more")

        if len(errors) > 0:
            return (False, errors)
        else:
            if bcrypt.checkpw(password.encode(), user[0].password.encode()):
                return (True, user[0])
            else:
                return (False, ['Incorrect password'])

class User(models.Model):
    name = models.CharField(max_length=255)
    alias = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    dob = models.DateField()
    created_at = models.DateTimeField(auto_now = True)
    updated_at = models.DateTimeField(auto_now = True)
    userManager = UserManager()
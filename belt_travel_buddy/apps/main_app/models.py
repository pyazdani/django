 # -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
import bcrypt
from datetime import datetime

class UserManager(models.Manager):
    def register(self, name, username, password, confirm):

        errors = []
        if len(name) < 3:
            errors.append("Name must be 3 characters or longer!")
        if len(username) < 3:
            errors.append("Username must be 3 characters or longer!")
        elif len(User.userManager.filter(username=username)) > 0:
            errors.append("Username already exists!")
        if len(password) < 8:
            errors.append("Password must be 8 characters or longer!")
        if not password == confirm:
            errors.append("Password must match Confirm Password!")

        if len(errors) > 0:
            return (False, errors)
        else:
            pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
            user = User.userManager.create(name=name, username=username, pw_hash=pw_hash)
            return (True, user)

    def login(self, username, password):

        errors = []

        if len(username) < 2:
            errors.append("Username must be 2 characters or longer!")
        if len(password) < 8:
            errors.append("Password must be 8 characters or longer!")

        user = User.userManager.filter(username=username)

        if len(user) == 0:
            errors.append("Username not found!")

        if len(errors) > 0:
            return (False, errors)
        else:
            if bcrypt.checkpw(password.encode(), user[0].pw_hash.encode()):
                return (True, user[0])
            else:
                return (False, ["Incorrect Password!"])

class User(models.Model):
    name = models.CharField(max_length=255)
    username = models.CharField(max_length = 255)
    pw_hash = models.CharField(max_length = 255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    userManager = UserManager()

    def __repr__(self):
        return "<User: {} {} {} {}>".format(
            self.name,
            self.username,
            self.created_at,
            self.updated_at
        )

class TripManager(models.Manager):
    def validate(self, destination, description, start_date, end_date):

        errors = []
        if len(destination) < 1:
            errors.append("Please select a destination!")
        if len(description) < 1:
            errors.append("Please write a descrition!")
        if len(start_date) < 1:
            errors.append("Please Select a Start Date!")
        elif start_date < str(datetime.now()):
            errors.append("Start Date Must Be in the Future!")
        if len(end_date) < 1:
            errors.append("Please Select an End Date!")
        elif start_date < str(datetime.now()):
            errors.append("End Date Must Be in the Future!")
        if start_date > end_date:
            errors.append("End Date Must Come After Start Date!")

        if len(errors) > 0:
            return (False, errors)
        else:
            trip = Trip.tripManager.create(destination=destination, description=description, start_date=start_date, end_date=end_date)
            return (True, trip)

class Trip(models.Model):
    destination = models.CharField(max_length = 255)
    description = models.TextField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    users = models.ManyToManyField(User, related_name = "trips")

    tripManager = TripManager()

    def __repr__(self):
        return "<Trip: {} {} {} {} {}>".format(
            self.destination,
            self.description,
            self.start_date,
            self.end_date,
            self.users,
        )
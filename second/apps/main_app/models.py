 # -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
import bcrypt
from datetime import datetime
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')

class UserManager(models.Manager):
    def register(self, name, username, password, confirm):

        errors = []
        if len(name) < 3:
            errors.append("Name must be 3 characters or longer!")
        if len(username) < 3:
            errors.append("Username must be 3 characters or longer!")
        elif len(User.userManager.filter(username=username)) > 0:
            errors.append("Username already exists!")
        elif not re.match(EMAIL_REGEX, username):
            errors.append("invalid email/username")
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

class QuoteManager(models.Manager):
    def validate(self, post_data, user_id):

        errors = []
        if len(post_data['author']) < 3:
            errors.append("Quoted By must be 3 characters or longer!")
        if len(post_data['message']) < 10:
            errors.append("Quote(Message) must be 10 characters or longer!")

        if len(errors) > 0:
            return (False, errors)
        else:
            quote = Quote.quoteManager.create(author=post_data['author'], quote=post_data['message'], uploader_id=user_id)
            return (True, quote)


class Quote(models.Model):
	author = models.CharField(max_length=255)
	quote = models.CharField(max_length=255)
	uploader = models.ForeignKey(User, related_name="sub_quotes")
	favorited = models.ManyToManyField(User, related_name="fav_quotes")

	quoteManager = QuoteManager()
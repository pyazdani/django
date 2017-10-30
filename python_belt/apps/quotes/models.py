from __future__ import unicode_literals
from django.db import models
from ..login.models import User, UserManager
from django.contrib import messages

class QuoteManager(models.Manager):
    def add (self, author, message, user_id):
        errors = []
        if len(author) < 3:
            errors.append("Author name must be . (Even if it is anonymous!)")
        if len(message) < 10:
            errors.append("Message text must be 10 charcters or more")
        else:
            quote = Quote.quoteManager.create(author=author, message=message, uploader=user_id)
            return(True, quote)


class Quote(models.Model):
    author = models.CharField(max_length=255)
    message = models.CharField(max_length=255)
    uploader = models.ForeignKey(User, related_name='uploaded')
    users = models.ManyToManyField(User, related_name='quotes')
    created_at = models.DateTimeField(auto_now = True)
    updated_at = models.DateTimeField(auto_now = True)
    quoteManager = QuoteManager()
from __future__ import unicode_literals
from django.db import models

class Dojos(models.Model):
    name = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=2)
    desc = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __repr__(self):
        return "<Dojos object:{} {} {} {} {} {}>".format(
            self.name, 
            self.city, 
            self.state,
            self.desc, 
            self.created_at, 
            self.updated_at,
            )

class Ninjas(models.Model):
    dojo_id = models.ForeignKey(Dojos, related_name="ninjas")
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __repr__(self):
        return "<Ninjas object:{} {} {} {} {}>".format(
            self.dojo_id, 
            self.first_name, 
            self.last_name, 
            self.created_at, 
            self.updated_at,
            )




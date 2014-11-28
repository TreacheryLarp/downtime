from django.db import models
from django.contrib.auth.models import User

class Discipline(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
            return self.name

class Title(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
            return self.name

class Ability(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
            return self.name

class Boon(models.Model):
    type = models.CharField(max_length=200)

    def __str__(self):
            return self.type

class Character(models.Model):
    name = models.CharField(max_length=200)
    user = models.ForeignKey(User)
    disciplines = models.ManyToManyField(Discipline)
    abilities = models.ManyToManyField(Ability)
    titles = models.ManyToManyField(Title)

    def __str__(self):
            return self.name

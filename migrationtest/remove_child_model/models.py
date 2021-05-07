from django.db import models


class Parent(models.Model):
    name = models.TextField()


class Child(Parent):
    alias = models.TextField()

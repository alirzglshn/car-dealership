from tkinter.constants import CASCADE

from django.db import models
from django.db.models import ForeignKey


# Create your models here.

class Person(models.Model):
    name = models.CharField(max_length=30)
    phone = models.IntegerField()
    date = models.DateTimeField(auto_now=True , auto_now_add=False)


class Car(models.Model):
    company = models.CharField(max_length=30)
    person = ForeignKey(Person , on_delete=models.CASCADE)



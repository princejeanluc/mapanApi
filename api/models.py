from tkinter import EventType

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone


# Create your models here.


class Organizer(AbstractUser):
    username = models.CharField(unique=True, max_length=100)
    password = models.CharField(max_length=500)
    email = models.EmailField()
    linkedin = models.URLField(default="https://www.linkedin.com")
    twitter = models.URLField(default="https://www.twitter.com")
    facebook = models.URLField(default="https://www.facebook.com")
    instagram = models.URLField(default="https://www.instagram")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


class EventType(models.Model):
    label = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)

class MapanEvent(models.Model):
    title = models.CharField(max_length=300)
    description = models.TextField()
    date = models.DateField()
    time = models.TimeField()
    longitude = models.DecimalField(max_digits=9,decimal_places=2)
    latitude = models.DecimalField(max_digits=9,decimal_places=2)
    address = models.CharField(max_length=500)
    image = models.ImageField(upload_to='')
    eventType = models.ForeignKey(EventType, on_delete=models.CASCADE)
    organizer = models.ForeignKey(Organizer, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    class Meta:
        ordering = ['created']
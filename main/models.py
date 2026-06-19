from django.db import models
from django.utils.timezone import now
from cloudinary.models import CloudinaryField
import os

class JobSeeker(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    message = models.TextField(blank=True)

    cv = CloudinaryField('cv')

    created_at = models.DateTimeField(default=now)

    def __str__(self):
        return self.name


class Vendor(models.Model):
    name = models.CharField(max_length=100)
    company = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class AdminUser(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.username
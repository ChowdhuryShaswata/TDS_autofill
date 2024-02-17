from django.db import models

# Create your models here.

class NameGenerator(models.Model):
    username = models.CharField(primary_key=True, max_length=100)
    location = models.CharField(max_length=100)
    category = models.CharField(max_length=100)

    def __str__(self):
        return self.username

class TDSUser(models.Model):
    username=models.CharField(max_length=200)
    email=models.CharField(max_length=200)
    password=models.CharField(max_length=200)
    def __str__(self):
        return self.username

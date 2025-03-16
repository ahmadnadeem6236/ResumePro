from django.contrib.postgres.fields import ArrayField
from django.db import models


# Create your models here.
class GeeksModel(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.title


class PdfModel(models.Model):
    name = models.CharField(max_length=100)
    skills = ArrayField(models.CharField(max_length=100), blank=True)
    experience = ArrayField(models.CharField(max_length=100), blank=True)
    projects = ArrayField(models.CharField(max_length=100), blank=True)
    education = ArrayField(models.CharField(max_length=100), blank=True)

    def __str__(self):
        return self.name

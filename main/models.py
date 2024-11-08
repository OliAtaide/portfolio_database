from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model
import os
#from PIL import Image

class Skill(models.Model):
    name = models.CharField("Nome", max_length=100, blank=False)
    logo = models.ImageField(upload_to="main", blank=False, null=True)
    url = models.URLField(max_length=200)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Skills"


class Project(models.Model):
    name = models.CharField("Nome", max_length=100, blank=False)
    thumbnail = models.ImageField(upload_to="main", blank=False, null=True)
    url = models.URLField(max_length=200, blank=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Projects"

import os

from django.db import models
from django.contrib.auth.models import User

def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext


def upload_image_path(instance, filename):
    name, ext = get_filename_ext(filename)
    final_name = f"{instance.title}-{User}-{os.times}{ext}"
    return f"logo-image/{final_name}"


# Create your models here.

class Siteabout(models.Model):
    title = models.CharField(max_length=150)
    about_us = models.TextField( null=True, blank=True)
    programmer_image = models.ImageField(upload_to=upload_image_path, null=True, blank=True)

    def __str__(self):
        return self.title

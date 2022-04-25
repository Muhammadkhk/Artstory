import os
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext


def upload_image_path(instance, filename):
    name, ext = get_filename_ext(filename)
    final_name = f"{instance.id}-{User}-{os.times}{ext}"
    return f"'profileimages/'{final_name}"

class Profile(models.Model):
    firstname = models.CharField(max_length=150,default='empty')
    lastname = models.CharField(max_length=150,default='empty')
    email = models.EmailField(max_length=150,default='empty')
    slogan = models.CharField(max_length=150,default='empty')
    text = models.TextField(default='empty')
    image = models.ImageField(upload_to=upload_image_path, null=True, blank=True)
    author = models.ForeignKey(User,default='empty',on_delete=models.CASCADE)

    def __str__(self):
        return self.firstname
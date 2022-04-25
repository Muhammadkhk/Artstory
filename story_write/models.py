#from enum import auto

import os
from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import get_list_or_404
#from matplotlib.pyplot import title

# Create your models here.


def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext


def upload_image_path(instance, filename):
    name, ext = get_filename_ext(filename)
    final_name = f"{instance.id}-{User}-{os.times}{ext}"
    return f"'profileimages/'{final_name}"


class StoryManager(models.Manager):
    def get_by_id(self, selected_story_id):
        qs = self.get_queryset().filter(id=selected_story_id)
        if qs.count() == 1:
            return qs.first()
        else:
            return None

    def get_show_story(self):
        return self.get_queryset().filter(public=True)

    def get_show_story_private(self, story_user):
        return get_list_or_404(Writestory,author=story_user,public=False)


class Writestory(models.Model):
    title = models.CharField(max_length=150)
    text = models.TextField()
    image = models.ImageField(upload_to=upload_image_path)
    public = models.BooleanField(default=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User,default='',on_delete=models.CASCADE)



    objects = StoryManager()

    def __str__(self):
        return self.title

class Comment(models.Model):
    text = models.TextField()
    Date = models.DateTimeField(auto_now_add=True)
    postID = models.IntegerField()
    author = models.ForeignKey(User,default='',on_delete=models.CASCADE)

    def __str__(self):
        return self.text
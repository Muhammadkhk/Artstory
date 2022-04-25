from django.contrib import admin

# Register your models here.

from .models import Profile

class userAdmin(admin.ModelAdmin):

    class Meta:
        model = Profile

admin.site.register(Profile)

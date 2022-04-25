from django.contrib import admin

# Register your models here.

from .models import Writestory,Comment

class WriteAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'title']

    class Meta:
        model = Writestory

admin.site.register(Writestory , WriteAdmin)

class Writecomment(admin.ModelAdmin):
    class Meta:
        model = Comment
admin.site.register(Comment,Writecomment)
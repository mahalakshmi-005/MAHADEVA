from django.contrib import admin
from django.utils.encoding import smart_str
from blog.models import post
from django.db import models
from tinymce.widgets import TinyMCE

class PostAdmin(admin.ModelAdmin):
    fieldsets = [
    ("Title/Date",{"fields":["title","date"]}),
    ("Content",{"fields":["des","body"]})
    ]

    formfield_overrides = {
    models.TextField:{ "widget":TinyMCE()}
    }
# Register your models here.
admin.site.register(post, PostAdmin)
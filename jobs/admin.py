from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Job, Skill

admin.site.register(Job)
admin.site.register(Skill)
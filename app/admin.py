from django.contrib import admin
from .models import Task # add model to model.py

# Register your models here.
@admin.register(Task)
class AuthorAdmin(admin.ModelAdmin):
    pass
from django.contrib import admin
from django.contrib.admin import register

from app.models import ToDo


@register(ToDo)
class ToDoAdmin(admin.ModelAdmin):
    pass

# coding: utf-8
from rest_framework import serializers

from .models import ToDo


class ToDoSerializer(serializers.ModelSerializer):

    class Meta:
        model = ToDo
        depth = 1
        fields = ['pk', 'note', 'added_at', 'done', 'done_at']

# coding: utf-8
from django.contrib.auth.models import User
from rest_framework import serializers
from .models import ToDo


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['user_name', ]


class ToDoSerializer(serializers.ModelSerializer):

    user_name = UserSerializer(many=False)

    class Meta:
        model = ToDo
        depth = 1
        fields = ['user_name', 'note', 'added_at', 'done', 'done_at']

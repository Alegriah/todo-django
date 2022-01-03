"""TODO"""

from rest_framework import serializers
from .models import (
    Category,
    Todo,
)


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        exclude = ()


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        exclude = ()

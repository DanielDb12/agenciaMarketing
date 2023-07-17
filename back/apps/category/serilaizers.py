from django.db.models import fields
from rest_framework import serializers
from .models import *


class CategorySerilaizer(serializers.ModelSerializer):

    class Meta:
        model=Category
        fields=[
                'id',
                'name',
                'slug',
                'views',
                ]

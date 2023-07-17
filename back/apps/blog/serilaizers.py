from rest_framework import serializers

from apps.category import serilaizers
from .models import *
from apps.category.serilaizers import CategorySerilaizer

class PostSerilaizer(serializers.ModelSerializer):
    category = CategorySerilaizer()
    class Meta:
        model=Post
        fields=['id',
                'title',
                'thumbnail',
                'description',
                'content',
                'time_read',
                'published',
                'views',
                'category',
                'slug'
                ]

class PostListSerializer(serializers.ModelSerializer):
    category = CategorySerilaizer()
    class Meta:
        model=Post
        fields=[
                'id',
                'title',
                'slug',
                'thumbnail',
                'description',
                'time_read',
                'published',
                'views',
                'category'
                ]

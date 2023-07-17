#!/usr/bin/env python3
from django.db.models import fields
from rest_framework import serializers
from .models import *

class ContactSerilaizer(serializers.ModelSerializer):

    class Meta:
        model=EmailModel
        fields = '__all__'

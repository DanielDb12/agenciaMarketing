#!/usr/bin/env python3
from django.urls import path
from .views import *



urlpatterns = [

    path('send_email', EmailView.as_view())

]

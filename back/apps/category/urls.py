from django.urls import path

from .views import *



urlpatterns = [

        path('list', ListCategoriesViews.as_view())
        ]

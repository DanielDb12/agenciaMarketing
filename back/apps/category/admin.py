from django.contrib import admin

from .models import *


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id','name',)
    list_display_link = ('name',)
    list_per_page = 25

admin.site.register(Category,CategoryAdmin)

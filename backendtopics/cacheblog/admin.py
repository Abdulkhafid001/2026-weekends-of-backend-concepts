from django.contrib import admin
from .models import Blog


class BlogAdmin(admin.ModelAdmin):
    list_display = ['author','pub_date']


# Register your models here.
admin.site.register(Blog, BlogAdmin)

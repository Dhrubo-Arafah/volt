from django.contrib import admin

from .models import Course


@admin.register(Course)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id','mentor','title']

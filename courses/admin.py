from django.contrib import admin
from .models import *


@admin.register(Product)
class AdminProduct(admin.ModelAdmin):
    list_display = ('name', 'owner',)
    fields = (
        'name',
        'owner',
    )


@admin.register(Lesson)
class AdminLesson(admin.ModelAdmin):
    list_display = ('name', 'video_url', 'duration_seconds',)

    fields = (
        'name',
        'video_url',
        'duration_seconds',
        'products',
    )


@admin.register(ProductAccess)
class AdminProductAccess(admin.ModelAdmin):
    list_display = ('user', 'product', 'status',)
    fields = (
        'user',
        'product',
        'status',
        'viewing_time_seconds',
    )

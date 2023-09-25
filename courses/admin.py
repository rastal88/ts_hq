from django.contrib import admin
from .models import *

@admin.register(Product)
class AdminProduct(admin.ModelAdmin):
    fields = (
        'name',
        'owner',
    )

@admin.register(Lesson)
class AdminLesson(admin.ModelAdmin):
    fields = (
        'name',
        'video_url',
        'duration_seconds',
    )

@admin.register(ProductAccess)
class AdminProductAccess(admin.ModelAdmin):
    fields = (
        'status',
        'viewing_time_seconds',
    )


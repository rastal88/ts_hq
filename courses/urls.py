from django.urls import path
from rest_framework import routers

from courses.views import *


router = routers.DefaultRouter()


urlpatterns = [
    path('api/lessons/', LessonListAPIView.as_view(), name='lesson-list'),
    path('api/lessons/product/<int:product_id>/', LessonByProductAPIView.as_view(), name='lesson-by-product'),
    path('api/lessons/products/stats/', ProductStatsAPIView.as_view(), name='product-stats'),
]
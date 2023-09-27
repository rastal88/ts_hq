from rest_framework import serializers
from .models import *
from django.db.models import Sum


class ProductModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = "__all__"

    def get_status(self, obj):
        user = self.context['request'].user
        product_access = ProductAccess.objects.get(user=user, product=obj.products.first())
        return product_access.status

    def get_viewing_time_seconds(self, obj):
        user = self.context['request'].user
        product_access = ProductAccess.objects.get(user=user, product=obj.products.first())
        return product_access.viewing_time_seconds

    def get_last_viewed_at(self, obj):
        user = self.context['request'].user
        product_access = ProductAccess.objects.get(user=user, product=obj.products.first())
        return product_access.last_viewed_at


class ProductAccessSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductAccess
        fields = ('user', 'status', 'viewing_time_seconds')


class ProductStatsSerializer(serializers.ModelSerializer):
    total_viewed_lessons = serializers.SerializerMethodField()
    total_viewing_time_seconds = serializers.SerializerMethodField()
    total_users = serializers.SerializerMethodField()
    acquisition_percentage = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = (
            'id', 'name', 'total_viewed_lessons', 'total_viewing_time_seconds', 'total_users', 'acquisition_percentage')

    def get_total_viewed_lessons(self, obj):
        return ProductAccess.objects.filter(product=obj, status=True).count()

    def get_total_viewing_time_seconds(self, obj):
        return ProductAccess.objects.filter(product=obj, status=True).aggregate(total_time=Sum('viewing_time_seconds'))[
            'total_time'] or 0

    def get_total_users(self, obj):
        return ProductAccess.objects.filter(product=obj).count()

    def get_acquisition_percentage(self, obj):
        total_users_on_platform = User.objects.count()
        if total_users_on_platform == 0:
            return 0
        return (ProductAccess.objects.filter(product=obj).count() / total_users_on_platform) * 100

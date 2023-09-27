from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from courses.models import Product, Lesson, ProductAccess
from courses.serializers import LessonSerializer, ProductStatsSerializer


class LessonListAPIView(generics.ListAPIView):
    serializer_class = LessonSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        user = self.request.user
        product_accesses = ProductAccess.objects.filter(user=user)

        lessons = Lesson.objects.filter(products__productaccess__in=product_accesses)

        return lessons


class LessonByProductAPIView(generics.ListAPIView):
    serializer_class = LessonSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        user = self.request.user
        product_id = self.kwargs['product_id']

        try:
            product_access = ProductAccess.objects.get(user=user, product_id=product_id)
        except ProductAccess.DoesNotExist:
            return Lesson.objects.none()

        lessons = Lesson.objects.filter(products=product_id)

        return lessons


class ProductStatsAPIView(generics.ListAPIView):
    serializer_class = ProductStatsSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return Product.objects.all()

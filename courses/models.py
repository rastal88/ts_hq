from django.contrib.auth.models import User
from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=255)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)


class Lesson(models.Model):
    name = models.CharField(max_length=255)
    video_url = models.URLField()
    duration_seconds = models.IntegerField()
    products = models.ManyToManyField(Product)


class ProductAccess(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    status = models.BooleanField(default=False)  # Просмотрено/Не просмотрено
    viewing_time_seconds = models.IntegerField(default=0)

    def update_viewing_status(self):
        # Вычисляем процент просмотренного видео
        percentage_viewed = (self.viewing_time_seconds / self.product.lesson.duration_seconds) * 100

        # Обновляем статус в зависимости от процента просмотренного видео
        if percentage_viewed >= 80:
            self.status = True
        else:
            self.status = False

    def update_viewing_time(self, seconds_viewed):
        # Обновляем время просмотра
        self.viewing_time_seconds = seconds_viewed

        # После обновления времени просмотра обновляем статус
        self.update_viewing_status()

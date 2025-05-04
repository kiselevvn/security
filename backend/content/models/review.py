from django.db import models


class Review(models.Model):
    """
    Отзыв
    """

    name = models.CharField(max_length=255, verbose_name="Имя")
    job = models.CharField(max_length=255, verbose_name="Организация", blank=True, null=True)
    text = models.TextField(verbose_name="Текст отзыва")
    is_published = models.BooleanField(verbose_name="Опубликовано", default=False)
    created_at = models.DateTimeField(verbose_name="Дата создания", auto_now_add=True)

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"

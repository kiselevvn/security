from django.db import models


class Offer(models.Model):
    """
    Предложение
    """

    picture = models.ImageField(verbose_name="Картинка", blank=True, null=True)
    subtitle = models.CharField(max_length=255, verbose_name="Подзаголовок")
    title = models.CharField(max_length=255, verbose_name="Заголовок")
    is_published = models.BooleanField(verbose_name="Опубликовано", default=False)
    number = models.IntegerField(verbose_name="Номер")


    class Meta:
        verbose_name = "Предложение"
        verbose_name_plural = "Предложения"
        ordering = ["number",]

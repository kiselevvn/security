from django.db import models


class Service(models.Model):
    """
    Услуга
    """

    number = models.IntegerField(verbose_name="Номер")
    picture = models.ImageField(verbose_name="Картинка", blank=True, null=True)
    name = models.CharField(max_length=255, verbose_name="Наименование")
    text = models.TextField(verbose_name="Описание")
    is_published = models.BooleanField(verbose_name="Опубликовано", default=False)

    class Meta:
        verbose_name = "Услуга"
        verbose_name_plural = "Услуги"
        ordering = ["number",]

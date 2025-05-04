from django.db import models


class Order(models.Model):
    """
    Заявка
    """

    class StatusEnum(models.IntegerChoices):
        NEW = 1, "Новое"
        WORK = 2, "В работе"
        CLOSE = 3, "Закрыта"

    name = models.CharField(max_length=255, verbose_name="Имя")
    number = models.CharField(max_length=25, verbose_name="Номер телефона")
    text = models.TextField(verbose_name="Текст", blank=True, null=True)
    status = models.PositiveSmallIntegerField(
        verbose_name="Статус",
        choices=StatusEnum,
        default=StatusEnum.NEW,
    )
    created_at = models.DateTimeField(verbose_name="Дата создания", auto_now_add=True)

    class Meta:
        verbose_name = "Заявка"
        verbose_name_plural = "Заявки"

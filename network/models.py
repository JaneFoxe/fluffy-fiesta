from django.core.exceptions import ValidationError
from django.db import models

NULL_PARAM = {"null": True, "blank": True}


class Contact(models.Model):
    """Модель контакта"""

    email = models.EmailField(max_length=250, verbose_name="Почта", **NULL_PARAM)
    country = models.CharField(max_length=250, verbose_name="Страна", **NULL_PARAM)
    city = models.CharField(max_length=250, verbose_name="Город", **NULL_PARAM)
    street = models.CharField(max_length=250, verbose_name="Улица", **NULL_PARAM)
    house_number = models.CharField(
        max_length=25, verbose_name="Номер дома", **NULL_PARAM
    )

    def __str__(self):
        return f"{self.country} - {self.email}"

    class Meta:
        verbose_name = "Контакт"
        verbose_name_plural = "Контакты"


class Network(models.Model):
    LEVEL_CHOICES = (
        (0, "Завод"),
        (1, "Розничная сеть"),
        (2, "Индивидуальный предприниматель"),
    )
    name = models.CharField(max_length=250, verbose_name="Название")
    contact = models.ForeignKey(
        Contact,
        on_delete=models.SET_NULL,
        verbose_name="Контакты",
        **NULL_PARAM,
    )
    provider = models.ForeignKey(
        "self", on_delete=models.SET_NULL, **NULL_PARAM, verbose_name="Поставщик"
    )
    level = models.IntegerField(
        choices=LEVEL_CHOICES, verbose_name="Уровень в иерархии"
    )
    arrears = models.DecimalField(
        "Задолженность", max_digits=10, decimal_places=2, **NULL_PARAM
    )
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name="Дата создания", **NULL_PARAM
    )

    def get_level(self):
        level = 0
        net = self
        while net.provider:
            level += 1
            net = net.provider
        return level

    def clean(self):
        super().clean()
        if self.get_level() > 2:
            raise ValidationError("Максимальная иерархия не должна превышать 3 звена")

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = "Сеть"
        verbose_name_plural = "Сети"


class Product(models.Model):
    name = models.CharField(max_length=250, verbose_name="Название")
    model_name = models.CharField(max_length=250, verbose_name="Модель", **NULL_PARAM)
    release_date = models.DateTimeField(
        auto_now_add=True, verbose_name="Дата выхода на рынок"
    )
    network = models.ForeignKey(
        Network,
        on_delete=models.CASCADE,
        verbose_name="Сеть",
        related_name="network_products_set",
    )

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"

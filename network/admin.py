from django.contrib import admin
from django.urls import reverse

from network.models import Network, Product, Contact


@admin.register(Network)
class NetworkAdmin(admin.ModelAdmin):
    """
    Админ-класс для модели Network.

    Управляет отображением и функциональностью объектов Network в админ-панели.
    Включает возможность фильтрации по городу контакта, очистку задолженности
    перед поставщиком и отображение кликабельной ссылки на поставщика.

    Атрибуты:
        list_display (tuple): Поля для отображения в списке объектов.
        list_filter (tuple): Поля для фильтрации объектов.
        actions (list): Список доступных действий в админке.
    """

    list_display = (
        "name",
        "contact",
        "view_providers_link",
        "level",
        "arrears",
        "created_at",
    )
    list_filter = ("contact__city",)
    actions = ["clear_arrear"]

    def clear_arrear(self, request, queryset):
        """
        Админ-действие для обнуления задолженности перед поставщиком.

        Этот метод обновляет задолженность для выбранных объектов Network, устанавливая ее в 0.

        """
        queryset.update(arrears=0)

    clear_arrear.short_description = "Очистить задолженность перед поставщиком"

    def view_providers_link(self, obj):
        """
        Отображает кликабельную ссылку на страницу редактирования поставщика.

        Если объект Network имеет связанного поставщика, возвращает HTML-ссылку,
        ведущую на страницу редактирования этого поставщика в админ-панели. Если
        поставщик не указан, возвращает '-'.

        Параметры:
            obj (Network): Объект Network, для которого генерируется ссылка.

        Возвращает:
            str: HTML-код ссылки на поставщика или '-'.
        """
        if obj.provider:
            from django.utils.html import format_html

            url = reverse("admin:network_network_change", args=[obj.provider.id])
            return format_html('<a href="{}">{}</a>', url, obj.provider.name)
        return "-"

    view_providers_link.short_description = "Поставщик"


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """
    Админ-класс для модели Product.

    Управляет отображением и функциональностью объектов Product в админ-панели.

    Атрибуты:
        list_display (tuple): Поля для отображения в списке объектов.
    """

    list_display = (
        "name",
        "model_name",
        "release_date",
        "network",
    )


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    """
    Админ-класс для модели Contact.

    Управляет отображением и функциональностью объектов Contact в админ-панели.

    Атрибуты:
        list_display (tuple): Поля для отображения в списке объектов.
    """

    list_display = (
        "email",
        "country",
        "city",
        "street",
        "house_number",
    )

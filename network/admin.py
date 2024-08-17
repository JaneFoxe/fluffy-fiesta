from django.contrib import admin
from django.urls import reverse

from network.models import Network, Product, Contact


@admin.register(Network)
class NetworkAdmin(admin.ModelAdmin):
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
        queryset.update(arrear=0)

        self.clear_arrear.short_description = "Очистить задолженность перед поставщиком"

    def view_providers_link(self, obj):
        if obj.provider:
            from django.utils.html import format_html

            url = reverse("admin:network_network_change", args=[obj.provider.id])
            return format_html('<a href="{}">{}</a>', url, obj.provider.name)
        return "-"

    view_providers_link.short_description = "Поставщик"


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "model_name",
        "release_date",
        "network",
    )


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = (
        "email",
        "country",
        "city",
        "street",
        "house_number",
    )

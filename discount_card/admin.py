from django.contrib import admin
from django.utils.html import format_html

from discount_card.models import Card, Item, Purchase


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ("title", "price", "amount")


@admin.register(Purchase)
class PurchaseAdmin(admin.ModelAdmin):
    list_display = ("card", "total_sum", "date", "get_items")

    def get_items(self, obj: Purchase):
        output = [item.title for item in obj.items.all()]
        return format_html("<br />".join(output))


@admin.register(Card)
class CardAdmin(admin.ModelAdmin):
    list_display = ("series", "number", "release_date", "total_sum", "status")

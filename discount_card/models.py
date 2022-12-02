from django.db import models


class Item(models.Model):
    title = models.CharField(max_length=255)
    price = models.FloatField()
    amount = models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.title


class Purchase(models.Model):
    card = models.ForeignKey(
        "Card", on_delete=models.CASCADE, related_name="purchases"
    )
    total_sum = models.FloatField()
    date = models.DateTimeField()
    items = models.ManyToManyField("Item")

    def __str__(self):
        return self.total_sum


class Card(models.Model):
    class Statuses(models.TextChoices):
        ACTIVE = "Active"
        INACTIVE = "Inactive"
        EXPIRED = "Expired"

    series = models.CharField(max_length=3)
    number = models.IntegerField()
    release_date = models.DateTimeField()
    expiry_date = models.DateTimeField()
    total_sum = models.FloatField()
    status = models.CharField(
        max_length=30, choices=Statuses.choices, default=Statuses.INACTIVE
    )

    def __str__(self):
        return f"{self.series}-{self.number}"

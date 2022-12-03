import random

from dateutil.relativedelta import *
from django.core.validators import MinLengthValidator
from django.db import models
from django.db.models import Sum
from django.utils import timezone


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
    total_sum = models.FloatField(blank=True, null=True)
    date = models.DateTimeField()
    items = models.ManyToManyField("Item")

    def __str__(self):
        return str(self.card.number)

    def save(self, *args, **kwargs):
        if self.pk:
            total_sum = self.items.all().aggregate(Sum("price"))["price__sum"]
            self.total_sum = total_sum
        super().save(*args, **kwargs)


class Card(models.Model):
    class Statuses(models.TextChoices):
        ACTIVE = "Active"
        INACTIVE = "Inactive"
        EXPIRED = "Expired"

    series = models.CharField(
        max_length=3,
        validators=[MinLengthValidator(3)],
        help_text="Only 3 letters",
    )
    number = models.IntegerField(
        max_length=10,
        validators=[MinLengthValidator(10)],
        help_text="Only 10 digits",
    )
    release_date = models.DateTimeField()
    expiry_date = models.DateTimeField()
    total_sum = models.FloatField(default=0)
    status = models.CharField(
        max_length=30, choices=Statuses.choices, default=Statuses.INACTIVE
    )

    @staticmethod
    def generate_card_number():
        return random.randint(1000000000, 9999999999)

    @staticmethod
    def generate_card(series, validity_term):
        Card.objects.create(
            series=series,
            number=Card.generate_card_number(),
            release_date=timezone.now(),
            expiry_date=timezone.now() + relativedelta(months=+validity_term),
            total_sum=0,
            status=Card.Statuses.INACTIVE,
        )

    def check_card(self):
        """Call this method before every action with the map."""
        if self.expiry_date > timezone.now():
            self.status = Card.Statuses.EXPIRED
            self.save()

    def __str__(self):
        return f"{self.series}-{self.number}"

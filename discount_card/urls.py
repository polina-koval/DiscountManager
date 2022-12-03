from django.urls import path

from discount_card.views import CardCreate

urlpatterns = [path("", CardCreate.as_view(), name="card_create")]

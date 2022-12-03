from django.urls import path

from discount_card.views import (
    CardCreate,
    CardDeleteView,
    CardDetail,
    CardListView,
    CardUpdateView,
    SearchResultsView,
)

urlpatterns = [
    path("generate_cards/", CardCreate.as_view(), name="card_create"),
    path("cards/", CardListView.as_view(), name="card_list"),
    path("card/<pk>/", CardDetail.as_view(), name="card_detail"),
    path("card/<pk>/delete/", CardDeleteView.as_view(), name="card_delete"),
    path("card/<pk>/update/", CardUpdateView.as_view(), name="card_update"),
    path("search/", SearchResultsView.as_view(), name="search_results"),
]

from django.db.models import Q
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import (
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
    View,
)

from discount_card.forms import CardForm
from discount_card.models import Card


class CardCreate(View):
    template_name = "discount_card/card_create.html"

    def get(self, request):
        form = CardForm()
        return render(request, self.template_name, {"form": form})

    def post(self, request):
        form = CardForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            for i in range(data["amount"]):
                Card.generate_card(
                    series=data["series"],
                    validity_term=int(data["validity_term"]),
                )
            return HttpResponseRedirect(reverse("card_create"))
        return render(request, self.template_name, {"form": form})


class CardListView(ListView):

    model = Card
    template_name = "discount_card/card_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cards"] = Card.objects.all()
        return context


class CardDetail(DetailView):
    model = Card
    context_object_name = "card"
    template_name = "discount_card/card_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        card = context["card"]
        card.check_card()
        return context


class CardDeleteView(DeleteView):
    model = Card
    template_name = "discount_card/card_delete.html"

    def get_success_url(self):
        return reverse("card_list")


class CardUpdateView(UpdateView):
    model = Card
    fields = ["status"]

    def get_success_url(self):
        pk = self.kwargs["pk"]
        return reverse("card_detail", kwargs={"pk": pk})


class SearchResultsView(ListView):
    model = Card
    template_name = "discount_card/search_result.html"
    queryset = Card.objects.all()

    def get_queryset(self):
        """Search by series, number, release date, expiry_date, status"""
        query = self.request.GET.get("q")
        object_list = Card.objects.filter(
            (
                Q(series__icontains=query)
                | Q(number__icontains=query)
                | Q(release_date__icontains=query)
                | Q(expiry_date__icontains=query)
                | Q(status__icontains=query)
            )
        )
        return object_list

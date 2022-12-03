from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import View

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

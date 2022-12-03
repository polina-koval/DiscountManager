from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import View

from discount_card.forms import CardForm


class CardCreate(View):
    template_name = "discount_card/card_create.html"

    def get(self, request):
        form = CardForm()
        return render(request, self.template_name, {"form": form})

    def post(self, request):
        form = CardForm(request.POST)
        if form.is_valid():
            # Do something with the form data
            print(form.cleaned_data)
            return HttpResponseRedirect(reverse("card_create"))
        return render(request, self.template_name, {"form": form})

from django import forms


class CardForm(forms.Form):
    TERMS = (
        (12, "1 YEAR"),
        (6, "6 MONTHS"),
        (1, "1 MONTH"),
    )

    series = forms.CharField(max_length=3, required=True)
    amount = forms.IntegerField(required=True)
    validity_term = forms.ChoiceField(choices=TERMS, required=True)

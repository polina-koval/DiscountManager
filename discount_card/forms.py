from django import forms


class CardForm(forms.Form):
    TERMS = (
        ("1_YEAR", 12),
        ("6_MONTH", 6),
        ("1_MONTH", 1),
    )

    series = forms.CharField(max_length=3, required=True)
    amount = forms.IntegerField(required=True)
    validity_term = forms.ChoiceField(choices=TERMS, required=True)

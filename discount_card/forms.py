from django import forms


class CardForm(forms.Form):
    TERMS = (
        (12, "1 YEAR"),
        (6, "6 MONTHS"),
        (1, "1 MONTH"),
    )

    series = forms.CharField(
        min_length=3,
        max_length=3,
        required=True,
        help_text="Please, write 3 letters",
    )
    amount = forms.IntegerField(required=True, min_value=1)
    validity_term = forms.ChoiceField(choices=TERMS, required=True)

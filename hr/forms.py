import django.forms as forms


class InterestForm(forms.Form):
    # fields
    amount = forms.FloatField(label="Loan Amount")
    rate = forms.FloatField(label="Interest Rate")

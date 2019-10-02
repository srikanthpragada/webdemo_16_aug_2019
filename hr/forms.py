import django.forms as forms
from .models import Employee
from django.forms import ModelForm


class InterestForm(forms.Form):
    # fields
    amount = forms.FloatField(label="Loan Amount")
    rate = forms.FloatField(label="Interest Rate")

    # custom validation
    def clean_rate(self):
        rate = float(self.cleaned_data['rate'])
        if rate < 5 or rate > 15:
            raise forms.ValidationError('Invalid interest rate!')

        return rate


class EmployeeForm(ModelForm):
    class Meta:
        model = Employee
        fields = ('fullname','job','salary')
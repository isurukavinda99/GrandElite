from django import forms

from allowances.models import Allowances


class AllowancesForm(forms.ModelForm):
    class Meta:
        model = Allowances
        fields = "__all__"

    error_messages = {
        'description': {'required': 'This field cannot be empty'},
        'amount': {'required': 'This field cannot be empty'},

    }

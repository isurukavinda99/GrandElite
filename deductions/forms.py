from django import forms

from deductions.models import Deductions


class DeductionsForm(forms.ModelForm):
    class Meta:
        model = Deductions
        fields = "__all__"

        error_messages = {
            'description': {'required': 'This field cannot be empty'},
            'amount': {'required': 'This field cannot be empty'},

        }

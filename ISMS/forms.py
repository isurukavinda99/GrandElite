from django.forms import ModelForm
from .models import *
from django import forms


class CategoryForm(ModelForm):
    class Meta:
        model = Category
        exclude = ('created_at' , 'updated_at' ,)


class ItemForm(ModelForm):
    class Meta:
        model = Item
        exclude = ('created_at' , 'updated_at' ,'suppliers' ,)

class SupplerForm(ModelForm):
    class Meta:
        model= Supplier
        exclude = ('created_at' , 'updated_at' ,)


class SendEmailForm(ModelForm):
    class Meta:
        model = SendMail
        exclude = ('request_date' , )

class ReleaseItemForm(ModelForm):
    class Meta:
        model = ItemReleaseTicket
        fields = ['item', 'released_quantity' , 'comment' , 'released_to']


class GenerateInvoice(ModelForm):

    emailRequest = forms.ModelChoiceField(queryset=SendMail.objects.filter(status="requested"))

    class Meta:
        model = ConfirmedInvoice
        fields = ['emailRequest' , 'offered_price']


from django.forms import ModelForm
from .models import *

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
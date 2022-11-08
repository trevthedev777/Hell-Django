from django import forms
from .models import Item


class ItemForm(forms.ModelForm):
    # This inner class gives the form more data about itself
    class Meta:
        model = Item
        fields = ['name', 'done']

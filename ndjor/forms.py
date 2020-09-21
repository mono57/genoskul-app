from django import forms

from ndjor.models import Product

class ProductModelForm(forms.ModelForm):
    class Meta: 
        model = Product
        fields = '__all__'
        exclude = ('owner', )
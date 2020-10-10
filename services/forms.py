from django import forms

from services.models import Box

class ServiceModelForm(forms.ModelForm):
    class Meta:
        model = Box
        exclude = ('owner','confirmed')
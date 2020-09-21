from django import forms

from learning.models import Document

class DocumentModelForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ('file', 'type', 'categories', 'description')
        widgets = {
            'description': forms.Textarea(attrs={'rows':3})
        }
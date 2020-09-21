from django import forms

from jobs.models import Job, Resume, JobType, JobCategory


class JobModelForm(forms.ModelForm):
    # Company details form
    company_name = forms.CharField(
        label='Nom de l\'entreprise',
        widget=forms.TextInput(attrs={'placeholder': 'Entrez le nom de l\'entreprise'}))
    website = forms.URLField(label='Site internet',
                             required=False,
                             widget=forms.TextInput(
                                 attrs={'placeholder': 'https://'}))
    tagline = forms.CharField(
        label='Petite description', required=False, widget=forms.TextInput())
    logo = forms.ImageField(label='Logo de l\'entreprise', required=False,
                            widget=forms.FileInput())

    class Meta:
        model = Job
        exclude = ('company', 'user')
        widgets = {
            'description': forms.Textarea(attrs={'rows': 3}),
            'category': forms.SelectMultiple(
                attrs={'class': 'chosen-select', 'data-placeholder': 'Choisissez une catégorie'})
        }


class ResumeModelForm(forms.ModelForm):
    class Meta:
        model = Resume
        exclude = ('user',)
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4})
        }
        labels = {
            'resume_file': 'Joindre un CV'
        }


class JobFilterForm(forms.Form):
    type = forms.ChoiceField(
        required=False,
        label="Type de l'emploi",
        widget=forms.Select(attrs={
            'class': 'chosen-select-no-single',
            'data-placeholder': 'Choisissez un type'
        }))
    location = forms.CharField(
        required=False,
        label="Lieu d'exécution",
        widget=forms.TextInput(
            attrs={'placeholder': 'Entrez un nom de ville ou pays'})
    )

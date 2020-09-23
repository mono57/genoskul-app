from django import forms

from accounts.models import Profile


class RegisterStep2ModelForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ('user', 'avatar')
        help_texts = {
            'birthday': 'Entrez la date sous le format: <span class=\'text-primary\'>jour/mois/année</span>'
        }


class ProfileModelForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ('user', )

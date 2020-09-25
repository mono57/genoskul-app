from django import forms
from django.contrib.auth import get_user_model

from accounts.models import Profile


User = get_user_model()


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


class UserInfoForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username','first_name', 'last_name', )


    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError('Ce nom d\'utilisateur existe déjà !')
    
        return username
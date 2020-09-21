from django import forms

from accounts.models import Profile


class RegisterStep2ModelForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ('user', 'avatar')



class ProfileModelForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ('user', )

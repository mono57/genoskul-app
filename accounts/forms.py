from django import forms
from django.contrib.auth import get_user_model
from allauth.account.forms import SignupForm

from accounts.models import Profile, Profession


User = get_user_model()

occupations_choices = (
    ('student', 'Etudiant'),
    ('shool_student', 'Elève'),
    ('others', 'Autres'),
)


class RegisterForm(SignupForm):
    profession = forms.ChoiceField(
        label='Profession', choices=[(p.pk, p.name) for p in Profession.objects.all()], required=True)
    


class SchoolStudentModelForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ('user', 'avatar', 'speciality', 'profession')
        help_texts = {
            'birthday': 'Entrez la date sous le format: <span class=\'text-primary\'>jour/mois/année</span>'
        }
        labels = {
            'residence': 'Pays de residence *',
            'nationality': 'Nationalité *',
            'school_student_level': 'Classe *',
            'birthday': 'Date de naissance *',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['school_student_level'].widget.attrs.update({'required': True})
        self.fields['nationality'].widget.attrs.update({'required': True})
        self.fields['residence'].widget.attrs.update({'required': True})
        self.fields['birthday'].widget.attrs.update({'required': True})

class StudentModelForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ('user', 'avatar', 'school_student_level', 'profession')
        help_texts = {
            'birthday': 'Entrez la date sous le format: <span class=\'text-primary\'>jour/mois/année</span>'
        }
        labels = {
            'residence': 'Pays de residence *',
            'nationality': 'Nationalité *',
            'speciality': 'Spécialité *',
            'birthday': 'Date de naissance *',
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['speciality'].widget.attrs.update({'required': True})
        self.fields['nationality'].widget.attrs.update({'required': True})
        self.fields['residence'].widget.attrs.update({'required': True})
        self.fields['birthday'].widget.attrs.update({'required': True})

class UserInfoForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', )

    # def clean_username(self):
    #     username = self.cleaned_data.get('username')
    #     if User.objects.filter(username=username).exists():
    #         raise forms.ValidationError('Ce nom d\'utilisateur existe déjà !')

    #     return username

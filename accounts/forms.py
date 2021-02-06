from django import forms
from django.contrib.auth import get_user_model
from allauth.account.forms import SignupForm

from accounts.models import Profile, SchoolStudentProfile, UserProfile


User = get_user_model()

occupations_choices = (
    ('student', 'Etudiant'),
    ('shool_student', 'Elève'),
    ('others', 'Autres'),
)

class RegisterForm(SignupForm):
    occupation = forms.ChoiceField(label="Profession", choices=occupations_choices)


class RegisterSchoolStudent(forms.ModelForm):
    class Meta:
        model = SchoolStudentProfile
        exclude = ('user', 'avatar')

class RegisterStep2ModelForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        exclude = ('user', 'avatar')
        help_texts = {
            'birthday': 'Entrez la date sous le format: <span class=\'text-primary\'>jour/mois/année</span>'
        }


class ProfileModelForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        exclude = ('user', )


class UserInfoForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', )


    # def clean_username(self):
    #     username = self.cleaned_data.get('username')
    #     if User.objects.filter(username=username).exists():
    #         raise forms.ValidationError('Ce nom d\'utilisateur existe déjà !')
    
    #     return username

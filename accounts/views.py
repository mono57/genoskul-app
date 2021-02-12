from django.urls.base import reverse_lazy
from accounts.models import Profile, Profession
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, FormView, UpdateView
from django.urls import reverse
from django.contrib.auth import get_user, get_user_model
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from allauth.account.views import SignupView as AllauthSignupView
# from allauth.account.forms import SignupForm
from forum.models import ForumRegistration, Forum
from accounts.forms import (
    SchoolStudentModelForm,
    StudentModelForm, User, UserInfoForm, RegisterForm)

User = get_user_model()


class SignupView(AllauthSignupView):
    template_name = 'account/signup.html'
    form_class = RegisterForm
    user_username = None

    def get_success_url(self):
        if self.user_username is not None:
            user = get_object_or_404(User, username=self.user_username)
            profile = user.profile
            profile.profession = self.profession_pk
            profile.save()
        return reverse('accounts:profile-completion')

    def form_valid(self, form):
        cleaned_data = form.cleaned_data
        self.user_username = cleaned_data.get('username')
        self.profession_pk = cleaned_data.get('profession')
        return super().form_valid(form)


class ProfileCompletionUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    template_name = 'accounts/profile-completion.html'
    success_message = 'Bienvenue sur Genoskul'
    model = Profile

    def get_object(self, queryset=None):
        return self.request.user.profile

    def get_success_url(self):
        self.set_user_to_forum()
        return reverse('dashboard:dashboard')

    def get_form_class(self):
        if self.request.user.profile.profession.name == "Elève":
            return SchoolStudentModelForm
        return StudentModelForm

    def set_user_to_forum(self):
        profile = self.get_object()
        if not ForumRegistration.objects.filter(user=profile).exists():
            forum = Forum.objects.get(name=profile.speciality.name)\
                if profile.is_student else Forum.objects.get(
                    name=profile.school_student_level.level)

            ForumRegistration.objects.create(
                forum=forum,
                user=profile.user
            )
            return True
        return False

class ProfileUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    template_name = 'accounts/profile.html'
    # form_class = ProfileModelForm
    success_message = 'Vos informations ont été bien mis à jour !'

    def get_object(self):
        return self.request.user.profile

    def get_form_class(self):
        if self.get_object().profession.name == 'Elève':
            return SchoolStudentModelForm
        return StudentModelForm

    def get_queryset(self):
        return self.request.user.profile

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Modifiez votre profil'
        context['profile'] = self.request.user.profile
        return context

    def get_success_url(self):
        return reverse('dashboard:profile-update')

    # def get_initial(self):
    #     profile = self.request.user.profile
    #     initial = super().get_initial()
    #     initial.update({
    #         'residence': profile.residence,
    #         'nationality': profile.nationality,
    #         'gender': profile.gender,
    #         'birthday': profile.birthday,
    #         'avatar': profile.avatar,
    #         'telephone': profile.telephone
    #     })
    #     return initial

    # def form_valid(self, form):
    #     data = form.cleaned_data
    #     profile = self.request.user.profile
    #     profile.residence = data.get('residence')
    #     profile.nationality = data.get('nationality')
    #     profile.gender = data.get('gender')
    #     profile.birthday = data.get('birthday')
    #     profile.avatar = data.get('avatar')
    #     profile.function = data.get('function')
    #     profile.save()
    #     return super().form_valid(form)


class UserInfoUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    template_name = 'accounts/user_info.html'
    form_class = UserInfoForm
    context_object_name = 'user'

    def get_object(self):
        return self.request.user

    def get_success_url(self):
        return reverse('accounts:user_info-update', kwargs={'pk': self.kwargs.get('pk')})

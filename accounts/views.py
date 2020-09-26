from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, FormView, UpdateView
from django.urls import reverse
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from allauth.account.views import SignupView as AllauthSignupView
from allauth.account.forms import SignupForm

from accounts.forms import ProfileModelForm, RegisterStep2ModelForm, UserInfoForm


class SignupView(AllauthSignupView):
    template_name = 'account/signup.html'
    form_class = SignupForm
    
    def get_success_url(self):
        return reverse('accounts:register-step2')


class RegisterStep1(LoginRequiredMixin, FormView):
    template_name = 'accounts/register-step2.html'
    form_class = RegisterStep2ModelForm

    def get_success_url(self):
        return reverse('dashboard:dashboard')

    def form_valid(self, form):
        data = form.cleaned_data
        profile = self.request.user.profile
        profile.residence = data.get('residence')
        profile.nationality = data.get('nationality')
        profile.gender = data.get('gender')
        profile.birthday = data.get('birthday')
        profile.telephone = data.get('telephone')
        profile.function = data.get('function')
        profile.save()

        messages.success(self.request, 'Bienvenue sur Genoskul !')

        return super().form_valid(form)


class ProfileUpdateView(LoginRequiredMixin, SuccessMessageMixin, FormView):
    template_name = 'accounts/profile.html'
    form_class = ProfileModelForm
    success_message = 'Vos informations ont été bien mis à jour !'

    def get_queryset(self):
        return self.request.user.profile

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Modifiez votre profil'
        context['profile'] = self.request.user.profile
        return context

    def get_success_url(self):
        return reverse('dashboard:profile-update')

    def get_initial(self):
        profile = self.request.user.profile
        initial = super().get_initial()
        initial.update({
            'residence': profile.residence,
            'nationality': profile.nationality,
            'gender': profile.gender,
            'birthday': profile.birthday,
            'avatar': profile.avatar,
            'function': profile.function
        })
        return initial

    def form_valid(self, form):
        data = form.cleaned_data
        profile = self.request.user.profile
        profile.residence = data.get('residence')
        profile.nationality = data.get('nationality')
        profile.gender = data.get('gender')
        profile.birthday = data.get('birthday')
        profile.avatar = data.get('avatar')
        profile.function = data.get('function')
        profile.save()
        return super().form_valid(form)


class UserInfoUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    template_name = 'accounts/user_info.html'
    form_class = UserInfoForm
    context_object_name = 'user'
    
    def get_object(self):
        return self.request.user


    def get_success_url(self):
        return reverse('accounts:user_info-update', kwargs={'pk': self.kwargs.get('pk')})
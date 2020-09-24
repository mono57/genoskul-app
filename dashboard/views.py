from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy, reverse
from django.views.generic import (
    ListView,
    CreateView,
    TemplateView,
    UpdateView
)

from jobs.forms import JobModelForm, ResumeModelForm
from jobs.models import Company, Job, Resume
from learning.models import Document
from services.forms import ServiceModelForm


class DashboardTemplateView(LoginRequiredMixin, TemplateView):
    template_name = 'dashboard/dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class DashboardDocumentListView(LoginRequiredMixin, ListView):
    model = Document
    context_object_name = 'documents'
    template_name = 'dashboard/documents.html'
    paginate_by = 10

    def get_queryset(self):
        return self.request.user.documents.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Mes documents'
        return context


class DashboardJobCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    form_class = JobModelForm
    template_name = 'dashboard/job-create.html'
    success_url = reverse_lazy('dashboard:job-create')
    success_message = 'Votre offre a été ajoutée avec succès !'

    def form_valid(self, form):
        data = form.cleaned_data
        company = Company.objects.create(
            name=data.get('company_name'),
            website=data.get('website'),
            logo=form.files.get('logo'),
            tagline=data.get('tagline'),
        )
        obj = form.save(commit=False)
        obj.company = company
        obj.user = self.request.user
        obj.save()
        return super().form_valid(form)


class DashboardResumeCreateView(
        LoginRequiredMixin,
        SuccessMessageMixin,
        CreateView):
    template_name = 'dashboard/profile-add.html'
    form_class = ResumeModelForm
    success_url = reverse_lazy('dashboard:resume-create')
    success_message = 'Votre CV a été déposé avec succès !'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Ajouter un CV'
        return context

    def form_invalid(self, form):
        print(form.errors)
        return super().form_invalid(form)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.user = self.request.user
        print(form.data)
        obj.save()
        return super().form_valid(form)


class DashboardResumeUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    template_name = 'dashboard/profile-add.html'
    form_class = ResumeModelForm
    success_message = 'Votre CV a été bien mis à jour !'
    success_url = reverse_lazy('dashboard:resume-update')

    def get_object(self):
        return get_object_or_404(Resume, pk=self.kwargs.get('pk'))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Modifier votre CV'
        return context


class DashboardJobUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    template_name = 'dashboard/job-create.html'
    model = Job
    form_class = JobModelForm
    context_object_name = 'job'
    success_message = 'Votre offre d\'emploi a été modifiée avec succès !'

    def get_success_url(self):
        return reverse('dashboard:job-update', kwargs={'pk': self.kwargs.get('pk')})

    def get_initial(self):
        company = self.get_object().company
        initial = super().get_initial()
        initial.update({
            'company_name': company.name,
            'website': company.website,
            'logo': company.logo,
            'tagline': company.tagline
        })
        return initial

    def form_valid(self, form):
        data = form.data
        obj = form.save()
        company = obj.company
        print(data)
        company.name = data.get('company_name')
        company.website = data.get('website')
        company.tagline = data.get('tagline')
        company.logo = form.files.get('logo')
        company.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Modification de l\'offre d\'emploi'
        return context


class DashboardProductListView(LoginRequiredMixin, ListView):
    template_name = 'dashboard/products.html'
    context_object_name = 'products'

    def get_queryset(self):
        return self.request.user.products.all()


class DashboardServiceCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    template_name = 'services/service-form.html'
    form_class = ServiceModelForm
    success_url = reverse_lazy('dashboard:dashboard')
    success_message = "Votre demande a été bien reçu, veuillez patienter pendant que nous validons! "

    def form_valid(self, form):
        obj = form.save()
        obj.owner = self.request.user
        obj.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Créer un service'
        return context
        
# class DashboardServiceCreateView(LoginRequiredMixin, SuccessMessageMixin, Update):
#     template_name = 'services/service-form.html'
#     form_class = ServiceModelForm
#     success_url = reverse_lazy('dashboard:service-update')
#     success_message = "Votre demande a été bien reçu, veuillez patienter pendant que nous validons! "

#     def get_object(self):
#         return get_object_or_404(Box, pk=self.kwargs.get('pk'))

#     def get_context_data(self):
#         context = super().get_context_data(**kwargs)
#         context['title'] = 'Modifier votre demande'


class DashboardJobsListView(LoginRequiredMixin, ListView):
    template_name = 'dashboard/jobs.html'
    model = Job
    context_object_name = 'jobs'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Liste des offres d\'emploi'
        return context

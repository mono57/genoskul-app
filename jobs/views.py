from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView
)

from accounts.models import Profile
from jobs.models import Job, Resume
from jobs.forms import ResumeModelForm, JobFilterForm


class JobListView(ListView):
    template_name = 'jobs/jobs-list.html'
    model = Job
    context_object_name = 'jobs'
    paginate_by = 6

    def get(self, request, *args, **kwargs):
        self.type = request.GET.get('type', None)
        self.location = request.GET.get('location', None)
        return super().get(request, *args, **kwargs)

    def get_queryset(self):
        return self.model.objects.filter_by(self.type, self.location)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Liste des offres d\'emploi'
        context['form'] = JobFilterForm(self.request.GET)
        return context


class ResumeListView(ListView):
    template_name = 'jobs/profile-list.html'
    model = Resume
    context_object_name = 'resumes'
    paginate_by = 6

    def get(self, request, *args, **kwargs):
        self.query = request.GET.get('query', None)
        return super().get(request, *args, **kwargs)

    def get_queryset(self):
        return self.model.objects.search(query=self.query)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Profils disponibles'
        if self.query:
            context['query'] = self.query
        return context

class ResumeDetailView(DetailView):
    template_name = 'jobs/profile-detail.html'
    model = Resume
    context_object_name = 'profile'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Details CV {}'.format(self.get_object().user.get_full_name)
        return context


class JobDetailView(DetailView):
    template_name = 'jobs/job-detail.html'
    model = Job
    context_object_name = 'job'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.get_object().title
        return context
    
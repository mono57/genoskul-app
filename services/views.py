from django.shortcuts import render

from django.views.generic import (
    ListView,
    DetailView)


from services.models import BoxType
from services.models import Box

class BoxDetailView(DetailView):
    template_name = 'services/service-detail.html'
    model = Box
    context_object_name = 'services'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.get_object().title
        return context


class ServiceListView(ListView):
    template_name = 'services/list-services.html'
    model = Box
    context_object_name = 'services'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Liste des services"
        return context
# Create your views here.
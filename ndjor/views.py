from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy, reverse
from django.views.generic import (
    CreateView,
    ListView,
    UpdateView
)

from ndjor.forms import ProductModelForm
from ndjor.models import Product


class ProductCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    template_name = 'ndjor/product-form.html'
    form_class = ProductModelForm
    success_url = reverse_lazy('dashboard:product-create')
    success_message = "Votre produit a été ajouté avec succès !"

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.owner = self.request.user
        obj.save()
        return super().form_valid(form)


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Ajouter un produit'
        return context

class ProductListView(LoginRequiredMixin, ListView):
    template_name = 'ndjor/product-list.html'
    model = Product
    context_object_name = 'products'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Produits disponibles'
        return context

class ProductUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    template_name = 'ndjor/product-form.html'
    form_class = ProductModelForm
    model = Product
    context_object_name = 'product'
    success_message = 'Votre produit a été mis à jour'

    def get_success_url(self):
        return reverse('dashboard:product-update', kwargs={'pk': self.kwargs.get('pk')})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Modification du document'
        return context
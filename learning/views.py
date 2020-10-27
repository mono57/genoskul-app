from django.shortcuts import render ,get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse, reverse_lazy
from django.views.generic import (
    CreateView,
    ListView,
    TemplateView,
    DetailView
)

from learning.models import Document, DocumentCategory
from learning.forms import DocumentModelForm


class DocumentCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    template_name = 'learning/document-form.html'
    form_class = DocumentModelForm
    success_url = reverse_lazy('dashboard:document-create')
    success_message = 'Votre document a été publié. Merci pour votre contribution ! 🙏🏾'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Publier un document'
        return context

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.user = self.request.user
        obj.save()
        return super().form_valid(form)

    

class DocumentListView(ListView):
    template_name = 'learning/document-list.html'
    model = Document
    context_object_name = 'documents'
    paginate_by = 12
    
    def get_object(self):
       return get_object_or_404(Document, self.kwargs.get('pk'))
        
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Liste des documents'
        return context
    

class DocumentCategoryListView(ListView):
    template_name = 'learning/doc_category-list.html'
    model = DocumentCategory
    context_object_name = 'doc_categories'
    paginate_by = 20

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Toutes les specialités disponibles'
        return context

class CourseListView(TemplateView):
    template_name = 'learning/course-list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Nos formations'
        return context

class CategoryDetailView(DetailView):
    template_name = 'learning/document-list.html'
    model = DocumentCategory
    context_object_name = 'doc_categories'

    #def get_object(self):
        #return get_object_or_404(Document, self.kwargs.get('pk'))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.get_object().name
        return context
        
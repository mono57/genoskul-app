from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, TemplateView, View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy, reverse
from django.utils.text import slugify


from blog.models import Post, PostCategory, Comment
from blog.forms import PostModelForm

import random

class PostCreateView(LoginRequiredMixin, CreateView):
    form_class = PostModelForm
    template_name = 'blog/post-form.html'
    success_url = reverse_lazy('blog:list')

    def form_valid(self, form):
        post_obj = form.save(commit=False)
        post_obj.creator = self.request.user
        post_obj.slug = slugify(post_obj.title)
        post_obj.save()
        return super().form_valid(form)


class PostListView(ListView):
    template_name = 'blog/post-list.html'
    model = Post
    context_object_name = 'posts'
    paginate_by = 21

    def get_queryset(self):
        posts = list(super().get_queryset())
        r_posts = []
        for i in range(len(posts)):
            choice = random.choice(posts)
            r_posts.append(choice)
            posts.remove(choice)

        return r_posts


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Généralités & Divertissement'
        return context

  

class PostDetailView(DetailView):
    template_name = 'blog/post-details.html'
    model = Post
    context_object_name = 'post'

    def get_object(self):
        return get_object_or_404(Post, pk=self.kwargs.get('pk'))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.get_object().title

        return context


class CategoryDetailView(DetailView):
    template_name = 'blog/post-list.html'
    model = PostCategory
    context_object_name = 'category'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Détails de la catégorie'
        return context

class ConsultSpecialite(TemplateView):
    template_name = 'blog/consult-specialiste.html'

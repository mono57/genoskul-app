from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse

from forum.models import Forum, ForumRegistration, Topic, Comment
from forum.forms import TopicModelForm, CommentModelForm


class ForumListView(LoginRequiredMixin, ListView):
    template_name = 'forum/forum-list.html'
    model = Forum
    context_object_name = 'forums'

    def get_queryset(self):
        return self.request.user.forums.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print(context)
        return context


class ForumDetailView(LoginRequiredMixin, DetailView):
    template_name = 'forum/forum-detail.html'
    model = Forum
    context_object_name = 'forum'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['registrations'] = self.request.user.forums.all()
        return context


class TopicDetailView(LoginRequiredMixin, DetailView):
    template_name = 'forum/topic-detail.html'
    model = Topic
    context_object_name = 'topic'

    def get_object(self):
        topic_pk = self.kwargs.get('topic_pk')
        return get_object_or_404(self.model, pk=topic_pk)


class TopicCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    template_name = 'forum/form.html'
    form_class = TopicModelForm
    success_message = 'Votre sujet a été ajouté'

    def get_success_url(self):
        return reverse(
            'forum:forum-detail',
            kwargs={'pk': self.kwargs.get('forum_pk')})

    def get_forum_object(self):
        return get_object_or_404(
            Forum,
            pk=self.kwargs.get('forum_pk'))

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.author = self.request.user
        obj.forum = self.get_forum_object()

        obj.save()

        return super().form_valid(form)

class CommentCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    template_name = 'forum/form.html'
    form_class = CommentModelForm
    success_message = 'Votre commentaire a été ajouté'

    def get_success_url(self):
        return reverse('forum:topic-detail', kwargs={
            'forum_pk': self.kwargs.get('forum_pk'),
            'topic_pk': self.kwargs.get('topic_pk')
        })

    def get_topic_object(self):
        return get_object_or_404(Topic, pk=self.kwargs.get('topic_pk'))

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.author = self.request.user
        obj.topic = self.get_topic_object()

        obj.save()

        return super().form_valid(form)
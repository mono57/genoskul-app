from django import forms

from forum.models import Comment, Topic


class TopicModelForm(forms.ModelForm):
    class Meta:
        model = Topic
        exclude = ('author', 'forum')


class CommentModelForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ('author', 'topic')


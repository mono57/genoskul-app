from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse

from genoskul.common.timestamp import TimeStampModel
from forum.managers import CommentManager, ForumManager

User = get_user_model()


class Forum(TimeStampModel):
    name = models.CharField(max_length=50, verbose_name='Nom du forum')
    description = models.TextField(
        blank=True, verbose_name='Description du forum')
    logo = models.ImageField(blank=True, null=True, upload_to='forums/logos/')
    visibility = models.CharField(max_length=20, default='private', choices=(
        ('private', 'Privé'), ('public', 'Public')), verbose_name='Visibilité')

    objects = ForumManager()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('forum:forum-detail', kwargs={'pk': self.pk})

    # def comments_count(self):
    #     return


class ForumRegistration(TimeStampModel):
    date = models.DateField(verbose_name='Date d\'inscription au forum', auto_now=True)
    is_admin = models.BooleanField(default=False, verbose_name='admin ?')
    forum = models.ForeignKey(
        Forum, on_delete=models.CASCADE, related_name='members')
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='forums')

    def __str__(self):
        return self.forum.name


class Topic(TimeStampModel):
    title = models.CharField(max_length=254, verbose_name='Titre')
    detail = models.TextField(verbose_name='Commentaire')
    author = models.ForeignKey(
        User, on_delete=models.CASCADE,
        verbose_name='Auteur',
        related_name='my_topics')
    forum = models.ForeignKey(
        Forum, on_delete=models.CASCADE,
        verbose_name='Forum',
        related_name='topics')

    class Meta:
        ordering = ('-created_at',)

    def __str__(self):
        return self.title

    # def get_absolute_url(self):
    #     return reverse('forum:topic-detail', kwargs={'fo'})

    def get_last_replied(self):
        replies = Comment.objects.get_comments_by_topic(self.pk)
        return replies.first()

    def get_last_replied_user(self):
        last_replied = self.get_last_replied()
        return last_replied.author if last_replied else None

    def get_last_replied_date(self):
        last_replied = self.get_last_replied()
        return last_replied.created_at if last_replied else None


class Comment(TimeStampModel):
    content = models.TextField(verbose_name='Contenu du commentaire')
    author = models.ForeignKey(
        User, on_delete=models.CASCADE,
        verbose_name='Auteur du commentaire',
        related_name='my_comments')

    topic = models.ForeignKey(
        Topic, on_delete=models.CASCADE,
        verbose_name='Sujet',
        related_name='comments')

    objects = CommentManager()

    class Meta:
        ordering = ('-created_at',)

    def __str__(self):
        return self.content

from django.db import models


class ForumManager(models.Manager):
    def get_public_forums(self):
        return self.get_queryset().filter(visibility='public')

    def get_not_registered_public_forums_by_user(self, user):
        user_forums = user.forums.all()
        qs = self.get_public_forums()
        return [forum for forum in qs if forum not in list(user_forums)]

# class ForumRegistration()
class CommentManager(models.Manager):
    def get_comments_by_topic(self, topic_pk):
        return self.get_queryset().filter(topic__pk=topic_pk)
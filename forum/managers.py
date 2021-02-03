from django.db import models

class CommentManager(models.Manager):
    def get_comments_by_topic(self, topic_pk):
        return self.get_queryset().filter(topic__pk=topic_pk)
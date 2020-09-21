from django.db import models
from django.db.models import Q


class JobManager(models.Manager):
    def filter_by(self, type=None, location=None):
        qs = self.get_queryset()
        if type == 'all':
            return qs

        if type or location:
            return qs.filter(
                Q(type=type) |
                Q(location__icontains=location) 
            )
        return qs

class ResumeManager(models.Manager):
    def search(self, query=None):
        qs = self.get_queryset()
        if query:
            return qs.filter(
                Q(pro_title__icontains=query) |
                Q(description__icontains=query) |
                Q(location__icontains=query)
            )
        return qs
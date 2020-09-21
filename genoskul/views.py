from django.views.generic import TemplateView

from jobs.models import Job, JobCategory
from learning.models import DocumentCategory, Document

class HomeTemplateView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['jobs'] = Job.objects.all()[:3]
        context['documents'] = Document.objects.all()[:4]

        return context
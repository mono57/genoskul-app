from django.views.generic import TemplateView

from jobs.models import Job, JobCategory
from learning.models import DocumentCategory, Document
from blog.models import Post
from services.models import Box
from us.models import SocialNetwork, Footer, About
from django.urls import reverse


class HomeTemplateView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['jobs'] = Job.objects.all().order_by('-created_at')[:3]
        context['categories'] = Document.objects.all()[:5]
        context['documents'] = DocumentCategory.objects.all()[:10]
        context['posts'] =Post.objects.all().order_by('-created_at')[:15]
        context['job_categories'] = JobCategory.objects.all()[:10]
        context['services'] = Box.objects.get_confirmed_services().order_by('-created_at')
        context['footer'] = Footer.objects.last()
        context['social_networks'] = SocialNetwork.objects.all()
        context['about'] = About.objects.last()

        return context
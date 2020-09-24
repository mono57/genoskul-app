from django.views.generic import TemplateView

from jobs.models import Job, JobCategory
from learning.models import DocumentCategory, Document
from blog.models import Post
from services.models import Box
from us.models import SocialNetwork, Footer, About


class HomeTemplateView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['jobs'] = Job.objects.all()[:3]
        context['documents'] = Document.objects.all()[:4]
        context['posts'] = Post.objects.all()[:3]
        context['job_categories'] = JobCategory.objects.all()[:8]
        context['services'] = Box.objects.get_confirmed_services()
        context['footer'] = Footer.objects.last()
        context['social_networks'] = SocialNetwork.objects.all()
        context['about'] = About.objects.last()

        return context
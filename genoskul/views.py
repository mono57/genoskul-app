from django.views.generic import TemplateView

from jobs.models import Job, JobCategory
from learning.models import DocumentCategory, Document
from blog.models import Post
from services.models import Box
from us.models import SocialNetwork, Footer, About
from django.urls import reverse

import random
 

def get_random_list(queryset):
    r_list = []
    for _ in range(len(queryset)):
        choice = random.choice(queryset)
        r_list.append(choice)
        queryset.remove(choice)

    return r_list
class HomeTemplateView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['jobs'] = Job.objects.all().order_by('-created_at')[:3]
        context['categories'] = Document.objects.all()[:5]
        context['documents'] = DocumentCategory.objects.all()[:10]
        context['document'] = Document.objects.all()[:10]
        context['job_categories'] = JobCategory.objects.all()[:10]
        context['services'] = get_random_list(
            list(Box.objects.get_confirmed_services().order_by('-created_at')))
        context['footer'] = Footer.objects.last()
        context['social_networks'] = SocialNetwork.objects.all()
        context['about'] = About.objects.last()
        context['posts'] = get_random_list(
            list(Post.objects.all().order_by('-created_at'))[:21])

        return context
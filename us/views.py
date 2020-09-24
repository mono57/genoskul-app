from django.shortcuts import render
from django.views.generic import TemplateView
from us.models import Privacy, TermOfService, About


class PrivacyTemplateView(TemplateView):
    template_name = 'privacy.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Politique de confidentialité'
        context['privacy'] = Privacy.objects.last()
        return context
        

class TermOfServiceTemplateView(TemplateView):
    template_name = 'terms.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Termes de services'
        context['term'] = TermOfService.objects.last()
        return context
    
class AboutTemplateView(TemplateView):
    template_name = 'about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "A propos de nous"
        context["about"] = About.objects.last()
        return context
    
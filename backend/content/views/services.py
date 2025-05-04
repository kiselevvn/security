from django.views.generic import TemplateView

from ..models import Service


class ServicesTemplateView(TemplateView):
    template_name = "pages/services.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['services'] = Service.objects.filter(is_published=True)
        return context

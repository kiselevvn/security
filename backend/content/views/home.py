from django.views.generic import TemplateView

from ..models import Offer, Review, Service


class HomeTemplateView(TemplateView):
    template_name = "pages/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['offers'] = Offer.objects.filter(is_published=True)
        context['reviews'] = Review.objects.filter(is_published=True)
        context['services'] = Service.objects.filter(is_published=True)
        return context

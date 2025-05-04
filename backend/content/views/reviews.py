from django.views.generic import TemplateView

from ..models import Offer, Review, Service


class ReviewsTemplateView(TemplateView):
    template_name = "pages/reviews.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['reviews'] = Review.objects.filter(is_published=True)
        return context

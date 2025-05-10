from django import forms
from django.views.generic.edit import FormView

from ..models import Review


class ReviewForm(forms.ModelForm):
    privacy = forms.BooleanField(required=True)

    class Meta:
        model = Review
        fields = [
            "name",
            "job",
            "text",
        ]


class ReviewCreateView(FormView):
    template_name = "pages/review.html"
    success_url = "/success-review/"
    form_class = ReviewForm
    
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
    
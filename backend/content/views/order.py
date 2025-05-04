from django import forms
from django.core.validators import MinLengthValidator
from django.views.generic.edit import FormView

from ..models import Order


class OrderForm(forms.ModelForm):
    privacy = forms.BooleanField(required=True)
    number = forms.CharField(required=True, validators=[MinLengthValidator(18)])

    class Meta:
        model = Order
        fields = [
            "name",
            "number",
            "text",
        ]


class OrderCreateView(FormView):
    template_name = "pages/order.html"
    success_url = "/success-order/"
    form_class = OrderForm


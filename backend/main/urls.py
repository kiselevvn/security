from content.views import (AboutView, HomeTemplateView, OrderCreateView,
                           ReviewCreateView, ReviewsTemplateView,
                           ServicesTemplateView)
from django.conf import settings
from django.contrib import admin
from django.urls import include, path, re_path
from django.views.generic import TemplateView

admin.site.site_header = "Горизонт безопасности"

urlpatterns = [

    path('', HomeTemplateView.as_view(), name="home"),
    path('order/', OrderCreateView.as_view(), name="order"),
    path('review/', ReviewCreateView.as_view(), name="review"),
    path('reviews/', ReviewsTemplateView.as_view(), name="reviews"),
    path('services/', ServicesTemplateView.as_view(), name="services"),
    path('about/', AboutView.as_view(), name="about"),
    path('admin/', admin.site.urls, name="admin"),
    path('privacy/', TemplateView.as_view(template_name="pages/privacy.html"), name="privacy"),
    path('success-order/', TemplateView.as_view(template_name="pages/success-order.html")),
    path('success-review/', TemplateView.as_view(template_name="pages/success-review.html")),
]


if settings.DEBUG:

    from django.conf.urls.static import static

    urlpatterns = (
        static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
        + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
        + urlpatterns
    )

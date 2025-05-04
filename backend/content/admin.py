from django.contrib import admin

from .models import Offer, Order, Review, Service


@admin.register(Offer)
class OfferAdmin(admin.ModelAdmin):
    list_display = [
        "title",
        "subtitle",
        "number",
        "is_published",
    ]
    list_filter = [
        "is_published",
    ]
    list_editable = [
        "number",
        "is_published",
    ]

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "text",
        "number",
        "is_published",
    ]
    list_filter = [
        "is_published",
    ]
    list_editable = [
        "number",
        "is_published",
    ]


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "number",
        "text",
        "status",
    ]
    list_filter = [
        "status",
    ]
    list_editable = [
        "status",
    ]

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "job",
        "text",
        "is_published"
    ]
    list_editable = [
        "is_published",
    ]

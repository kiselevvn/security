from .about import AboutView
from .home import HomeTemplateView
from .order import OrderCreateView
from .review import ReviewCreateView
from .reviews import ReviewsTemplateView
from .services import ServicesTemplateView

__all__ = [
    "HomeTemplateView",
    "OrderCreateView",
    "ReviewCreateView",
    "AboutView",
    "ReviewsTemplateView",
    "ServicesTemplateView",
]

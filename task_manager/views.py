from django.views.generic import TemplateView
from .models import User


class HomeView(TemplateView):
    template_name = "index.html"

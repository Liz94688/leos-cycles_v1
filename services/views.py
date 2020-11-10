from django.views.generic import ListView, DetailView
from .models import Level


class ServicesView(ListView):
    model = Level
    template_name = 'services/services.html'


class ServiceDetailView(DetailView):
    model = Level
    template_name = 'services/service_details.html'

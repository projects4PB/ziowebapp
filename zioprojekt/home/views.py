from django.views.generic.list import ListView

from places.models import RestCentre


class HomeView(ListView):
    model = RestCentre
    template_name = "home/home.html"

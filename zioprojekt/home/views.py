from django.views.generic.list import ListView

from places.models import TouristObject


class HomeView(ListView):
    model = TouristObject
    template_name = "home/home.html"

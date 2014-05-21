from django.views.generic.list import ListView

from zioprojekt.events.models import Event

from zioprojekt.places.models import TouristObject


class HomeView(ListView):
    model = TouristObject
    template_name = "home/home.html"

    def get_context_data(self, **kwargs):
        context = super(HomeView, self) \
            .get_context_data(**kwargs)

        events = Event.objects.all()

        context.update({
            'events': events
        })

        return context

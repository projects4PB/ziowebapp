from django.views.generic.list import ListView

from zioprojekt.events.models import Event

from zioprojekt.places.models import TouristObject


class HomeView(ListView):
    model = TouristObject
    template_name = "home/home.html"

    def get_queryset(self):
        qs = super(HomeView, self).get_queryset()

        return qs.order_by('-creation_date')[:5]

    def get_context_data(self, **kwargs):
        context = super(HomeView, self) \
            .get_context_data(**kwargs)

        events = Event.objects.all() \
            .order_by('-creation_date')[:5]

        context.update({
            'events': events
        })

        return context

from django.views.generic.edit import CreateView

from .models import Event


class CreateEventView(CreateView):
    model = Event
    template_name = 'events/create.html'
    success_url = '/'

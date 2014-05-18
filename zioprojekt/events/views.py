from django.views.generic.edit import CreateView

from .models import Event

from .forms import EventForm


class CreateEventView(CreateView):
    model = Event
    template_name = 'events/create.html'
    form_class = EventForm
    success_url = '/'

    def get_initial(self):
        initial = super(CreateEventView, self).get_initial()

        initial.update({
            'moderator': self.request.user.get_profile().pk,
            'offer': self.kwargs['offer_pk']
        })

        return initial

from django.shortcuts import render

from django.views.generic.base import View
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView

from .models import Event

from .forms import EventForm

from zioprojekt.offers.models import Offer


class JoinEventView(View):
    def get(self, request, *args, **kwargs):
        event = Event.objects.get(id=self.kwargs['event_pk'])

        participants = event.participants.all()

        if not self.request.user.get_profile() in participants:
            event.participants.add(self.request.user.get_profile())

            return render(request, 'events/join_success.html', {})

        else:
            return render(request, 'events/join_failure.html', {})


class ShowEventView(DetailView):
    model = Event
    template_name = 'events/show.html'


class CreateEventView(CreateView):
    model = Event
    template_name = 'events/create.html'
    form_class = EventForm
    success_url = '/'

    def form_valid(self, form):
        offer = Offer.objects.get(id=self.kwargs['offer_pk'])

        object = form.save(commit=False)
        object.moderator = self.request.user.get_profile()
        object.offer = offer
        object.save()

        return super(CreateEventView, self).form_valid(form)

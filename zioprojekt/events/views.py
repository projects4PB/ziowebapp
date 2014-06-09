# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.generic.base import View
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.core.urlresolvers import reverse

from .models import Event, EventJoinOffer

from .forms import EventForm

from zioprojekt.accounts.models import UserProfile

from zioprojekt.offers.models import Offer

from zioprojekt.notes.models import Note


class JoinEventOfferView(View):
    def get(self, request, *args, **kwargs):
        event = Event.objects.get(id=self.kwargs['event_pk'])

        offers = EventJoinOffer.objects.filter(
            event=event, participant=request.user.get_profile(),
            accepted=False)

        if not offers:
            join_offer = EventJoinOffer(
                participant=request.user.get_profile(), event=event)

            join_offer.save()

            return render(request, 'events/join_success.html', {})

        else:
            return render(request, 'events/join_failure.html', {})


class AddParticipantView(View):
    def get(self, request, *args, **kwargs):
        event = Event.objects.get(id=self.kwargs['event_pk'])

        participant = UserProfile.objects.get(id=self.kwargs['profile_pk'])
        event.participants.add(participant)

        offer = EventJoinOffer.objects.get(
            event=event, participant=participant, accepted=False)

        offer.accepted = True
        offer.save()

        messages.add_message(
            request, messages.INFO,
            'Użytkownik został poprawnie dodany do wydarzenia')

        return redirect('/')


class LeaveEventView(View):
    def get(self, request, *args, **kwargs):
        event = Event.objects.get(id=self.kwargs['event_pk'])

        event.participants.remove(request.user.get_profile())

        messages.add_message(
            request, messages.INFO,
            'Zostałeś poprawnie wypisany z wydarzenia')

        return redirect('/')


class ShowEventView(DetailView):
    model = Event
    template_name = 'events/show.html'

    def get_context_data(self, **kwargs):
        context = super(ShowEventView, self) \
            .get_context_data(**kwargs)

        notes = Note.objects.event_notes(
            self.get_object())

        context.update({
            'notes': notes
        })

        return context


class CreateEventView(CreateView):
    model = Event
    template_name = 'events/create.html'
    form_class = EventForm

    def get_success_url(self):
        return reverse('show_event', args=[self.object.pk])

    def form_valid(self, form):
        offer = Offer.objects.get(id=self.kwargs['offer_pk'])

        object = form.save(commit=False)
        object.moderator = self.request.user.get_profile()
        object.offer = offer
        object.save()

        messages.add_message(
            self.request, messages.INFO,
            'Wydarzenie zostało poprawnie utworzone')

        return super(CreateEventView, self).form_valid(form)

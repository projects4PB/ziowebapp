from django.shortcuts import render

from django.views.generic.base import View
from django.views.generic.edit import CreateView

from .models import Offer

from zioprojekt.places.models import TouristObject
from zioprojekt.choices.models import TripTypeChoice


class CreateOfferView(CreateView):
    model = Offer
    template_name = 'offers/create.html'
    success_url = '/'


class SearchOffersView(View):
    """Search for offers"""

    def post(self, request, *args, **kwargs):
        """Returns proper offers"""
        phrase = self.request.POST.get('phrase', '')

        qs = Offer.objects.search(phrase)

        choiced_type = self.kwargs['type_slug']

        categories = TripTypeChoice.objects.get(
            slug__iexact=choiced_type
        ).category.all()

        tourist_objs = TouristObject.objects.filter(
            category__in=categories)

        offers = qs.filter(tourist_object__in=tourist_objs)

        if phrase == '':
            offers = Offer.objects.all()

        return render(request, 'offers/search.html',
                      {'offers': offers})

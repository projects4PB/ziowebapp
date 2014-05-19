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
        tourist_objs = TouristObject.objects.search(phrase)

        choiced_type = self.kwargs['type_slug']

        categories = TripTypeChoice.objects.get(
            slug__iexact=choiced_type
        ).category.all()

        tourist_objs = tourist_objs.filter(
            category__in=categories)

        offers = Offer.objects.filter(
            tourist_object__in=tourist_objs)

        return render(request, 'offers/search.html',
                      {'offers': offers})

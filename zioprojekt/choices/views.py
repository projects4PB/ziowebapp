from django.views.generic.list import ListView

from zioprojekt.offers.models import Offer


class OffersListView(ListView):
    model = Offer
    template_name = 'offers/list.html'

from django.views.generic.edit import CreateView
from django.views.generic.list import ListView

from .models import Offer


class CreateOfferView(CreateView):
    model = Offer
    template_name = 'offers/create.html'
    success_url = '/'


class OffersListView(ListView):
    """Return proper offers list"""
    model = Offer
    template_name = 'offers/list.html'

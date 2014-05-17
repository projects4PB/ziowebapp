from django.views.generic.edit import CreateView

from .models import Offer


class CreateOfferView(CreateView):
    model = Offer
    template_name = 'offers/create.html'
    success_url = '/'

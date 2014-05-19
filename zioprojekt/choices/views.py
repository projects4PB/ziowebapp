from django.views.generic.list import ListView

from zioprojekt.offers.models import Offer

<<<<<<< HEAD
from zioprojekt.choices.models import TripTypeChoice

from zioprojekt.places.models import TouristObject

=======
>>>>>>> 6d213a7f4443ab21f1c06e8a69f9ad28124f3deb

class OffersListView(ListView):
    model = Offer
    template_name = 'offers/list.html'
<<<<<<< HEAD

    def get_queryset(self):
        qs = self.model._default_manager.all()

        choiced_type = self.kwargs['type_slug']

        categories = TripTypeChoice.objects.get(
            slug__iexact=choiced_type
        ).category.all()

        tourist_objs = TouristObject.objects.filter(
            category__in=categories)

        return qs.filter(tourist_object__in=tourist_objs)
=======
>>>>>>> 6d213a7f4443ab21f1c06e8a69f9ad28124f3deb

from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView

from .forms import TouristObjectForm

from .models import TouristObject

from zioprojekt.offers.models import Offer


class CreateTouristObjectView(CreateView):
    model = TouristObject
    form_class = TouristObjectForm
    template_name = 'places/add_object_form.html'
    success_url = '/'

    def form_valid(self, form):
        object = form.save(commit=False)
        object.owner = self.request.user.get_profile()
        object.save()

        return super(CreateTouristObjectView, self) \
            .form_valid(form)


class TouristObjectDetailView(DetailView):
    """Tourist object detail view"""
    model = TouristObject
    template_name = 'places/detail.html'


class TouristObjectAjaxDetailView(TouristObjectDetailView):
    """Tourist object detail view"""
    template_name = 'places/detail_ajax.html'


class PlanRoadView(DetailView):
    model = Offer
    template_name = 'places/road.html'

    def get_context_data(self, **kwargs):
        context = super(PlanRoadView, self) \
            .get_context_data(**kwargs)

        offer = self.get_object()

        context.update({
            'obj_address': offer.tourist_object.address,
            'offer_pk': offer.pk
        })

        return context

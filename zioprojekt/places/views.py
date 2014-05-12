from django.views.generic.edit import CreateView

from .models import TouristObject, RestCentre

from .forms import TouristObjectForm


class CreateTouristObjectView(CreateView):
    model = TouristObject
    form_class = TouristObjectForm
    template_name = 'places/add_object_form.html'


class CreateRestCentreView(CreateTouristObjectView):
    model = RestCentre

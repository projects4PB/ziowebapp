from django.views.generic.edit import CreateView

from .models import TouristObject


class CreateTouristObjectView(CreateView):
    model = TouristObject
    template_name = 'places/add_object_form.html'
    success_url = '/'

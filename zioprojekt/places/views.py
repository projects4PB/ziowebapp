from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView

from .models import TouristObject


class CreateTouristObjectView(CreateView):
    model = TouristObject
    template_name = 'places/add_object_form.html'
    success_url = '/'


class TouristObjectDetailView(DetailView):
    """Tourist object detail view"""
    model = TouristObject
    template_name = 'places/detail.html'


class TouristObjectAjaxDetailView(TouristObjectDetailView):
    """Tourist object detail view"""
    template_name = 'places/detail_ajax.html'

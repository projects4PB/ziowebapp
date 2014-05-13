from django.views.generic.edit import CreateView
from django.views.generic.list import ListView

from .models import TouristObject, RestCentre

from django.shortcuts import render


class CreateTouristObjectView(CreateView):
    model = TouristObject
    template_name = 'places/add_object_form.html'
    success_url = '/'


class CreateRestCentreView(CreateTouristObjectView):
    model = RestCentre


class SearchTouristObjectView(ListView):
    """Search for tourist objects"""
    model = RestCentre
    template_name = 'places/search.html'

    def post(self, request, *args, **kwargs):
        phrase = self.request.POST.get('search_phrase', "x")
        tourist_objs = RestCentre.objects.search(phrase)
        return render(request, 'places/search.html',
                      {'object_list': tourist_objs})

    def get_queryset(self):
        return RestCentre.objects.all()

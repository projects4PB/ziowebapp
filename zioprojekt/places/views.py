from django.views.generic.edit import CreateView
from django.views.generic.base import View

from .models import TouristObject

from django.shortcuts import render


class CreateTouristObjectView(CreateView):
    model = TouristObject
    template_name = 'places/add_object_form.html'
    success_url = '/'


class SearchTouristObjectView(View):
    """Search for tourist objects"""
    model = TouristObject
    template_name = 'places/search.html'

    def post(self, request, *args, **kwargs):
        phrase = self.request.POST.get('phrase', '')
        tourist_objs = TouristObject.objects.search(phrase)
        return render(request, 'places/search.html',
                      {'object_list': tourist_objs})

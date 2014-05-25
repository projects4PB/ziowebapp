import mimetypes

from django.views.generic.base import View
from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView
from django.http import Http404, HttpResponse

from database_storage import DatabaseStorage

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


class StorageImageView(View):
    def get(self, request, *args, **kwargs):
        DBS_OPTIONS = {
            'table': 'places_images',
            'base_url': '/storage_images/',
        }

        filename = self.kwargs['filename']
        storage = DatabaseStorage(DBS_OPTIONS)
        image_file = storage.open(filename, 'rb')
        if not image_file:
            raise Http404
        file_content = image_file.read()
        content_type, content_encoding = mimetypes.guess_type(filename)
        response = HttpResponse(content=file_content, mimetype=content_type)
        response['Content-Disposition'] = 'inline; filename=%s' % filename
        if content_encoding:
            response['Content-Encoding'] = content_encoding
        return response

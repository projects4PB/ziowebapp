import mimetypes

from django.views.generic.base import View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.http import Http404, HttpResponse, HttpResponseRedirect

from database_storage import DatabaseStorage

from .forms import TouristObjectForm, ObjectImagesFormSet

from .models import TouristObject

from zioprojekt.offers.models import Offer


class CreateTouristObjectView(CreateView):
    model = TouristObject
    form_class = TouristObjectForm
    template_name = 'places/add_object_form.html'
    success_url = '/'

    def get(self, request, *args, **kwargs):
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        image_form = ObjectImagesFormSet()

        return self.render_to_response(
            self.get_context_data(
                form=form, image_form=image_form))

    def post(self, request, *args, **kwargs):
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        image_form = ObjectImagesFormSet(
            self.request.POST, self.request.FILES)
        if image_form.is_valid() and form.is_valid():
            return self.form_valid(form, image_form)
        else:
            return self.form_invalid(form, image_form)

    def form_valid(self, form, image_form):
        self.object = form.save(commit=False)
        self.object.owner = self.request.user.get_profile()
        self.object.save()
        image_form.instance = self.object
        image_form.save()

        return HttpResponseRedirect(self.get_success_url())

    def form_invalid(self, form, image_form):
        return self.render_to_response(
            self.get_context_data(
                form=form, image_form=image_form))


class TouristObjectDetailView(DetailView):
    """Tourist object detail view"""
    model = TouristObject
    template_name = 'places/detail.html'


class TouristObjectAjaxDetailView(TouristObjectDetailView):
    """Tourist object detail view"""
    template_name = 'places/detail_ajax.html'


class TouristObjectUpdateView(UpdateView):
    """Tourist object update view"""
    model = TouristObject
    form_class = TouristObjectForm
    template_name = 'places/edit.html'


class TouristObjectDeleteView(DeleteView):
    """Tourist object delete view"""
    model = TouristObject
    template_name = 'places/delete.html'
    success_url = '/'


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

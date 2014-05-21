from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView

from .forms import TouristObjectForm

from .models import TouristObject


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

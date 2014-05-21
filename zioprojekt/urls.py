from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from zioprojekt.home.views import HomeView

from zioprojekt.webservice.views import NotesListWS

from zioprojekt.accounts.views import ProfileView
from zioprojekt.accounts.forms import UserRegistrationForm

from zioprojekt.notes.views import CreateNoteView

from zioprojekt.offers.views import CreateOfferView, \
    SearchOffersView

from zioprojekt.events.views import CreateEventView, ShowEventView, \
    JoinEventView

from zioprojekt.choices.views import OffersListView

from zioprojekt.places.views import CreateTouristObjectView, \
    TouristObjectDetailView, TouristObjectAjaxDetailView

from registration.backends.default.views import RegistrationView

urlpatterns = patterns(
    '',
    url(r'^$', HomeView.as_view()),
    url(r'^notes-ws/', NotesListWS.as_view()),
    url(r'^notes/create', CreateNoteView.as_view()),
    url(r'^offers/list', OffersListView.as_view()),
    url(r'^places/create', CreateTouristObjectView.as_view()),
    url(r'^places/detail/(?P<pk>\d+)/',
        TouristObjectDetailView.as_view(),
        name='tourist_object_detail'),
    url(r'^places/detail-ajax/(?P<pk>\d+)/',
        TouristObjectAjaxDetailView.as_view()),
    url(r'^events/show/(?P<pk>\d+)/', ShowEventView.as_view(),
        name='show_event'),
    url(r'^events/create/(?P<offer_pk>\d+)/', CreateEventView.as_view()),
    url(r'^events/join/(?P<event_pk>\d+)/', JoinEventView.as_view(),
        name='join_event'),
    url(r'^choices/offers-list/(?P<type_slug>[a-zA-Z0-9-_]+)/',
        OffersListView.as_view()),
    url(r'^offers/create', CreateOfferView.as_view()),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^search/(?P<type_slug>[a-zA-Z0-9-_]+)/',
        SearchOffersView.as_view()),
    url(r'^accounts/profile', ProfileView.as_view()),
    url(r'^accounts/register/$', RegistrationView.as_view(
        form_class=UserRegistrationForm),
        name='registration_register'),
    url(r'^accounts/', include('registration.backends.default.urls')),
    url(r'^accounts/', include('django.contrib.auth.urls')),
    url(r'^i18n/', include('django.conf.urls.i18n')),
)

from django.conf.urls.static import static
from django.conf import settings
if settings.DEBUG:
    urlpatterns += static(
        settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

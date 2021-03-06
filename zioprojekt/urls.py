from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from zioprojekt.home.views import HomeView

from zioprojekt.webservice.views import NotesListWS

from zioprojekt.accounts.views import ProfileView, EditProfileView
from zioprojekt.accounts.forms import UserRegistrationForm

from zioprojekt.notes.views import CreateNoteView

from zioprojekt.offers.views import CreateOfferView, \
    SearchOffersView

from zioprojekt.events.views import CreateEventView, ShowEventView, \
    JoinEventOfferView, LeaveEventView, AddParticipantView

from zioprojekt.choices.views import OffersListView

from zioprojekt.places.views import CreateTouristObjectView, \
    TouristObjectDetailView, TouristObjectAjaxDetailView, PlanRoadView, \
    StorageImageView, TouristObjectUpdateView, TouristObjectDeleteView

from djangoratings.views import AddRatingFromModel

from registration.backends.default.views import RegistrationView

urlpatterns = patterns(
    '',
    url(r'^$', HomeView.as_view()),
    url(r'^notes-ws/', NotesListWS.as_view()),
    url(r'^notes/create(?P<event_pk>\d+)/', CreateNoteView.as_view(),
        name='create_note'),
    url(r'^offers/list', OffersListView.as_view()),
    url(r'^places/create', CreateTouristObjectView.as_view()),
    url(r'^places/detail/(?P<pk>\d+)/',
        TouristObjectDetailView.as_view(),
        name='tourist_object_detail'),
    url(r'^places/edit/(?P<pk>\d+)/',
        TouristObjectUpdateView.as_view(),
        name='tourist_object_update'),
    url(r'^places/delete/(?P<pk>\d+)/',
        TouristObjectDeleteView.as_view(),
        name='tourist_object_delete'),
    url(r'^places/detail-ajax/(?P<pk>\d+)/',
        TouristObjectAjaxDetailView.as_view()),
    url(r'^places/road/(?P<pk>\d+)/',
        PlanRoadView.as_view(), name='plan_road'),
    url(r'^places/rate/(?P<object_id>\d+)/(?P<score>\d+)/',
        AddRatingFromModel(), {
            'app_label': 'places',
            'model': 'touristobject',
            'field_name': 'rating',
        }, name='rate_place'),
    url(r'^events/show/(?P<pk>\d+)/', ShowEventView.as_view(),
        name='show_event'),
    url(r'^events/create/(?P<offer_pk>\d+)/',
        CreateEventView.as_view(),
        name='create_event'),
    url(r'^events/join/(?P<event_pk>\d+)/(?P<profile_pk>\d+)/',
        AddParticipantView.as_view(),
        name='join_event'),
    url(r'^events/offer/(?P<event_pk>\d+)/', JoinEventOfferView.as_view(),
        name='join_event_offer'),
    url(r'^events/leave/(?P<event_pk>\d+)/', LeaveEventView.as_view(),
        name='leave_event'),
    url(r'^choices/offers-list/(?P<type_slug>[a-zA-Z0-9-_]+)/',
        OffersListView.as_view()),
    url(r'^offers/create', CreateOfferView.as_view()),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^search/(?P<type_slug>[a-zA-Z0-9-_]+)/',
        SearchOffersView.as_view()),
    url(r'^accounts/profile/edit/(?P<pk>\d+)/', EditProfileView.as_view(),
        name='edit_profile'),
    url(r'^accounts/profile', ProfileView.as_view(), name='profile_detail'),
    url(r'^accounts/register/$', RegistrationView.as_view(
        form_class=UserRegistrationForm),
        name='registration_register'),
    url(r'^comments/', include('django.contrib.comments.urls')),
    url(r'^accounts/', include('registration.backends.default.urls')),
    url(r'^accounts/', include('django.contrib.auth.urls')),
    url(r'^storage_images/(?P<filename>[a-zA-Z0-9-._/]+)',
        StorageImageView.as_view()),
    url(r'^i18n/', include('django.conf.urls.i18n')),
)

from django.conf.urls.static import static
from django.conf import settings
if settings.DEBUG:
    urlpatterns += static(
        settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

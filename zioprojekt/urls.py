from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from zioprojekt.home.views import HomeView

from zioprojekt.webservice.views import NotesListWS

from zioprojekt.accounts.views import ProfileView

from zioprojekt.notes.views import CreateNoteView

from zioprojekt.offers.views import CreateOfferView

from zioprojekt.events.views import CreateEventView

from zioprojekt.places.views import CreateRestCentreView, \
    SearchTouristObjectView

urlpatterns = patterns(
    '',
    url(r'^$', HomeView.as_view()),
    url(r'^notes-ws/', NotesListWS.as_view()),
    url(r'^notes/create', CreateNoteView.as_view()),
    url(r'^places/create', CreateRestCentreView.as_view()),
    url(r'^events/create', CreateEventView.as_view()),
    url(r'^offers/create', CreateOfferView.as_view()),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^search/', SearchTouristObjectView.as_view()),
    url(r'^accounts/profile', ProfileView.as_view()),
    url(r'^accounts/', include('registration.backends.default.urls')),
    url(r'^accounts/', include('django.contrib.auth.urls')),
    url(r'^i18n/', include('django.conf.urls.i18n')),
)

from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from home.views import HomeView

from webservice.views import NotesListWS

from accounts.views import ProfileView

from places.views import CreateRestCentreView

urlpatterns = patterns(
    '',
    url(r'^$', HomeView.as_view()),
    url(r'^notes/', NotesListWS.as_view()),
    url(r'^places/create', CreateRestCentreView.as_view()),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/profile', ProfileView.as_view()),
    url(r'^accounts/', include('registration.backends.default.urls')),
)

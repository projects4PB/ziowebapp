from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from webservice.views import NotesListWS
from home.views import HomeView

urlpatterns = patterns(
    '',
    url(r'^home/', HomeView.as_view()),
    url(r'^notes/', NotesListWS.as_view()),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('registration.backends.default.urls')),
)

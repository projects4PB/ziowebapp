from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from webservice.views import NotesListWS

urlpatterns = patterns(
    '',
    url(r'^notes/', NotesListWS.as_view()),
    url(r'^admin/', include(admin.site.urls)),
)

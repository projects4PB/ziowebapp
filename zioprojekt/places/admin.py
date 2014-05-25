from django.contrib import admin

from .models import Facilities, TouristObject, TouristObjectsCity, \
    TouristObjectImage

admin.site.register(TouristObject)
admin.site.register(TouristObjectsCity)
admin.site.register(TouristObjectImage)
admin.site.register(Facilities)

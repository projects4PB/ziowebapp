from django.contrib import admin

from .models import Facilities, TouristObject, TouristObjectsCity

admin.site.register(TouristObject)
admin.site.register(TouristObjectsCity)
admin.site.register(Facilities)

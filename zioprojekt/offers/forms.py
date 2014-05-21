# -*- coding: utf-8 -*-
from django import forms

from .models import Offer

from zioprojekt.places.models import TouristObject


class OfferForm(forms.ModelForm):
    """Setting tourist object facilities field"""
    def __init__(self, *args, **kwargs):
        profile = kwargs.pop('profile', None)
        super(OfferForm, self).__init__(*args, **kwargs)
        self.fields['tourist_object'].queryset = \
            TouristObject.objects.user_objs(profile)

    class Meta:
        model = Offer

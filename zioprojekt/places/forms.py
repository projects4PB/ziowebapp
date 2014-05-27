from django import forms
from django.forms.models import inlineformset_factory

from .models import Facilities, TouristObject, TouristObjectImage


class TouristObjectForm(forms.ModelForm):
    """Setting tourist object facilities field"""
    facilities = forms.ModelMultipleChoiceField(
        queryset=Facilities.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False, label=u'Udogodnienia')

    class Meta:
        model = TouristObject
        exclude = ('owner',)

ObjectImagesFormSet = inlineformset_factory(
    TouristObject, TouristObjectImage,
    form=TouristObjectForm, extra=5)

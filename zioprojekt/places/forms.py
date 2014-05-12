from django import forms

from .models import Facilities, TouristObject


class TouristObjectForm(forms.ModelForm):
    """Setting tourist object facilities field"""
    facilities = forms.ModelMultipleChoiceField(
        queryset=Facilities.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False, label=u'Udogodnienia')

    class Meta:
        model = TouristObject

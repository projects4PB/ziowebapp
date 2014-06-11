# -*- coding: utf-8 -*-
from registration.forms import RegistrationForm
from django import forms

from .models import UserProfile


class UserRegistrationForm(RegistrationForm):
    YES_OR_NO = (
        (True, 'Tak'),
        (False, 'Nie')
    )
    address = forms.CharField(label=u'Adres')
    is_owner = forms.BooleanField(widget=forms.RadioSelect(
        choices=YES_OR_NO), required=False,
        label=u'Czy jesteś właścicielem?:')


class UserProfileForm(forms.ModelForm):
    YES_OR_NO = (
        (True, 'Tak'),
        (False, 'Nie')
    )
    address = forms.CharField(label=u'Adres')
    is_owner = forms.BooleanField(widget=forms.RadioSelect(
        choices=YES_OR_NO), required=False,
        label=u'Czy jesteś właścicielem?:')

    class Meta:
        model = UserProfile
        exclude = ('user',)

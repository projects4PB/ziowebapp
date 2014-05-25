# -*- coding: utf-8 -*-
from registration.forms import RegistrationForm
from django import forms


class UserRegistrationForm(RegistrationForm):
    YES_OR_NO = (
        (True, 'Tak'),
        (False, 'Nie')
    )
    address = forms.CharField()
    is_owner = forms.BooleanField(widget=forms.RadioSelect(
        choices=YES_OR_NO), required=False,
        label=u'Czy jesteś właścicielem?:')

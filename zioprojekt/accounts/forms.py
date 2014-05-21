# -*- coding: utf-8 -*-
from registration.forms import RegistrationForm
from django import forms


class UserRegistrationForm(RegistrationForm):
    address = forms.CharField()
    is_owner = forms.BooleanField(
        label="Czy jesteś właścicielem obiektu?:")

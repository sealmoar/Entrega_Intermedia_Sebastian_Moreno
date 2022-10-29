from socket import fromshare
from django import forms
from django.forms import CharField, IntegerField, TextInput

class LocationForm(forms.Form):
    name = forms.CharField(
        label = "Nombre sucursal",
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "location-name",
                "placeholder": "Nombre de la sucursal",
                "required": "True",
            }
        ),
    )
    adress = forms.CharField(
        label = "dirección sucursal",
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "location-adress",
                "placeholder": "Dirección de la sucursal",
                "required": "True",
            }
        ),
    )
    n_hood = forms.CharField(
        label = "Barrio",
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "location-neighborhood",
                "placeholder": "Barrio de la sucursal",
                "required": "True",
            }
        ),
    )
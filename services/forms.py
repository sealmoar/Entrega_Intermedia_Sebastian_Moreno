from socket import fromshare
from django import forms
from django.forms import CharField, IntegerField, TextInput

class ServiceForm(forms.Form):
    name = forms.CharField(
        label = "Nombre servicio",
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "service-name",
                "placeholder": "Nombre del servicio",
                "required": "True",
            }
        ),
    )
    price = forms.IntegerField(
        label = "Precio",
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "service-price",
                "placeholder": "Valor del servicio",
                "required": "True",
            }
        ),
    )
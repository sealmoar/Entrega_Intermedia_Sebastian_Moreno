from socket import fromshare
from django import forms
from django.forms import CharField, IntegerField, TextInput

class OwnerForm(forms.Form):
    name = forms.CharField(
        label = "Nombre de Dueño",
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "owner-name",
                "placeholder": "Nombre de la mascota",
                "required": "True",
            }
        ),
    )
    adress = forms.CharField(
        label = "dirección Dueño",
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "owner-type",
                "placeholder": "Dirección del dueño",
                "required": "True",
            }
        ),
    )
    phone = forms.IntegerField(
        label = "celular dueño",
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "owner-adress",
                "placeholder": "Dirección del dueño",
                "required": "True",
            }
        ),
    )
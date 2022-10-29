from socket import fromshare
from django import forms
from django.forms import CharField, IntegerField, TextInput

class PetForm(forms.Form):
    name = forms.CharField(
        label = "Nombre de Mascota",
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "pet-name",
                "placeholder": "Nombre de la mascota",
                "required": "True",
            }
        ),
    )
    animal = forms.CharField(
        label = "tipo de Mascota",
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "pet-type",
                "placeholder": "Tipo de Mascota",
                "required": "True",
            }
        ),
    )
    breed = forms.CharField(
        label = "Raza de la Mascota",
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "pet-breed",
                "placeholder": "Raza de la mascota",
                "required": "True",
            }
        ),
    )
    age = forms.IntegerField(
        label = "Edad de Mascota",
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "pet-age",
                "placeholder": "Edad de la mascota",
                "required": "True",
            }
        ),
    )
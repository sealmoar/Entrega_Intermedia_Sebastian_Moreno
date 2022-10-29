from datetime import datetime
from django.contrib import messages
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

from pets.forms import PetForm
from pets.models import Pet


def get_pets(request):
    pets = Pet.objects.all()
    paginator = Paginator(pets, 3)
    page_number = request.GET.get("page")
    return paginator.get_page(page_number)


def create_pets(request):
    if request.method == "POST":
        pet_form = PetForm(request.POST)
        if pet_form.is_valid():
            data = pet_form.cleaned_data
            actual_objects = Pet.objects.filter(
                name=data["name"], animal=data["animal"]
            ).count()
            if actual_objects:
                messages.error(
                    request,
                    f"La mascota {data['name']} - {data['animal']} ya está creado",
                )
            else:
                pet = Pet(name=data["name"], animal=data["animal"],age=data["age"], breed=data["breed"])
                pet.save()
                messages.success(
                    request,
                    f"MAscota {data['name']} - {data['animal']} creado exitosamente!",
                )

            return render(
                request=request,
                context={"pets": Pet.objects.all()},
                template_name="pets/pet_list.html",
            )

    pet_form = PetForm(request.POST)
    context_dict = {"form": pet_form}
    return render(
        request=request, context=context_dict, template_name="pets/pet_form.html"
    )


def pets(request):
    return render(
        request=request,
        context={"pets": get_pets(request)},
        template_name="pets/pet_list.html",
    )


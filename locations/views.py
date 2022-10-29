from datetime import datetime
from django.contrib import messages
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

from locations.forms import LocationForm
from locations.models import Location


def get_locations(request):
    locations = Location.objects.all()
    paginator = Paginator(locations, 3)
    page_number = request.GET.get("page")
    return paginator.get_page(page_number)


def create_locations(request):
    if request.method == "POST":
        location_form = LocationForm(request.POST)
        if location_form.is_valid():
            data = location_form.cleaned_data
            actual_objects = Location.objects.filter(
                name=data["name"], adress=data["adress"]
            ).count()
            if actual_objects:
                messages.error(
                    request,
                    f"La mascota {data['name']} - {data['adress']} ya está creado",
                )
            else:
                location = Location(name=data["name"], adress=data["adress"],n_hood=data["n_hood"])
                location.save()
                messages.success(
                    request,
                    f"MAscota {data['name']} - {data['adress']} creado exitosamente!",
                )

            return render(
                request=request,
                context={"locations": Location.objects.all()},
                template_name="locations/location_list.html",
            )

    location_form = LocationForm(request.POST)
    context_dict = {"form": location_form}
    return render(
        request=request, context=context_dict, template_name="locations/location_form.html"
    )


def locations(request):
    return render(
        request=request,
        context={"locations": get_locations(request)},
        template_name="locations/location_list.html",
    )


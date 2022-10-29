from datetime import datetime
from django.contrib import messages
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

from services.forms import ServiceForm
from services.models import Service


def get_services(request):
    services = Service.objects.all()
    paginator = Paginator(services, 3)
    page_number = request.GET.get("page")
    return paginator.get_page(page_number)


def create_services(request):
    if request.method == "POST":
        service_form = ServiceForm(request.POST)
        if service_form.is_valid():
            data = service_form.cleaned_data
            actual_objects = Service.objects.filter(
                name=data["name"], price=data["price"]
            ).count()
            if actual_objects:
                messages.error(
                    request,
                    f"El servicio {data['name']} - {data['price']} ya está creado",
                )
            else:
                service = Service(name=data["name"], price=data["price"])
                service.save()
                messages.success(
                    request,
                    f"Servicio {data['name']} - {data['price']} creado exitosamente!",
                )

            return render(
                request=request,
                context={"services": Service.objects.all()},
                template_name="services/service_list.html",
            )

    service_form = ServiceForm(request.POST)
    context_dict = {"form": service_form}
    return render(
        request=request, context=context_dict, template_name="services/service_form.html"
    )


def services(request):
    return render(
        request=request,
        context={"services": get_services(request)},
        template_name="services/service_list.html",
    )


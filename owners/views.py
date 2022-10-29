from datetime import datetime
from django.contrib import messages
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

from owners.forms import OwnerForm
from owners.models import Owner


def get_owners(request):
    owners = Owner.objects.all()
    paginator = Paginator(owners, 3)
    page_number = request.GET.get("page")
    return paginator.get_page(page_number)


def create_owners(request):
    if request.method == "POST":
        owner_form = OwnerForm(request.POST)
        if owner_form.is_valid():
            data = owner_form.cleaned_data
            actual_objects = Owner.objects.filter(
                name=data["name"], phone=data["phone"]
            ).count()
            if actual_objects:
                messages.error(
                    request,
                    f"La mascota {data['name']} - {data['phone']} ya está creado",
                )
            else:
                owner = Owner(name=data["name"], phone=data["phone"],adress=data["adress"])
                owner.save()
                messages.success(
                    request,
                    f"MAscota {data['name']} - {data['phone']} creado exitosamente!",
                )

            return render(
                request=request,
                context={"owners": Owner.objects.all()},
                template_name="owners/owner_list.html",
            )

    owner_form = OwnerForm(request.POST)
    context_dict = {"form": owner_form}
    return render(
        request=request, context=context_dict, template_name="owners/owner_form.html"
    )


def owners(request):
    return render(
        request=request,
        context={"owners": get_owners(request)},
        template_name="owners/owner_list.html",
    )


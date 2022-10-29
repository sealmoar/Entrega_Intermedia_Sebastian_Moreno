from django.shortcuts import render
from django.db.models import Q

from pets.models import Pet

def index (request):
    return render(
        request=request,
        context={},
        template_name="home/index.html",
    )

def search(request):
    search_param = request.GET["search_param"]
    print("search: ", search_param)
    context_dict = dict()
    if search_param:
        query = Q(name__contains=search_param)
        query.add (Q(breed__contains=search_param), Q.OR)
        query.add (Q(age__contains=search_param), Q.OR)
        query.add (Q(animal__contains=search_param), Q.OR)
        pets = Pet.objects.filter(query)
        context_dict.update(
            {
                "pets": pets,
                "search_param": search_param,
            }
        )
    return render(
        request=request,
        context=context_dict,
        template_name="home/index.html",
    )
# Create your views here.

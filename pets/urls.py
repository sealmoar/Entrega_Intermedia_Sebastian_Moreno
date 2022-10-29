from django.urls import path

from pets import views

app_name = "pets"
urlpatterns = [
    path("pets", view=views.pets, name="pet-list"),
    path("pet/add", view=views.create_pets, name="pet-add"),
]
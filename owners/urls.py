from django.urls import path

from owners import views

app_name = "owners"
urlpatterns = [
    path("owners", view=views.owners, name="owner-list"),
    path("owner/add", view=views.create_owners, name="owner-add"),
]
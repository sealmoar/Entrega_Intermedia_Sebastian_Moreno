from django.urls import path

from services import views

app_name = "services"
urlpatterns = [
    path("services", view=views.services, name="service-list"),
    path("services/add", view=views.create_services, name="service-add"),
]
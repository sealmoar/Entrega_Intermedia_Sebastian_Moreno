from django.urls import path

from locations import views

app_name = "locations"
urlpatterns = [
    path("locations", view=views.locations, name="location-list"),
    path("location/add", view=views.create_locations, name="location-add"),
]
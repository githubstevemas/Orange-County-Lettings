from django.urls import path

from . import views

app_name = "lettings"

urlpatterns = [
    # Route for displaying the list of all lettings
    path("", views.index, name="lettings_index"),
    # Route for displaying a specific letting with its ID
    path("<int:letting_id>/", views.letting, name="letting"),
]

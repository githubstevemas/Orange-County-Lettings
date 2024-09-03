from django.urls import path

from . import views

app_name = "profiles"

urlpatterns = [
    # Route for displaying the list of all profiles
    path("", views.index, name="profiles_index"),
    # Route for displaying a specific letting with its username
    path("<str:username>/", views.profile, name="profile"),
]

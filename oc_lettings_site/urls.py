from django.contrib import admin
from django.urls import path, include

from oc_lettings_site import views

# Custom handler for 404 errors (Page Not Found)
handler404 = 'oc_lettings_site.views.custom_404'

# Custom handler for 500 errors (Server Error)
handler500 = 'oc_lettings_site.views.custom_500'

urlpatterns = [
    # Route for the home page of the site
    path('', views.index, name='index'),
    # Includes the URLs for the 'lettings' application
    path('lettings/', include('lettings.urls')),
    # Includes the URLs for the 'profiles' application
    path('profiles/', include('profiles.urls')),
    # Route for the Django admin interface
    path('admin/', admin.site.urls),
    # Route for sentry test
    path('sentry-debug/', views.trigger_error),
]

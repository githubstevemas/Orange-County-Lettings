import sentry_sdk
from django.shortcuts import render


def index(request):
    # Render the home page using the 'index.html' template
    return render(request, 'index.html')


def custom_404(request, exception):
    """
    Capture a "Page not found" message using Sentry and render the custom 404
    error page using the '404.html' template
    """

    return render(request, '404.html', status=404)


def custom_500(request):
    """
    Capture exception when a 500 server error occurs and render the custom 500
    error page using the '500.html' template
    """

    sentry_sdk.capture_exception()
    return render(request, '500.html', status=500)

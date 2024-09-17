import sentry_sdk
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    # Render the home page using the 'index.html' template
    return render(request, 'index.html')


def custom_404(request, exception):
    """
    Capture a "Page not found" message using Sentry and render the custom 404
    error page using the '404.html' template

    Args:
        request (HttpRequest): The request object.
        exception (Exception): The exception that caused the 404 error.

    Returns:
        HttpResponse: An HTTP response object rendering the '404.html' template
        with a 404 status code.
    """

    return render(request, '404.html', status=404)


def custom_500(request):
    """
    Capture exception when a 500 server error occurs and render the custom 500
    error page using the '500.html' template

    Args:
        request (HttpRequest): The request object.

    Returns:
        HttpResponse: An HTTP response object rendering the '500.html' template
        with a 500 status code.
    """

    sentry_sdk.capture_exception()
    return render(request, '500.html', status=500)


def trigger_error(request):
    """
    Sentry test with zero division

    Returns:
        An beautifull error!
    """
    error = 1 / 0
    return HttpResponse("Error.")

import sentry_sdk
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def custom_404(request, exception):
    sentry_sdk.capture_message("Page not found")
    return render(request, '404.html', status=404)


def custom_500(request):
    sentry_sdk.capture_exception()
    return render(request, '500.html', status=500)

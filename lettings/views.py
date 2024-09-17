from django.shortcuts import render, get_object_or_404

from .models import Letting


def index(request):
    """
    Get all the lettings from db and render context dictionary
    to the 'lettings/index.html' template

    Args:
        request (HttpRequest): The request object.

    Returns:
        HttpResponse: An HTTP response object rendering the
        'lettings/index.html' template with a context containing the list
        of all lettings.
    """

    lettings_list = Letting.objects.all()
    context = {'lettings_list': lettings_list}
    return render(request, 'lettings/index.html', context)


def letting(request, letting_id):
    """
    Get specific letting with its ID or return a 404 error if not found
    and render context dictionary to the 'lettings/letting.html' template

    Args:
        request (HttpRequest): The request object.
        letting_id (int): The ID of the letting to retrieve.

    Returns:
        HttpResponse: An HTTP response object rendering the
        'lettings/letting.html' template with a context containing the
        letting's title and address. If the letting is not found,
        it raises a 404 error and returns a 404 response.
    """

    letting = get_object_or_404(Letting, id=letting_id)
    context = {
        'title': letting.title,
        'address': letting.address,
    }

    return render(request, 'lettings/letting.html', context)

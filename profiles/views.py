from django.shortcuts import render, get_object_or_404

from .models import Profile


def index(request):
    """
    Get all the profiles from db and render context dictionary
    to the 'profiles/index.html' template

    Args:
        request (HttpRequest): The request object.

    Returns:
        HttpResponse: An HTTP response object rendering the 'profiles/index.html' template
        with a context containing the list of all profiles.
    """

    profiles_list = Profile.objects.all()
    context = {'profiles_list': profiles_list}
    return render(request, 'profiles/index.html', context)


def profile(request, username):
    """
    Get specific profile with its username or return a 404 error if not found
    and render context dictionary to the 'profiles/profile.html' template

    Args:
        request (HttpRequest): The request object.
        username (str): The username of the profile to retrieve.

    Returns:
        HttpResponse: An HTTP response object rendering the 'profiles/profile.html' template
        with a context containing the profile data. If the profile is not found,
        it raises a 404 error and returns a 404 response.
    """

    profile = get_object_or_404(Profile, user__username=username)
    context = {'profile': profile}
    return render(request, 'profiles/profile.html', context)

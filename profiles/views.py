from django.shortcuts import render, get_object_or_404

from .models import Profile


def index(request):
    """
    Get all the profiles from db and render context dictionary
    to the 'profiles/index.html' template
    """

    profiles_list = Profile.objects.all()
    context = {'profiles_list': profiles_list}
    return render(request, 'profiles/index.html', context)


def profile(request, username):
    """
    Get specific profile with its username or return a 404 error if not found
    and render context dictionary to the 'profiles/profile.html' template
    """

    profile = get_object_or_404(Profile, user__username=username)
    context = {'profile': profile}
    return render(request, 'profiles/profile.html', context)

from django.shortcuts import render
from bug.settings import BO


def bug_profile(request):
    if BO.first_time:
        BO.first_time = False
        return render(request, "bug_profile.html", {'first_time': True})
    return render(request, "bug_profile.html", {'first_time': False})

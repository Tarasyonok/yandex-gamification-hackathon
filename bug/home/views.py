from django.shortcuts import render

from bug.settings import BO


def home(request):
    return render(request, "index.html")


def profile(request):
    return render(request, "profile.html", {'first_time': BO.first_time})


from django.shortcuts import render
from .models import Avatar


# Create your views here.
def home_view(request):
    return render(request, "home.html")


def avatar_view(request):
    avatar = Avatar.objects.all
    return render(request, "Avatars.html", {"avatar": avatar})

from django.shortcuts import render
from .models import Avatar, Bloodline
from users.models import Player


# Create your views here.
def num_of_tables_in_model(model):
    all_model = model.objects.count
    return all_model


def home_view(request):
    return render(request, "home.html",
                  {"avatar_num": num_of_tables_in_model(Avatar), "player_num": num_of_tables_in_model(Player)})


def avatar_view(request):
    avatar = Avatar.objects.all
    return render(request, "Avatars.html", {"avatar": avatar})


def bloodline_view(request):
    bloodline = Bloodline.objects.all
    return render(request, "Bloodlines.html", {"bloodline": bloodline})

from django.shortcuts import render
from .models import Avatar


# Create your views here.
def home_view(request):
    avatar = Avatar.objects.filter(name__contains="")
    dis_avatar = avatar.order_by("bio")[2]
    avatar2 = Avatar.objects.filter(name__contains="h")
    dis_avatar2 = avatar2.order_by("bio")[1]
    avatar3 = Avatar.objects.filter(name__contains="sh")
    dis_avatar3 = avatar3.order_by("bio")[0]

    return render(request, "home.html", {"dis_ava": dis_avatar, "dis_ava2":dis_avatar2, "dis_ava3":dis_avatar3})


def avatar_view(request):
    avatar = Avatar.objects.all
    return render(request, "Avatars.html", {"avatar": avatar})

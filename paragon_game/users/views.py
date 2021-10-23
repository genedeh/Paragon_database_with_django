from django.shortcuts import render, redirect
from django.template.defaultfilters import slugify

from .forms import PlayerSigninForm, PlayerLoginForm
from .models import Player, Group
from django.views.generic import DetailView


# Create your views here.
def public_player_view(request):
    model = Player.objects.all().order_by('username')
    return render(request, 'players.html', {'model': model})


def public_group_view(request):
    model = Group.objects.all().order_by('name')
    return render(request, 'groups.html', {'model': model})


def group_View(request):
    pass


def sign_in_view(request):
    if request.method == "POST":
        form = PlayerSigninForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.slug = slugify(post.username)
            post.just_joined = True
            post.save()
            return redirect(post.get_absolute_url())
    else:
        form = PlayerSigninForm
    return render(request, "Sign up.html", {'form': form})


def login_view(request, error=""):
    if request.method == 'POST':
        form = PlayerLoginForm(request.POST)
        username = request.POST['username']
        password = request.POST['password']

        if Player.objects.filter(username=username):
            if Player.objects.filter(password=password):
                play = Player.objects.filter(password=password)
                play_list = list(play)
                for p in play_list:
                    join_url = p.get_absolute_url()
                    p.just_joined = False
                    p.save()
                return redirect(join_url)
            else:
                error = "  Username or Password is  not correct please check you Username and Password."
        else:
            error = "  Username or Password is  not correct please check you Username and Password."
    else:
        form = PlayerLoginForm
    return render(request, "login.html", {'form': form, 'error': error})


class PlayerView(DetailView):
    model = Player
    template_name = 'user.html'

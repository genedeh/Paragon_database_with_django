from django.shortcuts import render, redirect
from django.template.defaultfilters import slugify

from .forms import PlayerSigninForm, PlayerLoginForm
from .models import Player
from django.views.generic import DetailView


# Create your views here.
def sign_in_view(request):
    if request.method == "POST":
        form = PlayerSigninForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.slug = slugify(post.username)
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
        if Player.objects.filter(username=username) and Player.objects.filter(password=password):
            # p = Player(username=username, password=password)
            print('--------------------------------------')
            play = Player.objects.filter(username=username)
            play_list = list(play)
            for p in play_list:
                join_url = p.get_absolute_url()
            print('--------------------------------------')
            return redirect(join_url)
        else:
            error = "username or password is  not correct please check you username and password"
    else:
        form = PlayerLoginForm
    return render(request, "login.html", {'form': form, 'error': error})


class PlayerView(DetailView):
    model = Player
    template_name = r'C:\Users\KidChaos\PycharmProjects\Paragon_with_django\paragon_game\templates\user.html'

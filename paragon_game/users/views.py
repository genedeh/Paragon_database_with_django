from django.shortcuts import render, redirect
from django.template.defaultfilters import slugify

from .forms import PlayerSigninForm
from .models import Player
from django.urls import reverse
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


class PlayerView(DetailView):
    model = Player
    template_name = r'C:\Users\KidChaos\PycharmProjects\Paragon_with_django\paragon_game\templates\user.html'

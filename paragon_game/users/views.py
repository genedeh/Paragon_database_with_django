from django.shortcuts import render, redirect
from .forms import PlayerSigninForm
from .models import Player
from django.views.generic import DetailView


# Create your views here.
def sign_in_view(request):
    if request.method == "POST":
        form = PlayerSigninForm(request.POST)
        if form.is_valid():
            # print(form.cleaned_data['location'])
            form.save()
            return redirect("game:home")
    else:
        form = PlayerSigninForm
    return render(request, "Sign up.html", {'form': form})


class UserView(DetailView):
    model = Player
    template_name = r'C:\Users\KidChaos\PycharmProjects\Paragon_with_django\paragon_game\templates\user.html'

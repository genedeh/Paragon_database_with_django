from django.urls import path
from .views import home_view, avatar_view

app_name = "game"

urlpatterns = [
    path('', home_view, name='home'),
    path('avatars', avatar_view, name='avatars')
]

from django.urls import path
from .views import sign_in_view, PlayerView, login_view

app_name = "users"

urlpatterns = [
    path('signin', sign_in_view, name='Signin'),
    path('login', login_view, name='login'),
    path('<slug:slug>/', PlayerView.as_view(), name='player')
]

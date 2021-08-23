from django.urls import path
from .views import sign_in_view, PlayerView

app_name = "users"

urlpatterns = [
    path('signin', sign_in_view, name='Signin'),
    path('<slug:slug>/', PlayerView.as_view(), name='player')
]

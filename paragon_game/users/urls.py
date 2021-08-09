from django.urls import path
from .views import sign_in_view, UserView

app_name = "users"

urlpatterns = [
    path('signin', sign_in_view, name='Signin'),
    path('Player/<pk>/', UserView.as_view(), name='player')
]

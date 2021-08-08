from django.urls import path
from .views import sign_in_view

app_name = "users"

urlpatterns = [
    path('signin', sign_in_view, name='Signin'),
]

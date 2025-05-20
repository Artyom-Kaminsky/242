from django.urls import path

from clients.views import (
    RegistrationView, 
    LoginView,
    LogoutView,
    ActivationView
)


urlpatterns = [
    path(route="reg/", view=RegistrationView.as_view(), name="reg"),
    path(route="login/", view=LoginView.as_view(), name="login"),
    path(route="logout/", view=LogoutView.as_view(), name="logout"),
    path(
        route="activation/<str:username>/<str:code>", 
        view=ActivationView.as_view(), name="activate"
    ),
]

from django.urls import path
from core.views import SignUpView, LoginView, ProfileView


urlpatterns = [
    path("signup", SignUpView.as_view()),
    path("login", LoginView.as_view()),
    path("profile", ProfileView.as_view()),
]

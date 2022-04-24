from django.urls import path
from .views import LoginView, RegisterView


urlpatterns = [

    path('registration',RegisterView.as_view()),
    path('login',LoginView.as_view())
]
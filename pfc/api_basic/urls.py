from django.urls import path
from .views import appointment_list
urlpatterns = [
    path("",appointment_list)
]

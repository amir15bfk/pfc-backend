from django.urls import path
from .views import AppointemtAPIView, appointment_list,appointment_detail
urlpatterns = [
    # path("appointment",appointment_list),
    path("appointment",AppointemtAPIView.as_view()),
    path("detail/<int:pk>",appointment_detail)
]

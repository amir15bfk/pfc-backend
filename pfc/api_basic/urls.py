from django.urls import path
from .views import AppointemtAPIView, AppointmentDetail,AppointemtAPIViewWithYear,AppointemtAPIViewWithMonth,AppointemtAPIViewWithDay#, GenericAPIView, appointment_list,appointment_detail
urlpatterns = [
    # path("appointments",appointment_list),
    path("appointment",AppointemtAPIView.as_view()),
    # path("detail/<int:pk>",appointment_detail),
    path("detail/<int:pk>",AppointmentDetail.as_view()),
    # path("generics/appointment",GenericAPIView.as_view()),
    path("appointment/<int:year>",AppointemtAPIViewWithYear.as_view()),
    path("appointment/<int:year>/<int:month>",AppointemtAPIViewWithMonth.as_view()),
    path("appointment/<int:year>/<int:month>/<int:day>",AppointemtAPIViewWithDay.as_view()),

]

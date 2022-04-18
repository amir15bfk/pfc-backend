import imp
from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from rest_framework.parsers import JSONParser
from .models import Appointment
from .serializers import AppointmentSerializer
# Create your views here.


def appointment_list(request):
    if request.method == 'GET':
        appointment = Appointment.objects.all()
        serializer = AppointmentSerializer(appointment,many=True)
        return JsonResponse(serializer.data,safe=False)
    
    elif request.method == 'POST':
        data  = JSONParser().parse(request)
        serializer = AppointmentSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data,status=201)
        return JsonResponse(serializer.errors,status= 400)
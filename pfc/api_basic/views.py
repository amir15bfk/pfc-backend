import imp
from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from rest_framework.parsers import JSONParser
from .models import Appointment
from .serializers import AppointmentSerializer
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
# Create your views here.


class AppointemtAPIView(APIView):
    def get(self,request):
        appointment = Appointment.objects.filter(owner=request.user)
        serializer = AppointmentSerializer(appointment,many=True)
        return Response(serializer.data)

    def post(self,request):
        serializer = AppointmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status= status.HTTP_400_BAD_REQUEST) 

@api_view(['GET','POST'])
def appointment_list(request):
    if request.method == 'GET':
        appointment = Appointment.objects.filter(owner=request.user)
        serializer = AppointmentSerializer(appointment,many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = AppointmentSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status= status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
def appointment_detail(request,pk):
    try:
        appointment = Appointment.objects.get(pk=pk)
    except Appointment.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)
    
    if request.method =='GET':
        serializer= AppointmentSerializer(appointment)
        return Response(serializer.data)
    elif request.method =='PUT':
        serializer = AppointmentSerializer(appointment,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status= status.HTTP_400_BAD_REQUEST)
    elif request.method =='DELETE':
        appointment.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)
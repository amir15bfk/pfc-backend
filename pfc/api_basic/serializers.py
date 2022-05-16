from dataclasses import fields
from pyexpat import model
from rest_framework import serializers
from .models import Appointment

class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = ["title","id","description","date","start_time","end_time","is_completed","importance"]
    # title = serializers.CharField(max_length=50)
    # description = serializers.CharField(max_length=200)
    # date = serializers.DateTimeField()
    # importance = serializers.IntegerField(default=1)

    # def create(self ,validated_data):
    #     return Appointment.objects.create(validated_data)
    # def update(self,instance,validated_data):
    #     instance.title = validated_data.get("title",instance.title)
    #     instance.description = validated_data.get("description",instance.description)
    #     instance.date = validated_data.get("date",instance.date)
    #     instance.importance = validated_data.get("importance",instance.importance)
    #     instance.save()
    #     return instance
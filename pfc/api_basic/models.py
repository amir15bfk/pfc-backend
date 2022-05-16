from django.db import models
from django.conf import settings

# Create your models here.
class Appointment(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    date = models.DateField()
    start_time = models.TimeField() 
    end_time = models.TimeField() 
    is_completed = models.BooleanField(default=False)
    importance = models.IntegerField(default=1)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title

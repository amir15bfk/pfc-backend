from django.contrib.auth.models import Group
from django.contrib import admin


admin.site.unregister(Group)
admin.site.site_header = "Appointment App Admin"
admin.site.site_title = "Appointment App Admin Portal"
admin.site.index_title = "Welcome to our PFC admin pann"
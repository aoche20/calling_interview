from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Interview, Room

admin.site.register(Interview)
admin.site.register(Room)

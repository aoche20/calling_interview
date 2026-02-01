from django.urls import path
from .views import room_view

urlpatterns = [
    path('room/<str:room_name>/', room_view, name='room'),
]

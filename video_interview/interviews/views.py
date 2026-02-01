from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def room_view(request, room_name):
    return render(request, 'interviews/room.html', {
        'room_name': room_name
    })
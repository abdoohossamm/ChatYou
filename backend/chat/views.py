from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Room
def index(request):
    rooms = Room.objects.all()
    ctx = {'rooms': rooms}
    return render(request, 'chat/index.html', ctx)
def base(request):
    return render(request, 'base.html')


@login_required
def room(request, room_name):
    room = get_object_or_404(Room, name=room_name)
    rooms = Room.objects.all()
    return render(request, 'chat/room.html', {
        'room_name': room.name,
        'rooms': rooms,
        'username': request.user.username
    })
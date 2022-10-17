from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Contact, Message, Chat
# Create your views here.
def index(request):
    contact = get_object_or_404(Contact, user=request.user)
    contact = contact.chats.all() #type:ignore
    print(contact)
    ctx = {'friends': contact}
    return render(request, 'chat/index.html', ctx)


# def base(request):
#     return render(request, 'base.html')


# # @login_required
# # def room(request, room_name):
# #     room = get_object_or_404(Room, name=room_name)
# #     rooms = Room.objects.all()
# #     return render(request, 'chat/room.html', {
# #         'room_name': room.name,
# #         'rooms': rooms,
# #         'username': request.user.username
# #     })
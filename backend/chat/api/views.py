from rest_framework import generics
from rest_framework import permissions
from rest_framework.authentication import SessionAuthentication
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model
from chat.api.serializers import MessageSerializer, RoomSerializer
from chat.models import Room, Message
# from oto.api.permissions import AuthorModifyOrReadOnly, IsAdminUserForObject

User = get_user_model()

class RoomList(generics.ListAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    permission_classes = [permissions.AllowAny]

class RoomCreate(generics.CreateAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer

class RoomDetail(generics.RetrieveUpdateDestroyAPIView):
    # permission_classes = (permissions.isAuthenticated,) #type: ignore
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    
class MessageList(generics.ListAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = [permissions.AllowAny]

class MessageCreate(generics.CreateAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

class MessageDetail(generics.RetrieveUpdateDestroyAPIView):
    # permission_classes = (permissions.isAuthenticated,) #type: ignore
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
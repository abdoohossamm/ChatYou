from rest_framework import generics
from rest_framework import permissions
from rest_framework.authentication import SessionAuthentication
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model
from oto.api.serializers import ChatSerializer
from oto.models import Chat, Contact
# from oto.api.permissions import AuthorModifyOrReadOnly, IsAdminUserForObject

User = get_user_model()
def get_user_contact(username):
    user = get_object_or_404(User, username=username)
    contact = get_object_or_404(Contact, user=user)
    return contact

class ChatList(generics.ListAPIView):
    # queryset = Chat.objects.all()
    serializer_class = ChatSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        queryset = Chat.objects.all()
        print(queryset)
        username = self.request.query_params.get('username', None)
        if username is not None:
            contact = get_user_contact(username)
            queryset = contact.chats.all()
        return queryset
class ChatCreate(generics.CreateAPIView):
    queryset = Chat.objects.all()
    serializer_class = ChatSerializer

class ChatDetail(generics.RetrieveUpdateDestroyAPIView):
    # permission_classes = (permissions.isAuthenticated,) #type: ignore
    queryset = Chat.objects.all()
    serializer_class = ChatSerializer
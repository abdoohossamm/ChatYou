from dataclasses import fields
from rest_framework import serializers
from oto.models import Chat

class ChatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chat
        fields = ('__all__')
from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Room(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name 
class Message(models.Model):
    user = models.ForeignKey(User, related_name='author', on_delete=models.CASCADE)
    content = models.TextField()
    time = models.DateTimeField(auto_now_add=True)
    room = models.ForeignKey(Room, related_name='message_room', on_delete=models.CASCADE)
    
    
    def __str__(self):
        return f"{self.user.username[:10]}: {self.content[:10]}"
    def last_30_msgs():
        return Message.objects.order_by("-time").all()[:30]
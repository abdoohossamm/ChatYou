from pyexpat.errors import messages
from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Contact(models.Model):
    user = models.ForeignKey(User, related_name= 'friends', on_delete=models.CASCADE)
    friends = models.ManyToManyField('self', blank=True)
    def __str__(self):
        return str(self.user.friends)

class Message(models.Model):
    contact = models.ForeignKey(Contact, related_name='messages', on_delete=models.CASCADE)
    content = models.TextField()
    time = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.contact}: {self.content}"
class Chat(models.Model):
    participants = models.ManyToManyField(Contact, related_name='chats')
    messages = models.ManyToManyField(Message, blank=True)
    def __str__(self):
        return f'{self.pk}'